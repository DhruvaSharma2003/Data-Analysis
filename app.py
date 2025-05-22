# app.py
import streamlit as st
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Devotional Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🕉️ Devotional Data Insights")
st.markdown("Analyze streaming behavior, language preferences, and top devotional content to design smart subscription packages.")

# Load Excel file once
@st.cache_data
def load_excel():
    file_path = "DEVOTIONAL DATA.xlsx"
    xl = pd.ExcelFile(file_path)
    return {
        "Repertoire": xl.parse("Repertoire"),
        "Streams": xl.parse("Streams"),
        "PDL": xl.parse("PDL- Tracks"),
        "LanguageWise": xl.parse("STREAM_LANGUAGE_WISE")
    }

data = load_excel()

# Create tabs
tabs = st.tabs(["📈 Monthly Trends", "🎵 Top Groups", "🗣️ Language Insights", "🎧 Top Tracks", "💡 Strategy"])

with tabs[0]:
    st.subheader("Overall Streaming Trend")
    st.markdown("Visualize total devotional streaming growth across months.")
    # Leave this blank for now or show a placeholder
    st.info("This section will display the monthly streaming trend line chart.")

with tabs[1]:
    st.subheader("Top Devotional Groups")
    st.markdown("View performance of leading devotional content groups.")
    st.info("Coming soon: Group-wise trend analytics.")

with tabs[2]:
    st.subheader("Language Preferences")
    st.markdown("Understand which languages drive the most engagement.")
    st.info("This section will help design regional packs.")

with tabs[3]:
    st.subheader("Track & Genre Performance")
    st.markdown("Explore which songs and genres are most loved.")
    st.info("To be populated with top playcounts and genre charts.")

with tabs[4]:
    st.subheader("Subscription Strategy Suggestions")
    st.markdown("Get data-driven ideas for regional, fan, or seasonal packs.")
    st.info("Will include rule-based suggestions based on analytics.")
