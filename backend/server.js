const express = require('express');
const cors = require('cors');
const axios = require('axios');
const Redis = require('redis');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
app.use(cors({ origin: 'http://localhost:3000' }));
app.use(express.json());

// Redis
const redis = Redis.createClient();
redis.connect();

// Auth middleware (JWT in production)
const authenticate = (req, res, next) => {
    // Mock auth for demo
    req.user = { id: 1, role: 'volunteer' };
    next();
};

// Routes
app.get('/api/dashboard', authenticate, async (req, res) => {
    const cacheKey = 'dashboard:summary';
    
    let data = await redis.get(cacheKey);
    if (!data) {
        // Fetch from Python ML
        const [forecast, needs] = await Promise.all([
            axios.get('http://localhost:8001/api/impact-forecast/New%20York'),
            axios.get('http://localhost:8001/api/volunteer-needs')
        ]);
        
        data = {
            impact_forecast: forecast.data,
            volunteer_needs: needs.data.needs.slice(0, 4),
            timestamp: new Date().toISOString()
        };
        
        await redis.setEx(cacheKey, 300, JSON.stringify(data)); // 5min cache
    }
    
    res.json(JSON.parse(data));
});

app.get('/api/energy-stats', authenticate, async (req, res) => {
    // Mock energy data (integrate smart meter API)
    res.json({
        grid_stress: 0.82,
        anomalies: [{ building: 47, excess: 38 }],
        recommendations: [
            { action: 'thermostat_2c', savings: 14 },
            { action: 'shift_laundry', savings: 9 }
        ]
    });
});

app.post('/api/volunteer/match', authenticate, async (req, res) => {
    const { skills } = req.body;
    // Query MongoDB + ML matching
    res.json({
        matches: [
            { task: 'Clinic insulation', impact: 0.91, location: 'North Sector' },
            { task: 'Snow clearing', impact: 0.85, location: 'East' }
        ]
    });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`🚀 DataFrost Node Gateway on port ${PORT}`);
});
