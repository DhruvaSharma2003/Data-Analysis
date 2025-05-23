# app.py

import streamlit as st
import plotly.express as px

# Load modular functions
from data_loader import load_excel_data
from utils.trends import get_monthly_stream_totals
from utils.languages import get_top_language_trends
from utils.groups import get_top_groups_trend
from utils.tracks import get_top_tracks, get_genre_trends
from utils.strategy import generate_subscription_suggestions

# Streamlit page config
st.set_page_config(
    page_title="Devotional Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Excel data
data = load_excel_data()

# Create tabs
tabs = st.tabs(["📈 Monthly Trends", "🎵 Top Groups", "🗣️ Language Insights", "🎧 Top Tracks", "💡 Strategy", "Debug"])

# ------------------ TAB 0: Monthly Trends ------------------
with tabs[0]:
    st.subheader("Overall Streaming Trend")
    st.markdown("Visualize total devotional streaming growth across months.")

    monthly_df = get_monthly_stream_totals(data["Streams"])

    fig = px.line(monthly_df, x="Month", y="Total Streams", markers=True,
                  title="Monthly Devotional Streaming Totals")
    st.plotly_chart(fig, use_container_width=True)
    
# ------------------ TAB 1: Top Devotional groups ------------------
with tabs[1]:
    st.subheader("Top Devotional Groups Over Time")
    st.markdown("Select the number of top-performing groups to visualize their monthly streaming trends.")

    # User input for number of groups
    top_n = st.slider("Select Top N Groups", min_value=3, max_value=10, value=5)

    # Load and plot
    top_groups_df = get_top_groups_trend(data["Streams"], top_n=top_n)

    fig = px.line(top_groups_df, x="Month", y="Streams", color="GROUP_NAME", markers=True,
                  title=f"Top {top_n} Devotional Groups - Monthly Streaming Trend")
    st.plotly_chart(fig, use_container_width=True)
    
# ------------------ TAB 2: Language wise stream trend ------------------
with tabs[2]:
    st.subheader("Language-Wise Streaming Trends")
    st.markdown("Identify which languages are most preferred by users across months.")

    top_n_lang = st.slider("Select Top N Languages", min_value=3, max_value=10, value=5)

    lang_df = data["LanguageWise"]
    lang_trends = get_top_language_trends(lang_df, top_n=top_n_lang)

    fig = px.line(lang_trends, x="Month", y="Streams", color="Language", markers=True,
                  title=f"Top {top_n_lang} Languages - Monthly Streaming Trend")
    st.plotly_chart(fig, use_container_width=True)

# ------------------ TAB 3: Top tracks and genre trend ------------------
with tabs[3]:
    st.subheader("Top Tracks & Genre Trends")
    st.markdown("Explore the most played devotional tracks and genre-level popularity.")

    pdl_df = data["PDL"]

    # Display top tracks
    st.markdown("### 🎧 Top Tracks by Playcount")
    top_n = st.slider("Select Number of Top Tracks", 5, 20, 10)
    top_tracks_df = get_top_tracks(pdl_df, top_n=top_n)
    st.dataframe(top_tracks_df[["Title", "Album", "Language", "Genre", "Playcount"]])

    # Display genre-wise playcount
    st.markdown("### 🎼 Genre Popularity")
    genre_df = get_genre_trends(pdl_df)
    fig = px.bar(genre_df, x="Genre", y="Playcount", title="Playcount by Genre", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# ------------------ TAB 4: Final Strategy ------------------
with tabs[4]:
    st.subheader("Smart Subscription Strategy")
    st.markdown("Use these data-backed ideas to build custom devotional subscription offerings.")

    # Generate suggestions
    strategy_points = generate_subscription_suggestions(
        monthly_df,
        top_groups_df,
        lang_trends
    )

    for point in strategy_points:
        st.markdown(f"- {point}")

with tabs[5]:
    st.write("Streams Columns:", data["Streams"].columns.tolist())
    st.write("LanguageWise Columns:", data["LanguageWise"].columns.tolist())


    


