from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from pymongo import MongoClient
import redis
from owm import OWM
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime, timedelta

load_dotenv()
app = FastAPI(title="DataFrost ML Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connections
mongo_client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = mongo_client["datafrost"]
redis_client = redis.Redis(host='localhost', port=6379, db=0)
owm = OWM(os.getenv("OWM_API_KEY"))

# ML Model for Impact Prediction
impact_model = RandomForestRegressor(n_estimators=100)
# Train on historical data (in production)
historical_data = pd.DataFrame({
    'temp': [-5, -8, -12, -3],
    'windchill': [-12, -15, -20, -8],
    'precip': [85, 92, 70, 60],
    'population_density': [1200, 800, 1500, 900],
    'impact_score': [0.92, 0.95, 0.88, 0.75]
})
impact_model.fit(historical_data[['temp','windchill','precip','population_density']], historical_data['impact_score'])

@app.get("/api/impact-forecast/{city}")
async def get_impact_forecast(city: str):
    """Predict community impact scores"""
    
    # Get real weather
    mgr = owm.weather_manager()
    observation = mgr.weather_at_city(city)
    weather = observation.weather
    
    # ML Prediction
    features = np.array([[
        weather.temperature('celsius')['temp'],
        weather.wind()['speed'] * 0.6 - 10,  # Windchill approx
        weather.rain or 0,
        1000  # Mock density
    ]])
    
    impact_score = impact_model.predict(features)[0]
    
    # Cache result
    forecast_key = f"impact:{city}:{datetime.now().strftime('%Y%m%d')}"
    redis_client.setex(forecast_key, 3600, impact_score)
    
    # Save to Mongo
    db.forecasts.insert_one({
        "city": city,
        "impact_score": float(impact_score),
        "weather": weather.to_dict(),
        "timestamp": datetime.utcnow()
    })
    
    return {
        "city": city,
        "impact_score": float(impact_score),
        "risk_level": "HIGH" if impact_score > 0.8 else "MEDIUM",
        "predicted_needs": {
            "heating_units": int(impact_score * 500),
            "delivery_zones": int(impact_score * 15)
        }
    }

@app.get("/api/volunteer-needs")
async def get_volunteer_needs():
    """Real-time volunteer matching"""
    needs = list(db.needs.find({}, {"_id": 0}).sort("urgency", -1).limit(5))
    return {"needs": needs}

@app.post("/api/logistics/route")
async def optimize_route(data: dict):
    """Smart route optimization (mock Google Maps API)"""
    # In production: integrate Google Directions API
    return {
        "standard_route": {"duration": 135, "distance": 45},
        "optimized_route": {"duration": 102, "distance": 38, "confidence": 0.94},
        "risk_avoided": 0.72
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
