# app.py

import streamlit as st
import plotly.express as px

# Load modular functions
from data_loader import load_excel_data
from utils.trends import get_monthly_stream_totals

# Streamlit page config
st.set_page_config(
    page_title="Devotional Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Excel data
data = load_excel_data()

# Create tabs
tabs = st.tabs(["📈 Monthly Trends", "🎵 Top Groups", "🗣️ Language Insights", "🎧 Top Tracks", "💡 Strategy"])

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

    


