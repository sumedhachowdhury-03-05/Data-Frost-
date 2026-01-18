# DataFrost ❄️ – Winter Intelligence Dashboard

**DataFrost transforms winter data into community impact.**
Real-time OpenWeatherMap APIs combined with ML predictions (Scikit-learn) power live impact heatmaps, 94% ETA logistics routing, $14/week energy savings insights, and skill‑matched volunteering alerts.

Built for **Winter of Code 5.0** under **Data Science, Web Development, and Open Innovation** tracks.

[![Winter of Code](https://img.shields.io/badge/Winter%20of%20Code-5.0-blueviolet)](https://winter-of-code.tech)

##                                                   🏅  ![Winter of Code 5.0 Contributor] : 🏅 
<img width="140" height="120" alt="WoC 5 0 - Contributor Badge Black" src="https://github.com/user-attachments/assets/559a2c02-0826-49f1-8112-3a4ffa413c39" />


---

## ✨ Live Features

🔥 **Live Impact Heatmaps** – ML‑predicted cold‑risk zones from real weather data                                                                                                                                  
🚚 **Predictive Logistics** – Frost‑Route Planner with **94% ETA confidence**                                                                                                                                      
⚡ **Energy Optimization** – Grid stress meter + **$14 weekly savings insight**                                                                                                                                    
👥 **Volunteering Matcher** – Skill‑to‑need mapping (**14 volunteers needed NOW**)                        

---

## 🛠️ Tech Stack

**Frontend**
HTML5 · TailwindCSS · Chart.js · Leaflet
Glassmorphism “Frost” UI theme

**Backend**
FastAPI (Python ML Engine) · Node.js API Gateway
MongoDB · Redis

**Data & ML**
Pandas (Impact prediction models)

**APIs**
OpenWeatherMap · Google Maps (ready)

**Deployment**
 Vercel

---

## 🚀 Quick Start

### Option 1: HTML Demo (Works Immediately)

```bash
# VS Code: Save as frontend/datafrost-final.html
# Double-click the file to run in browser
```

### Option 2: Full Stack (Real ML Data)

```bash
# 1. Clone project
git clone <your-repo> && cd datafrost

# 2. Start backend services
vercel-compose up --build

# 3. Access dashboard
http://localhost:3000
```
---

## 🎯 Winter of Code 5.0 Tracks

✅ **Data Science & AI** – ML‑based impact prediction models                                                                                                                                                       
✅ **Web Development** – Responsive glassmorphism dashboard                                                                                                                                                        
✅ **Open Innovation** – Modular seasonal crisis intelligence platform

---

## 📊 Real-Time Data Sources

🌤️ **OpenWeatherMap API** → Live temperature & windchill                                                                                                                                                     
🤖 **Scikit‑learn** → Impact score predictions                                                                                                                                                                  
🗄️ **MongoDB** → Volunteer & logistics data                                                                                                                                                                      
⚡ **Redis** → 5‑minute caching layer                                                                                                                                                                           

---

## 🔗 API Endpoints (Backend Running)

```text
GET  http://localhost:8001/api/impact-forecast/{city}   # ML predictions
GET  http://localhost:3001/api/dashboard                # Unified dashboard data
POST http://localhost:3001/api/volunteer/match          # Skill matching
GET  http://localhost:8001/docs                         # FastAPI interactive docs
```

---

## 🎨 UI Features

✅ Glassmorphism "Frost" theme with backdrop blur                                                                                                                                                               
✅ 5 separate pages with smooth transitions                                                                                                                                                                        
✅ Gmail‑only login (@gmail.com) + strong validation                                                                                                                                                            
✅ Backend‑aware real‑time hooks                                                                                                                                                                               
✅ Mobile‑responsive + hover animations                                                                                                                                                                         
✅ Password rules: 8+ chars, 1 uppercase, 1 number, 1 special character                                                                                                                                           

---

## 🏆 Demo Metrics

```text
High Risk Zones     : 17 (ML predicted)
ETA Confidence      : 94%
Grid Stress         : 82% (Near freezing)
Volunteers Needed   : 14 (North Sector)
Weekly Savings      : $14 (Thermostat optimization)
---

## 🚀 Run Commands (Manual)

```bash
# Terminal 1 – Python ML Backend
cd backend/python-api
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

```bash
# Terminal 2 – Node Gateway
cd backend/node-server
npm install
npm run dev
```

```text
# Terminal 3 – Frontend
Open frontend/datafrost-final.html in browser
```

---

## 👤 Author

**Sumedha Chowdhury**
