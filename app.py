# IPL Analytics Dashboard - Complete Project (FIXED VERSION)
# File: app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    .main {
        font-family: 'Roboto', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin: 10px 0 0 0;
        opacity: 0.9;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ff9a56 0%, #ff6b35 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .metric-card h2 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .metric-card p {
        font-size: 1rem;
        margin: 5px 0 0 0;
        opacity: 0.9;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    .prediction-result {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    .vs-divider {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #ff6b35;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load IPL dataset - creates realistic sample data"""
    return create_realistic_ipl_data()

def create_realistic_ipl_data():
    """Create realistic IPL dataset based on actual patterns"""
    
    # IPL Teams with their actual names
    teams = {
        'MI': 'Mumbai Indians',
        'CSK': 'Chennai Super Kings', 
        'RCB': 'Royal Challengers Bangalore',
        'KKR': 'Kolkata Knight Riders',
        'DC': 'Delhi Capitals',
        'PBKS': 'Punjab Kings',
        'RR': 'Rajasthan Royals',
        'SRH': 'Sunrisers Hyderabad',
        'GT': 'Gujarat Titans',
        'LSG': 'Lucknow Super Giants'
    }
    
    # Famous IPL players
    players = [
        'Virat Kohli', 'MS Dhoni', 'Rohit Sharma', 'KL Rahul', 'Shikhar Dhawan',
        'AB de Villiers', 'David Warner', 'Jos Buttler', 'Rishabh Pant', 
        'Hardik Pandya', 'Ravindra Jadeja', 'Jasprit Bumrah', 'Yuzvendra Chahal',
        'Rashid Khan', 'Andre Russell', 'Glenn Maxwell', 'Faf du Plessis',
        'Quinton de Kock', 'Suryakumar Yadav', 'Ishan Kishan', 'Ruturaj Gaikwad',
        'Shreyas Iyer', 'Sanju Samson', 'Kane Williamson', 'Jonny Bairstow'
    ]
    
    # IPL Venues
    venues = [
        'Wankhede Stadium, Mumbai', 'M. A. Chidambaram Stadium, Chennai',
        'M. Chinnaswamy Stadium, Bangalore', 'Eden Gardens, Kolkata',
        'Arun Jaitley Stadium, Delhi', 'PCA Stadium, Mohali',
        'Sawai Mansingh Stadium, Jaipur', 'Rajiv Gandhi Intl Stadium, Hyderabad',
        'Narendra Modi Stadium, Ahmedabad', 'BRSABV Ekana Stadium, Lucknow'
    ]
    
    # Generate matches data (2020-2024 seasons)
    np.random.seed(42)  # For reproducible data
    matches_data = []
    match_id = 1
    
    for season in range(2020, 2025):
        # Each season has around 70-74 matches
        num_matches = np.random.randint(70, 75)
        
        for _ in range(num_matches):
            team1 = np.random.choice(list(teams.keys()))
            team2 = np.random.choice([t for t in teams.keys() if t != team1])
            
            # Winner probability based on team strength (realistic)
            team_strength = {
                'MI': 0.65, 'CSK': 0.62, 'RCB': 0.45, 'KKR': 0.55,
                'DC': 0.58, 'PBKS': 0.42, 'RR': 0.48, 'SRH': 0.52,
                'GT': 0.60, 'LSG': 0.50
            }
            
            if np.random.random() < team_strength.get(team1, 0.5):
                winner = team1
            else:
                winner = team2
            
            toss_winner = np.random.choice([team1, team2])
            toss_decision = np.random.choice(['bat', 'field'], p=[0.6, 0.4])  # Teams prefer batting first
            
            # Win margins
            if np.random.random() < 0.6:  # 60% win by runs
                win_by_runs = np.random.randint(1, 85)
                win_by_wickets = 0
            else:  # 40% win by wickets
                win_by_runs = 0
                win_by_wickets = np.random.randint(1, 11)
            
            matches_data.append({
                'id': match_id,
                'season': season,
                'date': f"{season}-0{np.random.randint(3,6)}-{np.random.randint(10,29)}",
                'team1': team1,
                'team2': team2,
                'venue': np.random.choice(venues),
                'toss_winner': toss_winner,
                'toss_decision': toss_decision,
                'winner': winner,
                'win_by_runs': win_by_runs,
                'win_by_wickets': win_by_wickets,
                'player_of_match': np.random.choice(players),
                'umpire1': f"Umpire {np.random.randint(1, 20)}",
                'umpire2': f"Umpire {np.random.randint(1, 20)}"
            })
            match_id += 1
    
    # Generate deliveries data - FIXED VERSION
    deliveries_data = []
    
    for match in matches_data[:100]:  # Generate detailed data for first 100 matches
        match_id = match['id']
        batting_team = match['team1']
        bowling_team = match['team2']
        
        # Generate 120 balls (20 overs) for first innings
        for ball_num in range(1, 121):
            over_num = ((ball_num - 1) // 6) + 1
            ball_in_over = ((ball_num - 1) % 6) + 1
            
            # FIXED: Ensure at least one player is selected
            available_batsmen = [p for p in players if np.random.random() < 0.4]
            if not available_batsmen:  # If no players selected, add at least one
                available_batsmen = [np.random.choice(players)]
            batsman = np.random.choice(available_batsmen)
            
            available_bowlers = [p for p in players if np.random.random() < 0.4 and p != batsman]
            if not available_bowlers:  # If no bowlers selected, add at least one
                available_bowlers = [np.random.choice([p for p in players if p != batsman])]
            bowler = np.random.choice(available_bowlers)
            
            # Non-striker (different from batsman)
            available_non_strikers = [p for p in players if p != batsman and np.random.random() < 0.3]
            if not available_non_strikers:
                available_non_strikers = [np.random.choice([p for p in players if p != batsman])]
            non_striker = np.random.choice(available_non_strikers)
            
            # Realistic run distribution
            runs_prob = [0.35, 0.25, 0.15, 0.08, 0.12, 0.03, 0.02]  # 0,1,2,3,4,6,wicket
            outcome = np.random.choice([0, 1, 2, 3, 4, 6, -1], p=runs_prob)
            
            if outcome == -1:  # Wicket
                batsman_runs = 0
                is_wicket = 1
                total_runs = 0
            else:
                batsman_runs = outcome
                is_wicket = 0
                total_runs = outcome
            
            deliveries_data.append({
                'match_id': match_id,
                'inning': 1,
                'batting_team': batting_team,
                'bowling_team': bowling_team,
                'over': over_num,
                'ball': ball_in_over,
                'batsman': batsman,
                'non_striker': non_striker,
                'bowler': bowler,
                'is_super_over': 0,
                'wide_runs': 1 if np.random.random() < 0.05 else 0,
                'bye_runs': 1 if np.random.random() < 0.02 else 0,
                'legbye_runs': 1 if np.random.random() < 0.03 else 0,
                'noball_runs': 1 if np.random.random() < 0.03 else 0,
                'penalty_runs': 0,
                'batsman_runs': batsman_runs,
                'extra_runs': 1 if np.random.random() < 0.08 else 0,
                'total_runs': total_runs + (1 if np.random.random() < 0.08 else 0),
                'player_dismissed': batsman if is_wicket else None,
                'dismissal_kind': np.random.choice(['caught', 'bowled', 'lbw', 'run out']) if is_wicket else None,
                'fielder': np.random.choice(players) if is_wicket and np.random.random() < 0.7 else None
            })
    
    matches_df = pd.DataFrame(matches_data)
    deliveries_df = pd.DataFrame(deliveries_data)
    
    # Convert date column
    matches_df['date'] = pd.to_datetime(matches_df['date'])
    
    return matches_df, deliveries_df, teams

class IPLAnalytics:
    def __init__(self, matches_df, deliveries_df, teams_dict):
        self.matches_df = matches_df
        self.deliveries_df = deliveries_df
        self.teams_dict = teams_dict
        
    def get_team_performance(self):
        """Team Performance Analysis"""
        team_stats = []
        
        for team_code, team_name in self.teams_dict.items():
            # All matches for this team
            team_matches = self.matches_df[
                (self.matches_df['team1'] == team_code) | 
                (self.matches_df['team2'] == team_code)
            ]
            
            if len(team_matches) == 0:
                continue
                
            wins = len(team_matches[team_matches['winner'] == team_code])
            losses = len(team_matches) - wins
            win_percentage = (wins / len(team_matches)) * 100
            
            # Points calculation (2 points per win)
            points = wins * 2
            
            team_stats.append({
                'Team': team_name,
                'Code': team_code,
                'Matches': len(team_matches),
                'Wins': wins,
                'Losses': losses,
                'Win %': round(win_percentage, 1),
                'Points': points
            })
        
        return pd.DataFrame(team_stats).sort_values('Points', ascending=False)
    
    def get_player_statistics(self):
        """Player Statistics & Rankings"""
        if len(self.deliveries_df) == 0:
            return pd.DataFrame()
            
        # Batting statistics
        batting_stats = self.deliveries_df.groupby('batsman').agg({
            'batsman_runs': ['sum', 'count'],
            'match_id': 'nunique',
            'total_runs': 'count'
        }).round(2)
        
        batting_stats.columns = ['total_runs', 'balls_faced', 'matches', 'innings']
        batting_stats = batting_stats.reset_index()
        
        # Calculate advanced metrics - FIXED
        batting_stats['strike_rate'] = np.where(
            batting_stats['balls_faced'] > 0,
            ((batting_stats['total_runs'] / batting_stats['balls_faced']) * 100).round(2),
            0
        )
        
        batting_stats['average'] = np.where(
            batting_stats['matches'] > 0,
            (batting_stats['total_runs'] / batting_stats['matches']).round(2),
            0
        )
        
        # Filter minimum qualification
        batting_stats = batting_stats[batting_stats['total_runs'] >= 50]
        
        return batting_stats.sort_values('total_runs', ascending=False).head(20)
    
    def get_head_to_head(self, team1, team2):
        """Head-to-Head Comparison"""
        h2h_matches = self.matches_df[
            ((self.matches_df['team1'] == team1) & (self.matches_df['team2'] == team2)) |
            ((self.matches_df['team1'] == team2) & (self.matches_df['team2'] == team1))
        ]
        
        if len(h2h_matches) == 0:
            return None
            
        team1_wins = len(h2h_matches[h2h_matches['winner'] == team1])
        team2_wins = len(h2h_matches[h2h_matches['winner'] == team2])
        
        return {
            'total_matches': len(h2h_matches),
            'team1_wins': team1_wins,
            'team2_wins': team2_wins,
            'team1_win_rate': (team1_wins / len(h2h_matches)) * 100,
            'team2_win_rate': (team2_wins / len(h2h_matches)) * 100
        }
    
    def predict_match_winner(self, team1, team2):
        """Win Prediction & Trend Analysis"""
        # Get recent form (last 10 matches for each team)
        team1_recent = self.matches_df[
            (self.matches_df['team1'] == team1) | (self.matches_df['team2'] == team1)
        ].tail(10)
        
        team2_recent = self.matches_df[
            (self.matches_df['team1'] == team2) | (self.matches_df['team2'] == team2)
        ].tail(10)
        
        team1_recent_wins = len(team1_recent[team1_recent['winner'] == team1])
        team2_recent_wins = len(team2_recent[team2_recent['winner'] == team2])
        
        # Head to head record
        h2h = self.get_head_to_head(team1, team2)
        
        # Simple prediction algorithm
        team1_score = team1_recent_wins * 0.4
        team2_score = team2_recent_wins * 0.4
        
        if h2h:
            team1_score += (h2h['team1_win_rate'] / 100) * 0.6
            team2_score += (h2h['team2_win_rate'] / 100) * 0.6
        
        if team1_score > team2_score:
            predicted_winner = team1
            confidence = min(((team1_score / (team1_score + team2_score)) * 100), 85)
        else:
            predicted_winner = team2
            confidence = min(((team2_score / (team1_score + team2_score)) * 100), 85)
            
        return {
            'predicted_winner': predicted_winner,
            'confidence': round(confidence, 1),
            'team1_recent_form': f"{team1_recent_wins}/10",
            'team2_recent_form': f"{team2_recent_wins}/10"
        }
    
    def get_venue_analysis(self):
        """Venue & Toss Impact Study"""
        venue_stats = self.matches_df.groupby('venue').agg({
            'id': 'count',
            'win_by_runs': 'mean',
            'win_by_wickets': 'mean'
        }).round(1)
        
        venue_stats.columns = ['matches_played', 'avg_run_margin', 'avg_wicket_margin']
        venue_stats = venue_stats.reset_index()
        
        # Toss impact
        toss_impact = self.matches_df.groupby('toss_decision').agg({
            'id': 'count'
        })
        
        toss_win_impact = len(self.matches_df[
            self.matches_df['toss_winner'] == self.matches_df['winner']
        ]) / len(self.matches_df) * 100
        
        return venue_stats, round(toss_win_impact, 1)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏏 IPL Analytics Dashboard</h1>
        <p>Complete Cricket Data Analysis with Interactive Visualizations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    with st.spinner('Loading IPL data...'):
        matches_df, deliveries_df, teams_dict = load_data()
        analytics = IPLAnalytics(matches_df, deliveries_df, teams_dict)
    
    # Sidebar navigation
    st.sidebar.markdown("## 🎯 Navigation Menu")
    
    analysis_options = [
        "📊 Overview Dashboard",
        "🏏 Match & Team Performance", 
        "👑 Player Statistics & Rankings",
        "⚔️ Head-to-Head Comparisons",
        "🔮 Win Prediction & Trends",
        "🏟️ Venue & Toss Impact Study"
    ]
    
    selected_analysis = st.sidebar.selectbox("Choose Analysis Type:", analysis_options)
    
    # Main content based on selection
    if selected_analysis == "📊 Overview Dashboard":
        show_overview_dashboard(matches_df, deliveries_df, analytics)
    
    elif selected_analysis == "🏏 Match & Team Performance":
        show_team_performance(analytics, teams_dict)
    
    elif selected_analysis == "👑 Player Statistics & Rankings":
        show_player_statistics(analytics)
    
    elif selected_analysis == "⚔️ Head-to-Head Comparisons":
        show_head_to_head(analytics, teams_dict)
    
    elif selected_analysis == "🔮 Win Prediction & Trends":
        show_win_prediction(analytics, teams_dict)
    
    elif selected_analysis == "🏟️ Venue & Toss Impact Study":
        show_venue_analysis(analytics)

def show_overview_dashboard(matches_df, deliveries_df, analytics):
    """Overview Dashboard with Key Metrics"""
    st.header("📊 IPL Overview Dashboard")
    
    # Key metrics in cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{len(matches_df):,}</h2>
            <p>Total Matches</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{matches_df['season'].nunique()}</h2>
            <p>Seasons</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_runs = deliveries_df['total_runs'].sum() if len(deliveries_df) > 0 else 0
        st.markdown(f"""
        <div class="metric-card">
            <h2>{total_runs:,}</h2>
            <p>Total Runs</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total_players = deliveries_df['batsman'].nunique() if len(deliveries_df) > 0 else 0
        st.markdown(f"""
        <div class="metric-card">
            <h2>{total_players}</h2>
            <p>Players</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Championship Winners")
        season_winners = matches_df.groupby('season')['winner'].agg(lambda x: x.value_counts().index[0]).reset_index()
        
        fig = px.bar(
            season_winners,
            x='season',
            y=[1] * len(season_winners),  # Just for display
            color='winner',
            title="Season Champions",
            text='winner'
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_traces(textposition='inside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Matches Per Season")
        season_matches = matches_df.groupby('season').size().reset_index()
        season_matches.columns = ['Season', 'Matches']
        
        fig = px.line(
            season_matches,
            x='Season',
            y='Matches',
            title="Tournament Growth",
            markers=True,
            line_shape='spline'
        )
        fig.update_traces(line_color='#FF6B35', marker_color='#FF6B35', marker_size=8)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Team performance summary
    st.subheader("🏏 Team Performance Summary")
    team_performance = analytics.get_team_performance()
    
    if len(team_performance) > 0:
        fig = px.bar(
            team_performance.head(10),
            x='Win %',
            y='Team',
            orientation='h',
            color='Win %',
            color_continuous_scale='RdYlGn',
            text='Win %',
            title="Team Win Percentage"
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='inside')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Team performance data will be displayed here")

def show_team_performance(analytics, teams_dict):
    """Match & Team Performance Analysis"""
    st.header("🏏 Match & Team Performance Analysis")
    
    # Get team performance data
    team_performance = analytics.get_team_performance()
    
    if len(team_performance) == 0:
        st.warning("No team performance data available")
        return
    
    # Team selector for detailed analysis
    col1, col2 = st.columns(2)
    
    with col1:
        selected_team = st.selectbox(
            "Select Team for Detailed Analysis:",
            options=list(teams_dict.keys()),
            format_func=lambda x: f"{x} - {teams_dict[x]}"
        )
    
    # Show selected team stats
    if selected_team:
        team_data = team_performance[team_performance['Code'] == selected_team]
        
        if len(team_data) > 0:
            team_data = team_data.iloc[0]
            
            st.subheader(f"📊 {teams_dict[selected_team]} Performance")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Matches", team_data['Matches'])
            with col2:
                st.metric("Wins", team_data['Wins'])
            with col3:
                st.metric("Win Rate", f"{team_data['Win %']}%")
            with col4:
                st.metric("Points", team_data['Points'])
    
    # Performance comparison chart
    st.subheader("📊 Team Performance Comparison")
    
    fig = go.Figure()
    
    # Add wins bars
    fig.add_trace(go.Bar(
        name='Wins',
        x=team_performance['Team'],
        y=team_performance['Wins'],
        marker_color='#4ECDC4'
    ))
    
    # Add losses bars
    fig.add_trace(go.Bar(
        name='Losses',
        x=team_performance['Team'],
        y=team_performance['Losses'],
        marker_color='#FF6B6B'
    ))
    
    fig.update_layout(
        title="Wins vs Losses Comparison",
        barmode='stack',
        height=500,
        xaxis_title="Teams",
        yaxis_title="Number of Matches"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed table
    st.subheader("📋 Complete Team Statistics")
    st.dataframe(team_performance, use_container_width=True)

def show_player_statistics(analytics):
    """Player Statistics & Rankings"""
    st.header("👑 Player Statistics & Rankings")
    
    # Get player statistics
    player_stats = analytics.get_player_statistics()
    
    if len(player_stats) > 0:
        # Top performers section
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏆 Top Run Scorers")
            top_scorers = player_stats.head(10)
            
            fig = px.bar(
                top_scorers,
                x='total_runs',
                y='batsman',
                orientation='h',
                color='strike_rate',
                color_continuous_scale='viridis',
                text='total_runs',
                title="Top 10 Batsmen by Runs"
            )
            fig.update_traces(textposition='inside')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("⚡ Strike Rate Leaders")
            sr_leaders = player_stats[player_stats['total_runs'] >= 100].nlargest(10, 'strike_rate')
            
            if len(sr_leaders) > 0:
                fig = px.scatter(
                    sr_leaders,
                    x='total_runs',
                    y='strike_rate',
                    size='matches',
                    color='average',
                    hover_name='batsman',
                    title="Strike Rate vs Total Runs",
                    color_continuous_scale='plasma'
                )
                fig.update_layout(height=500)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Strike rate data will be displayed here")
        
        # Complete statistics table
        st.subheader("📊 Complete Player Statistics")
        st.dataframe(player_stats, use_container_width=True)
    else:
        st.info("Player statistics will be displayed when more data is available")

def show_head_to_head(analytics, teams_dict):
    """Head-to-Head Comparisons"""
    st.header("⚔️ Head-to-Head Team Comparisons")
    
    # Team selectors
    col1, col2 = st.columns(2)
    
    with col1:
        team1 = st.selectbox(
            "Select First Team:",
            options=list(teams_dict.keys()),
            format_func=lambda x: f"{x} - {teams_dict[x]}",
            key="h2h_team1"
        )
    
    with col2:
        team2 = st.selectbox(
            "Select Second Team:",
            options=[t for t in teams_dict.keys() if t != team1],
            format_func=lambda x: f"{x} - {teams_dict[x]}",
            key="h2h_team2"
        )
    
    if team1 and team2:
        # VS divider
        st.markdown(f'<div class="vs-divider">{teams_dict[team1]} VS {teams_dict[team2]}</div>', 
                   unsafe_allow_html=True)
        
        # Get head-to-head data
        h2h_data = analytics.get_head_to_head(team1, team2)
        
        if h2h_data:
            # Head-to-head metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Matches", h2h_data['total_matches'])
            
            with col2:
                st.metric(f"{teams_dict[team1]} Wins", h2h_data['team1_wins'])
            
            with col3:
                st.metric(f"{teams_dict[team2]} Wins", h2h_data['team2_wins'])
            
            # Visual comparison
            col1, col2 = st.columns(2)
            
            with col1:
                # Win percentage pie chart
                fig = go.Figure(data=[go.Pie(
                    labels=[teams_dict[team1], teams_dict[team2]],
                    values=[h2h_data['team1_wins'], h2h_data['team2_wins']],
                    hole=0.4,
                    marker_colors=['#FF6B35', '#4ECDC4']
                )])
                
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(
                    title="Head-to-Head Win Distribution",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Win rate comparison
                fig = go.Figure(data=[
                    go.Bar(
                        name=teams_dict[team1],
                        x=['Win Rate'],
                        y=[h2h_data['team1_win_rate']],
                        marker_color='#FF6B35'
                    ),
                    go.Bar(
                        name=teams_dict[team2],
                        x=['Win Rate'],
                        y=[h2h_data['team2_win_rate']],
                        marker_color='#4ECDC4'
                    )
                ])
                
                fig.update_layout(
                    title="Win Rate Comparison (%)",
                    barmode='group',
                    height=400,
                    yaxis=dict(range=[0, 100])
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No head-to-head matches found between these teams.")

def show_win_prediction(analytics, teams_dict):
    """Win Prediction & Trend Analysis"""
    st.header("🔮 Match Win Prediction & Trend Analysis")
    
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 AI-Powered Match Prediction</h3>
        <p>Our advanced algorithm analyzes team performance, recent form, head-to-head records, and historical trends to predict match outcomes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team selectors for prediction
    col1, col2 = st.columns(2)
    
    with col1:
        pred_team1 = st.selectbox(
            "Team 1:",
            options=list(teams_dict.keys()),
            format_func=lambda x: f"{x} - {teams_dict[x]}",
            key="pred_team1"
        )
    
    with col2:
        pred_team2 = st.selectbox(
            "Team 2:",
            options=[t for t in teams_dict.keys() if t != pred_team1],
            format_func=lambda x: f"{x} - {teams_dict[x]}",
            key="pred_team2"
        )
    
    # Prediction button
    if st.button("🎯 Predict Match Winner", type="primary"):
        with st.spinner("Analyzing team data and generating prediction..."):
            prediction = analytics.predict_match_winner(pred_team1, pred_team2)
            
            # Show prediction result
            winner_team = teams_dict[prediction['predicted_winner']]
            
            st.markdown(f"""
            <div class="prediction-result">
                <h2>🏆 Predicted Winner</h2>
                <h1>{winner_team}</h1>
                <h3>Confidence: {prediction['confidence']}%</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed analysis
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 Analysis Factors")
                st.write(f"**{teams_dict[pred_team1]} Recent Form**: {prediction['team1_recent_form']}")
                st.write(f"**{teams_dict[pred_team2]} Recent Form**: {prediction['team2_recent_form']}")
                
                # Confidence meter
                st.subheader("🎯 Confidence Level")
                st.progress(prediction['confidence'] / 100)
                st.write(f"Prediction Confidence: **{prediction['confidence']}%**")
            
            with col2:
                # Win probability visualization
                st.subheader("📈 Win Probabilities")
                
                team1_prob = prediction['confidence'] if prediction['predicted_winner'] == pred_team1 else 100 - prediction['confidence']
                team2_prob = 100 - team1_prob
                
                prob_data = pd.DataFrame({
                    'Team': [teams_dict[pred_team1], teams_dict[pred_team2]],
                    'Win Probability': [team1_prob, team2_prob]
                })
                
                fig = px.bar(
                    prob_data,
                    x='Team',
                    y='Win Probability',
                    color='Win Probability',
                    color_continuous_scale='RdYlGn',
                    text='Win Probability',
                    title="Match Win Probabilities"
                )
                
                fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
                fig.update_layout(height=400, yaxis=dict(range=[0, 100]))
                st.plotly_chart(fig, use_container_width=True)

def show_venue_analysis(analytics):
    """Venue & Toss Impact Study"""
    st.header("🏟️ Venue & Toss Impact Analysis")
    
    # Get venue analysis data
    venue_stats, toss_impact = analytics.get_venue_analysis()
    
    # Toss impact overview
    st.subheader("🪙 Toss Impact Study")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Toss Win = Match Win", f"{toss_impact}%")
    
    with col2:
        toss_decisions = analytics.matches_df['toss_decision'].value_counts()
        bat_percentage = (toss_decisions.get('bat', 0) / len(analytics.matches_df) * 100)
        st.metric("Teams Prefer Batting", f"{bat_percentage:.1f}%")
    
    with col3:
        field_percentage = (toss_decisions.get('field', 0) / len(analytics.matches_df) * 100)
        st.metric("Teams Prefer Bowling", f"{field_percentage:.1f}%")
    
    # Venue analysis
    st.subheader("🏟️ Stadium Performance Analysis")
    
    if len(venue_stats) > 0:
        # Top venues by matches
        top_venues = venue_stats.nlargest(10, 'matches_played')
        
        fig = px.bar(
            top_venues,
            x='matches_played',
            y='venue',
            orientation='h',
            title="Most Used Venues",
            color='matches_played',
            color_continuous_scale='blues',
            text='matches_played'
        )
        
        fig.update_traces(textposition='inside')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # Venue statistics table
        st.subheader("📋 Complete Venue Statistics")
        st.dataframe(venue_stats.sort_values('matches_played', ascending=False), use_container_width=True)
    else:
        st.info("Venue analysis data will be displayed here")

# Footer
def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <h4>🏏 IPL Analytics Dashboard</h4>
        <p>Complete Cricket Data Analysis Solution</p>
        <p>Built with ❤️ using Streamlit & Python | Data Science Project</p>
        <p><strong>Features:</strong> Team Performance • Player Statistics • Win Prediction • Venue Analysis</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_footer()
