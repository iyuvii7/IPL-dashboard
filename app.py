import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IPL Dashboard (2007/08 - 2024)", layout="wide")
st.markdown("<h1 style='text-align: center;'>🏏 IPL Data Dashboard (2007/08 - 2024)</h1>", unsafe_allow_html=True)
# Load all CSV files
team_win_stats = pd.read_csv("data/team_win_stats.csv")
win_per_season = pd.read_csv("data/win_per_season.csv")
toss_vs_match = pd.read_csv("data/toss_vs_match_wins.csv")
top_batsman = pd.read_csv("data/top_batsmen.csv")
strike_rate = pd.read_csv("data/strike_rate.csv")
top_bowler = pd.read_csv("data/top_bowler.csv")
top_batsman_season = pd.read_csv("data/top_batsman_per_season.csv")
batting_vs_chasing = pd.read_csv("data/batting_vs_chasing_win_percent.csv")
team_runs_season = pd.read_csv("data/team_season_runs.csv")
finals_winners = pd.read_csv("data/finals_winners.csv")

# Tabs
tab1, tab2, tab3 = st.tabs(["🏏 Team Performance", "🔥 Player Performance", "📊 Match Insights"])

# -------------------- TEAM PERFORMANCE ---------------------
with tab1:
    st.header("🏆 Team Win Percentage")
    fig = px.bar(team_win_stats.sort_values("win_percent", ascending=False),
                 x='team', y='win_percent', color='win_percent', text='win_percent')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Team Wins Per Season")
    fig = px.line(win_per_season, x='season', y='wins', color='winner', markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🪙 Toss Win = Match Win?")
    fig = px.pie(toss_vs_match, names='toss_match_result', values='Win percent', title="Toss Win vs Match Win")
    st.plotly_chart(fig, use_container_width=True)

# -------------------- PLAYER PERFORMANCE ---------------------
with tab2:
    st.header("🏏 Top 10 Run Scorers")
    fig = px.bar(top_batsman.head(10), x='batter', y='batsman_runs', color='batsman_runs')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("⚡ Top 10 Strike Rates (500+ Runs)")
    fig = px.bar(strike_rate.head(10), x='batter', y='0', color='0')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔥 Top 10 Wicket Takers")
    fig = px.bar(top_bowler.head(10), x='bowler', y='count', color='count')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🎯 Top Batsmen Per Season")
    fig = px.bar(top_batsman_season, x='season', y='batsman_runs', color='batter', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

# -------------------- MATCH INSIGHTS ---------------------
with tab3:
    st.header("🏁 Batting First vs Chasing Win %")
    fig = px.pie(batting_vs_chasing, names='type', values='win_percent')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🚀 Total Runs by Teams Per Season")
    fig = px.bar(team_runs_season, x='season', y='total_runs', color='batting_team', barmode='stack')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🏆 IPL Final Winners by Season")
    st.dataframe(finals_winners, use_container_width=True)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size:16px;'>© 2025 | Created by <strong>Yuvraj Singh</strong></p>", unsafe_allow_html=True)
