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

