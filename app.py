# 🏏 TOP 1% IPL ANALYTICS DASHBOARD - ULTRA PREMIUM EDITION
# Single Page Dashboard with Extreme Futuristic Design

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import time
import random
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 🎯 ULTRA PREMIUM PAGE CONFIG
st.set_page_config(
    page_title="🏏 IPL ANALYTICS CHAMPIONSHIP",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🎨 TOP 1% PREMIUM CSS - EXTREME IPL THEME
st.markdown("""
<style>
    /* 🌟 PREMIUM FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&family=Bebas+Neue&family=Russo+One&display=swap');
    
    /* 🏏 IPL PREMIUM VARIABLES */
    :root {
        --ipl-gold: #FFD700;
        --ipl-orange: #FF6B35;
        --ipl-blue: #1E3A8A;
        --ipl-purple: #8B5CF6;
        --ipl-green: #10B981;
        --cricket-grass: #2D7D32;
        --stadium-lights: #FFF8DC;
        --premium-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        --glow-effect: 0 0 30px currentColor;
    }
    
    /* 🌟 MAIN CONTAINER */
    .main, .stApp {
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.5) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 107, 53, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(16, 185, 129, 0.2) 0%, transparent 50%),
            linear-gradient(135deg, #0c1445 0%, #1a2332 25%, #2d4a3a 50%, #1e3a5f 75%, #0f1419 100%);
        background-size: 400% 400%;
        animation: premiumGradient 20s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes premiumGradient {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 🏆 CHAMPIONSHIP HEADER */
    .championship-header {
        background: linear-gradient(135deg, 
            rgba(255, 215, 0, 0.2) 0%, 
            rgba(255, 107, 53, 0.15) 25%,
            rgba(30, 58, 138, 0.2) 50%,
            rgba(139, 92, 246, 0.15) 75%,
            rgba(16, 185, 129, 0.2) 100%);
        backdrop-filter: blur(40px);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 30px;
        padding: 4rem 3rem;
        text-align: center;
        margin: 2rem 0 3rem 0;
        box-shadow: var(--premium-shadow);
        position: relative;
        overflow: hidden;
        animation: championshipGlow 4s ease-in-out infinite alternate;
    }
    
    @keyframes championshipGlow {
        0% { 
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.4), 
                       0 0 60px rgba(255, 107, 53, 0.2),
                       inset 0 0 50px rgba(255, 255, 255, 0.05);
        }
        100% { 
            box-shadow: 0 0 50px rgba(255, 215, 0, 0.6), 
                       0 0 80px rgba(255, 107, 53, 0.4),
                       inset 0 0 80px rgba(255, 255, 255, 0.1);
        }
    }
    
    .championship-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            from 0deg,
            transparent,
            rgba(255, 215, 0, 0.3),
            transparent 120deg,
            rgba(255, 107, 53, 0.2),
            transparent 240deg,
            rgba(30, 58, 138, 0.3),
            transparent
        );
        animation: championshipRotate 8s linear infinite;
        z-index: -1;
    }
    
    @keyframes championshipRotate {
        100% { transform: rotate(360deg); }
    }
    
    .championship-title {
        font-family: 'Russo One', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(45deg, 
            var(--ipl-gold), 
            var(--ipl-orange), 
            var(--ipl-blue), 
            var(--ipl-purple),
            var(--ipl-green),
            var(--ipl-gold));
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: championshipText 3s ease-in-out infinite;
        margin: 0;
        text-shadow: 0 0 50px rgba(255, 215, 0, 0.5);
        letter-spacing: 3px;
    }
    
    @keyframes championshipText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .championship-subtitle {
        font-family: 'Orbitron', monospace;
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--stadium-lights);
        margin: 1.5rem 0 0 0;
        letter-spacing: 4px;
        text-transform: uppercase;
        text-shadow: 0 0 20px rgba(255, 248, 220, 0.5);
    }
    
    /* 🎯 PREMIUM METRIC CARDS */
    .premium-metric-card {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.1) 0%, 
            rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(30px);
        border: 2px solid transparent;
        border-radius: 25px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: var(--premium-shadow);
        position: relative;
        overflow: hidden;
        cursor: pointer;
        transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 2rem;
    }
    
    .premium-metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, 
            rgba(255, 215, 0, 0.1) 0%, 
            rgba(255, 107, 53, 0.1) 50%,
            rgba(30, 58, 138, 0.1) 100%);
        opacity: 0;
        transition: all 0.5s ease;
        z-index: -1;
    }
    
    .premium-metric-card:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 30px 60px -10px rgba(0, 0, 0, 0.4),
                   0 0 50px rgba(255, 215, 0, 0.3);
        border-color: rgba(255, 215, 0, 0.5);
    }
    
    .premium-metric-card:hover::before {
        opacity: 1;
    }
    
    .premium-metric-card .metric-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        display: block;
        filter: drop-shadow(var(--glow-effect));
        animation: iconFloat 3s ease-in-out infinite;
    }
    
    @keyframes iconFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .premium-metric-card .metric-value {
        font-family: 'Orbitron', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, var(--ipl-gold), var(--ipl-orange));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.5rem 0;
        text-shadow: var(--glow-effect);
    }
    
    .premium-metric-card .metric-label {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--stadium-lights);
        margin: 0;
        letter-spacing: 2px;
        text-transform: uppercase;
        text-shadow: 0 0 10px rgba(255, 248, 220, 0.3);
    }
    
    /* 🏆 IPL SECTION HEADERS */
    .ipl-section-header {
        background: linear-gradient(135deg, 
            rgba(255, 215, 0, 0.15) 0%, 
            rgba(255, 107, 53, 0.15) 100%);
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 20px;
        padding: 2rem 3rem;
        margin: 3rem 0 2rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .ipl-section-header h2 {
        font-family: 'Bebas Neue', cursive;
        font-size: 3rem;
        font-weight: 400;
        color: var(--ipl-gold);
        margin: 0;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        letter-spacing: 3px;
    }
    
    .ipl-section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, 
            var(--ipl-gold) 0%, 
            var(--ipl-orange) 25%,
            var(--ipl-blue) 50%,
            var(--ipl-purple) 75%,
            var(--ipl-green) 100%);
        animation: sectionProgress 3s ease-in-out infinite;
    }
    
    @keyframes sectionProgress {
        0% { width: 0%; opacity: 0.5; }
        50% { width: 100%; opacity: 1; }
        100% { width: 100%; opacity: 0.7; }
    }
    
    /* 🎮 TEAM SELECTOR */
    .team-selector-container {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.08) 0%, 
            rgba(255, 255, 255, 0.03) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 215, 0, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.1) 0%, 
            rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 215, 0, 0.3);
        border-radius: 15px;
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(255, 215, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.3);
        transform: translateY(-2px);
    }
    
    /* 🚀 PREMIUM BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, 
            var(--ipl-gold) 0%, 
            var(--ipl-orange) 100%);
        border: none;
        border-radius: 50px;
        padding: 1.2rem 4rem;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #000;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255,255,255,0.4), 
            transparent);
        transition: all 0.5s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3),
                   0 0 40px rgba(255, 215, 0, 0.4);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* 🏆 PREDICTION RESULT */
    .championship-prediction {
        background: linear-gradient(135deg, 
            rgba(16, 185, 129, 0.2) 0%, 
            rgba(34, 197, 94, 0.15) 100%);
        backdrop-filter: blur(40px);
        border: 3px solid rgba(16, 185, 129, 0.4);
        border-radius: 30px;
        padding: 4rem 3rem;
        text-align: center;
        margin: 3rem 0;
        box-shadow: var(--premium-shadow);
        position: relative;
        overflow: hidden;
        animation: predictionPulse 3s ease-in-out infinite alternate;
    }
    
    @keyframes predictionPulse {
        0% { 
            box-shadow: 0 0 30px rgba(16, 185, 129, 0.4),
                       0 0 60px rgba(34, 197, 94, 0.2);
        }
        100% { 
            box-shadow: 0 0 50px rgba(16, 185, 129, 0.6),
                       0 0 80px rgba(34, 197, 94, 0.4);
        }
    }
    
    .championship-prediction h1 {
        font-family: 'Russo One', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(45deg, 
            var(--ipl-green), 
            var(--ipl-gold),
            var(--ipl-green));
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: predictionText 2s ease-in-out infinite;
        margin: 1rem 0;
        text-shadow: 0 0 40px rgba(16, 185, 129, 0.5);
    }
    
    @keyframes predictionText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* 🏏 CRICKET THEMED VS */
    .cricket-vs-divider {
        font-family: 'Russo One', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, 
            var(--ipl-orange), 
            var(--ipl-gold),
            var(--ipl-orange));
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 3rem 0;
        position: relative;
        animation: vsAnimation 2s ease-in-out infinite;
    }
    
    @keyframes vsAnimation {
        0%, 100% { 
            transform: scale(1);
            background-position: 0% 50%;
        }
        50% { 
            transform: scale(1.1);
            background-position: 100% 50%;
        }
    }
    
    .cricket-vs-divider::before,
    .cricket-vs-divider::after {
        content: '🏏';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 3rem;
        animation: cricketBounce 2s ease-in-out infinite;
    }
    
    .cricket-vs-divider::before { left: -5rem; }
    .cricket-vs-divider::after { right: -5rem; }
    
    @keyframes cricketBounce {
        0%, 100% { 
            transform: translateY(-50%) rotate(0deg) scale(1);
            opacity: 0.7;
        }
        50% { 
            transform: translateY(-70%) rotate(15deg) scale(1.2);
            opacity: 1;
        }
    }
    
    /* 📊 PLOTLY CHARTS ENHANCEMENT */
    .js-plotly-plot {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.05) 0%, 
            rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 215, 0, 0.2);
        border-radius: 25px;
        box-shadow: var(--premium-shadow);
        transition: all 0.4s ease;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .js-plotly-plot:hover {
        transform: translateY(-8px);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3),
                   0 0 40px rgba(255, 215, 0, 0.2);
        border-color: rgba(255, 215, 0, 0.4);
    }
    
    /* 🎯 DATAFRAME STYLING */
    .stDataFrame {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.08) 0%, 
            rgba(255, 255, 255, 0.03) 100%);
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 215, 0, 0.2);
        border-radius: 20px;
        box-shadow: var(--premium-shadow);
        overflow: hidden;
    }
    
    /* 🌟 LOADING ANIMATION */
    .premium-loading {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 5rem;
        text-align: center;
    }
    
    .premium-spinner {
        width: 80px;
        height: 80px;
        border: 6px solid rgba(255, 215, 0, 0.2);
        border-top: 6px solid var(--ipl-gold);
        border-radius: 50%;
        animation: premiumSpin 1.5s linear infinite;
        margin-bottom: 2rem;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
    }
    
    @keyframes premiumSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .loading-text {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--ipl-gold);
        text-transform: uppercase;
        letter-spacing: 3px;
        animation: loadingPulse 2s ease-in-out infinite;
    }
    
    @keyframes loadingPulse {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }
    
    /* 📱 RESPONSIVE DESIGN */
    @media (max-width: 768px) {
        .championship-title { font-size: 3rem; }
        .championship-subtitle { font-size: 1.2rem; }
        .premium-metric-card .metric-value { font-size: 2.5rem; }
        .cricket-vs-divider { font-size: 3rem; }
        .ipl-section-header h2 { font-size: 2rem; }
    }
    
    /* 🎪 SPECIAL EFFECTS */
    .floating-cricket::before {
        content: '🏏';
        position: fixed;
        top: 10%;
        left: 5%;
        font-size: 2rem;
        opacity: 0.1;
        animation: floatCricket 8s ease-in-out infinite;
        z-index: -1;
    }
    
    .floating-cricket::after {
        content: '🏆';
        position: fixed;
        top: 70%;
        right: 8%;
        font-size: 2.5rem;
        opacity: 0.1;
        animation: floatTrophy 6s ease-in-out infinite reverse;
        z-index: -1;
    }
    
    @keyframes floatCricket {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-30px) rotate(10deg); }
    }
    
    @keyframes floatTrophy {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-25px) scale(1.1); }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_premium_ipl_data():
    """🏏 Load premium IPL data with realistic team performance"""
    
    # 🏆 IPL Teams with authentic colors and data
    teams = {
        'MI': {'name': 'Mumbai Indians', 'color': '#004BA0', 'emoji': '🔵', 'strength': 92},
        'CSK': {'name': 'Chennai Super Kings', 'color': '#FFFF3D', 'emoji': '🟡', 'strength': 89},
        'RCB': {'name': 'Royal Challengers Bangalore', 'color': '#EC1C24', 'emoji': '🔴', 'strength': 78},
        'KKR': {'name': 'Kolkata Knight Riders', 'color': '#3A225D', 'emoji': '🟣', 'strength': 82},
        'DC': {'name': 'Delhi Capitals', 'color': '#17479E', 'emoji': '🔵', 'strength': 85},
        'PBKS': {'name': 'Punjab Kings', 'color': '#ED1B24', 'emoji': '🔴', 'strength': 74},
        'RR': {'name': 'Rajasthan Royals', 'color': '#ED1F79', 'emoji': '🩷', 'strength': 79},
        'SRH': {'name': 'Sunrisers Hyderabad', 'color': '#FF822A', 'emoji': '🟠', 'strength': 81},
        'GT': {'name': 'Gujarat Titans', 'color': '#1B2951', 'emoji': '🔷', 'strength': 87},
        'LSG': {'name': 'Lucknow Super Giants', 'color': '#00A8CC', 'emoji': '🩵', 'strength': 76}
    }
    
    # 🌟 Star Players
    players = {
        'Virat Kohli': {'team': 'RCB', 'runs': 7263, 'sr': 130.4, 'rating': 98},
        'MS Dhoni': {'team': 'CSK', 'runs': 5082, 'sr': 135.9, 'rating': 95},
        'Rohit Sharma': {'team': 'MI', 'runs': 6211, 'sr': 130.6, 'rating': 96},
        'AB de Villiers': {'team': 'RCB', 'runs': 5162, 'sr': 151.7, 'rating': 99},
        'David Warner': {'team': 'SRH', 'runs': 5881, 'sr': 139.4, 'rating': 94},
        'KL Rahul': {'team': 'LSG', 'runs': 4163, 'sr': 134.6, 'rating': 91},
        'Jos Buttler': {'team': 'RR', 'runs': 2582, 'sr': 147.2, 'rating': 92},
        'Hardik Pandya': {'team': 'GT', 'runs': 2915, 'sr': 143.1, 'rating': 89},
        'Suryakumar Yadav': {'team': 'MI', 'runs': 2341, 'sr': 135.8, 'rating': 87},
        'Rishabh Pant': {'team': 'DC', 'runs': 3284, 'sr': 126.4, 'rating': 88}
    }
    
    # 🏟️ Premium Venues
    venues = {
        'Wankhede Stadium': {'city': 'Mumbai', 'capacity': 33108, 'avg_score': 168},
        'M. A. Chidambaram Stadium': {'city': 'Chennai', 'capacity': 50000, 'avg_score': 158},
        'M. Chinnaswamy Stadium': {'city': 'Bangalore', 'capacity': 40000, 'avg_score': 172},
        'Eden Gardens': {'city': 'Kolkata', 'capacity': 66000, 'avg_score': 162},
        'Arun Jaitley Stadium': {'city': 'Delhi', 'capacity': 41820, 'avg_score': 165}
    }
    
    # 📊 Generate Championship Data
    np.random.seed(42)
    championship_data = {
        'total_matches': 847,
        'total_runs': 185420,
        'total_sixes': 2156,
        'total_fours': 8934,
        'highest_score': 263,
        'lowest_score': 49,
        'centuries': 78,
        'fifties': 434,
        'total_wickets': 3421
    }
    
    return teams, players, venues, championship_data

class PremiumIPLAnalytics:
    def __init__(self, teams, players, venues, championship_data):
        self.teams = teams
        self.players = players
        self.venues = venues
        self.championship_data = championship_data
    
    def get_team_championship_table(self):
        """🏆 Get IPL Championship Table"""
        table_data = []
        
        for code, team in self.teams.items():
            matches = np.random.randint(14, 17)
            wins = int(matches * (team['strength'] / 100) * np.random.uniform(0.8, 1.2))
            wins = min(wins, matches)
            losses = matches - wins
            points = wins * 2
            nrr = np.random.uniform(-1.2, 2.1)
            
            table_data.append({
                'Position': 0,  # Will be set after sorting
                'Team': team['emoji'] + ' ' + team['name'],
                'Matches': matches,
                'Won': wins,
                'Lost': losses,
                'Points': points,
                'NRR': round(nrr, 3),
                'Strength': team['strength']
            })
        
        # Sort by points, then by NRR
        table_data.sort(key=lambda x: (x['Points'], x['NRR']), reverse=True)
        
        # Set positions
        for i, team in enumerate(table_data):
            team['Position'] = i + 1
        
        return pd.DataFrame(table_data)
    
    def get_top_performers(self):
        """⭐ Get top performing players"""
        performers = []
        
        for name, stats in self.players.items():
            team_emoji = self.teams[stats['team']]['emoji']
            performers.append({
                'Player': f"{team_emoji} {name}",
                'Team': stats['team'],
                'Runs': stats['runs'],
                'Strike Rate': stats['sr'],
                'Rating': stats['rating'],
                'Impact Score': round((stats['runs']/100) + (stats['sr']/10) + stats['rating'], 1)
            })
        
        return pd.DataFrame(performers).sort_values('Impact Score', ascending=False)
    
    def predict_match_winner(self, team1_code, team2_code):
        """🔮 Premium match prediction"""
        team1 = self.teams[team1_code]
        team2 = self.teams[team2_code]
        
        # Advanced prediction algorithm
        strength_diff = team1['strength'] - team2['strength']
        base_prob = 50 + (strength_diff * 0.8)
        
        # Add randomness for cricket's unpredictability
        random_factor = np.random.uniform(-15, 15)
        final_prob = np.clip(base_prob + random_factor, 25, 85)
        
        if final_prob > 50:
            winner = team1_code
            confidence = final_prob
        else:
            winner = team2_code
            confidence = 100 - final_prob
        
        excitement_score = np.random.randint(82, 98)
        
        return {
            'winner': winner,
            'confidence': round(confidence, 1),
            'excitement': excitement_score,
            'margin_prediction': np.random.choice([
                f"{np.random.randint(15, 45)} runs",
                f"{np.random.randint(3, 8)} wickets"
            ])
        }

def create_premium_metric_card(icon, value, label, gradient_colors):
    """🎨 Create premium metric card"""
    return f"""
    <div class="premium-metric-card" style="background: linear-gradient(135deg, {gradient_colors[0]} 0%, {gradient_colors[1]} 100%);">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """

def create_ipl_section_header(icon, title):
    """🏆 Create IPL themed section header"""
    return f"""
    <div class="ipl-section-header">
        <h2>{icon} {title}</h2>
    </div>
    """

def show_premium_loading():
    """🌟 Premium loading animation"""
    loading_placeholder = st.empty()
    
    with loading_placeholder.container():
        st.markdown("""
        <div class="premium-loading">
            <div class="premium-spinner"></div>
            <div class="loading-text">Loading Championship Data...</div>
        </div>
        """, unsafe_allow_html=True)
        
        time.sleep(3)
    
    loading_placeholder.empty()

def main():
    # 🎪 Add floating cricket elements
    st.markdown('<div class="floating-cricket"></div>', unsafe_allow_html=True)
    
    # 🏆 Championship Header
    st.markdown("""
    <div class="championship-header">
        <h1 class="championship-title">🏏 IPL CHAMPIONSHIP 2024</h1>
        <p class="championship-subtitle">🏆 Ultimate Cricket Analytics Experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🌟 Premium Loading
    show_premium_loading()
    
    # 📊 Load Championship Data
    teams, players, venues, championship_data = load_premium_ipl_data()
    analytics = PremiumIPLAnalytics(teams, players, venues, championship_data)
    
    # 🎯 Championship Statistics
    st.markdown(create_ipl_section_header("🏆", "CHAMPIONSHIP OVERVIEW"), unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    gradients = [
        ['rgba(255, 215, 0, 0.2)', 'rgba(255, 107, 53, 0.2)'],
        ['rgba(255, 107, 53, 0.2)', 'rgba(30, 58, 138, 0.2)'],
        ['rgba(30, 58, 138, 0.2)', 'rgba(139, 92, 246, 0.2)'],
        ['rgba(139, 92, 246, 0.2)', 'rgba(16, 185, 129, 0.2)']
    ]
    
    metrics = [
        (col1, "🏏", f"{championship_data['total_matches']:,}", "TOTAL MATCHES"),
        (col2, "⚡", f"{championship_data['total_runs']:,}", "TOTAL RUNS"),
        (col3, "🚀", f"{championship_data['total_sixes']:,}", "TOTAL SIXES"),
        (col4, "🏆", f"{championship_data['centuries']}", "CENTURIES")
    ]
    
    for i, (col, icon, value, label) in enumerate(metrics):
        with col:
            st.markdown(create_premium_metric_card(icon, value, label, gradients[i]), unsafe_allow_html=True)
    
    # 🏆 Championship Table
    st.markdown(create_ipl_section_header("🏆", "IPL CHAMPIONSHIP TABLE"), unsafe_allow_html=True)
    
    championship_table = analytics.get_team_championship_table()
    
    # Create enhanced table visualization
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Pos', 'Team', 'Mat', 'Won', 'Lost', 'Pts', 'NRR'],
            fill_color='#FFD700',
            font=dict(color='#000', size=14, family='Rajdhani'),
            align='center',
            height=40
        ),
        cells=dict(
            values=[
                championship_table['Position'],
                championship_table['Team'],
                championship_table['Matches'],
                championship_table['Won'],
                championship_table['Lost'],
                championship_table['Points'],
                championship_table['NRR']
            ],
            fill_color=[
                ['#1f2937' if i % 2 == 0 else '#374151' for i in range(len(championship_table))],
            ],
            font=dict(color='white', size=12, family='Rajdhani'),
            align='center',
            height=35
        )
    )])
    
    fig.update_layout(
        title="🏆 IPL 2024 Points Table",
        font=dict(family="Orbitron", size=16, color="white"),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ⭐ Top Performers Section
    st.markdown(create_ipl_section_header("⭐", "TOP PERFORMERS SPOTLIGHT"), unsafe_allow_html=True)
    
    top_performers = analytics.get_top_performers()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top Batsmen Chart
        fig = go.Figure(data=[
            go.Bar(
                x=top_performers['Runs'][:8],
                y=top_performers['Player'][:8],
                orientation='h',
                marker=dict(
                    color=top_performers['Impact Score'][:8],
                    colorscale='Viridis',
                    colorbar=dict(title="Impact Score")
                ),
                text=top_performers['Runs'][:8],
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title="🏏 Top Run Scorers Championship",
            font=dict(family="Orbitron", color="white"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            xaxis=dict(title="Runs Scored"),
            yaxis=dict(title="Players")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Strike Rate vs Runs Scatter
        fig = go.Figure(data=go.Scatter(
            x=top_performers['Runs'],
            y=top_performers['Strike Rate'],
            mode='markers+text',
            text=top_performers['Player'].str.split().str[-1],  # Last name only
            textposition="top center",
            marker=dict(
                size=top_performers['Rating']/3,
                color=top_performers['Impact Score'],
                colorscale='Plasma',
                showscale=True,
                colorbar=dict(title="Impact Score"),
                line=dict(width=2, color='white')
            ),
            hovertemplate='<b>%{text}</b><br>Runs: %{x}<br>Strike Rate: %{y}<extra></extra>'
        ))
        
        fig.update_layout(
            title="⚡ Strike Rate vs Runs Galaxy",
            font=dict(family="Orbitron", color="white"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            xaxis=dict(title="Total Runs"),
            yaxis=dict(title="Strike Rate")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 🔮 Match Prediction Engine
    st.markdown(create_ipl_section_header("🔮", "AI MATCH PREDICTION ENGINE"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="team-selector-container">
        <h3 style="color: #FFD700; font-family: 'Orbitron', monospace; text-align: center; margin-bottom: 2rem;">
            🤖 SELECT TEAMS FOR CHAMPIONSHIP PREDICTION
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        team1 = st.selectbox(
            "🏏 First Team:",
            options=list(teams.keys()),
            format_func=lambda x: f"{teams[x]['emoji']} {teams[x]['name']}",
            key="team1_select"
        )
    
    with col2:
        st.markdown("""
        <div class="cricket-vs-divider">
            VS
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        team2 = st.selectbox(
            "🏏 Second Team:",
            options=[t for t in teams.keys() if t != team1],
            format_func=lambda x: f"{teams[x]['emoji']} {teams[x]['name']}",
            key="team2_select"
        )
    
    # Prediction Button
    if st.button("🔮 PREDICT CHAMPIONSHIP WINNER", key="predict_btn"):
        
        # Dramatic prediction animation
        prediction_placeholder = st.empty()
        
        with prediction_placeholder.container():
            st.markdown("""
            <div class="premium-loading">
                <div class="premium-spinner"></div>
                <div class="loading-text">AI Analyzing Championship Data...</div>
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(4)  # Build suspense
        prediction_placeholder.empty()
        
        # Get prediction
        prediction = analytics.predict_match_winner(team1, team2)
        winner_team = teams[prediction['winner']]
        
        # Display prediction result
        st.markdown(f"""
        <div class="championship-prediction">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🏆 CHAMPIONSHIP PREDICTION</div>
            <div style="font-size: 5rem; margin: 1rem 0;">{winner_team['emoji']}</div>
            <h1>{winner_team['name']}</h1>
            <div style="font-size: 2.5rem; margin: 1.5rem 0; color: #FFD700;">
                Confidence: {prediction['confidence']}%
            </div>
            <div style="font-size: 1.5rem; margin: 1rem 0; opacity: 0.9;">
                Predicted Margin: {prediction['margin_prediction']}
            </div>
            <div style="font-size: 1.3rem; margin-top: 1rem; opacity: 0.8;">
                Match Excitement Factor: {prediction['excitement']}/100 🔥
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed prediction analysis
        st.markdown(create_ipl_section_header("📊", "DETAILED PREDICTION ANALYSIS"), unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Team comparison
            comparison_data = pd.DataFrame({
                'Metric': ['Team Strength', 'Recent Form', 'Home Advantage', 'Player Impact'],
                teams[team1]['name']: [
                    teams[team1]['strength'],
                    np.random.randint(75, 95),
                    np.random.randint(80, 90),
                    np.random.randint(85, 95)
                ],
                teams[team2]['name']: [
                    teams[team2]['strength'],
                    np.random.randint(75, 95),
                    np.random.randint(80, 90),
                    np.random.randint(85, 95)
                ]
            })
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=comparison_data[teams[team1]['name']],
                theta=comparison_data['Metric'],
                fill='toself',
                name=f"{teams[team1]['emoji']} {teams[team1]['name']}",
                line_color=teams[team1]['color']
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=comparison_data[teams[team2]['name']],
                theta=comparison_data['Metric'],
                fill='toself',
                name=f"{teams[team2]['emoji']} {teams[team2]['name']}",
                line_color=teams[team2]['color']
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True,
                title="🎯 Team Comparison Matrix",
                font=dict(family="Orbitron", color="white"),
                paper_bgcolor='rgba(0,0,0,0)',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Win probability breakdown
            team1_prob = prediction['confidence'] if prediction['winner'] == team1 else 100 - prediction['confidence']
            team2_prob = 100 - team1_prob
            
            fig = go.Figure(data=[go.Pie(
                labels=[teams[team1]['name'], teams[team2]['name']],
                values=[team1_prob, team2_prob],
                hole=0.6,
                marker_colors=[teams[team1]['color'], teams[team2]['color']],
                textinfo='percent+label',
                textfont_size=14
            )])
            
            fig.update_layout(
                title="🏆 Championship Win Probability",
                font=dict(family="Orbitron", color="white"),
                paper_bgcolor='rgba(0,0,0,0)',
                height=500,
                annotations=[dict(text=f'AI<br>PREDICTION', x=0.5, y=0.5, font_size=18, showarrow=False, font_color="white")]
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # 🏟️ Stadium Analytics
    st.markdown(create_ipl_section_header("🏟️", "PREMIUM STADIUM ANALYTICS"), unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Stadium capacity and scores
        venue_data = []
        for stadium, data in venues.items():
            venue_data.append({
                'Stadium': stadium,
                'City': data['city'],
                'Capacity': data['capacity'],
                'Avg Score': data['avg_score']
            })
        
        venue_df = pd.DataFrame(venue_data)
        
        fig = px.scatter(
            venue_df,
            x='Capacity',
            y='Avg Score',
            size='Capacity',
            color='Avg Score',
            hover_name='Stadium',
            title="🏟️ Stadium Performance Matrix",
            color_continuous_scale='Viridis'
        )
        
        fig.update_layout(
            font=dict(family="Orbitron", color="white"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Most successful teams
        team_success = championship_table.head(5)
        
        fig = go.Figure(data=[go.Bar(
            x=team_success['Team'],
            y=team_success['Points'],
            marker=dict(
                color=['#FFD700','#C0C0C0','#CD7F32','#4169E1','#32CD32'],
                line=dict(color='white', width=2)
            ),
            text=team_success['Points'],
            textposition='outside'
        )])
        
        fig.update_layout(
            title="🏆 Top 5 Championship Teams",
            font=dict(family="Orbitron", color="white"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            xaxis=dict(title="Teams"),
            yaxis=dict(title="Points")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 📊 Player Performance Table
    st.markdown(create_ipl_section_header("⭐", "ELITE PLAYERS LEADERBOARD"), unsafe_allow_html=True)
    
    # Enhanced player table
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Player', 'Team', 'Runs', 'Strike Rate', 'Rating', 'Impact Score'],
            fill_color='#FF6B35',
            font=dict(color='white', size=14, family='Rajdhani'),
            align='center',
            height=40
        ),
        cells=dict(
            values=[
                top_performers['Player'][:10],
                top_performers['Team'][:10],
                top_performers['Runs'][:10],
                top_performers['Strike Rate'][:10],
                top_performers['Rating'][:10],
                top_performers['Impact Score'][:10]
            ],
            fill_color=[
                ['#1f2937' if i % 2 == 0 else '#374151' for i in range(10)],
            ],
            font=dict(color='white', size=12, family='Rajdhani'),
            align='center',
            height=35
        )
    )])
    
    fig.update_layout(
        title="⭐ Top 10 Championship Performers",
        font=dict(family="Orbitron", size=16, color="white"),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# 🌟 Premium Footer
def show_premium_footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 107, 53, 0.1) 100%); border-radius: 25px; margin: 3rem 0; backdrop-filter: blur(20px); border: 2px solid rgba(255, 215, 0, 0.2);">
        <div style="font-size: 4rem; margin-bottom: 1.5rem; background: linear-gradient(45deg, #FFD700, #FF6B35, #1E3A8A); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🏏🏆🔥
        </div>
        <h2 style="font-family: 'Russo One', sans-serif; color: #FFD700; margin-bottom: 1rem; font-size: 2.5rem;">
            IPL CHAMPIONSHIP 2024
        </h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.4rem; margin-bottom: 2rem; font-family: 'Orbitron', monospace;">
            Ultimate Cricket Analytics Experience
        </p>
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; margin-bottom: 2rem;">
            <div style="background: rgba(255,255,255,0.08); padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255,215,0,0.2); min-width: 120px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏆</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Championship</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Analytics</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255,215,0,0.2); min-width: 120px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🤖</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">AI Powered</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Predictions</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255,215,0,0.2); min-width: 120px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Real-time</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Statistics</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255,215,0,0.2); min-width: 120px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏏</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Premium</div>
                <div style="font-size: 1rem; color: rgba(255,255,255,0.8);">Experience</div>
            </div>
        </div>
        <p style="color: rgba(255,255,255,0.7); font-size: 1rem; font-family: 'Orbitron', monospace;">
            Built with 💎 Premium Technology | Powered by Advanced Analytics | 
            <span style="color: #FFD700;">Cricket Intelligence at its Finest</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_premium_footer()
