import streamlit as st

# Set page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Session state to handle theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Custom CSS for layout and styles ---
custom_css = """
<style>
    body { font-family: 'Segoe UI', sans-serif; }
    .color-box input[type='color'] {
        width: 100%;
        padding: 0.4em;
        border: none;
        height: 2.5em;
    }
    .dashboard-preview {
        background-color: VAR(--bg-color);
        padding: 2em;
        border-radius: 12px;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }
    .kpi {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1.5em;
    }
    .kpi-card {
        background-color: VAR(--card-bg);
        padding: 1em;
        border-radius: 8px;
        width: 32%;
        text-align: center;
        color: VAR(--text-color);
        font-size: 1.2em;
        font-weight: 600;
    }
    .chart {
        display: inline-block;
        width: 30%;
        height: 150px;
        border-radius: 8px;
        background-color: VAR(--chart-color);
        margin-right: 2%;
    }
    .generate-btn {
        background-color: VAR(--btn-color);
        color: white;
        padding: 0.7em 1.5em;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        cursor: pointer;
    }
    .footer {
        text-align: center;
        margin-top: 3em;
        font-size: 0.9em;
        color: gray;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# --- Title and toggle ---
col1, col2 = st.columns([8, 1])
with col1:
    st.markdown("<h1 style='color:#7B1FA2;'>🎨 DashColor Preview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:-10px;'>Dashboard preview styled with the selected colors.</p>", unsafe_allow_html=True)
with col2:
    st.toggle("🌙 Dark Mode", key="dark_mode")

# --- Color Inputs ---
st.sidebar.header("🎛️ Color Input Fields")
background = st.sidebar.color_picker("Background", "#F3F4F6")
sidebar = st.sidebar.color_picker("Side bar", "#E5E7EB")
sidebar_icons = st.sidebar.color_picker("Icons in the side bar", "#6B7280")
logo = st.sidebar.color_picker("Logo", "#8B5CF6")
title = st.sidebar.color_picker("Title", "#681C87")
subtitles = st.sidebar.color_picker("Subtitles", "#6B2146")
text = st.sidebar.color_picker("Text", "#3F3F46")
kpi = st.sidebar.color_picker("KPI Cards", "#A355F7")
button = st.sidebar.color_picker("Buttons", "#7C3AED")
chart = st.sidebar.color_picker("Charts", "#9383EA")

# --- Inject dynamic CSS variables ---
theme_css = f"""
<style>
:root {{
    --bg-color: {background};
    --card-bg: {kpi};
    --text-color: {text};
    --chart-color: {chart};
    --btn-color: {button};
}}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# --- Dashboard Preview ---
st.markdown("<div class='dashboard-preview'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:{title}; margin-bottom:0;'>Dashboard</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{subtitles}; margin-top:0;'>One-line explanation</p>", unsafe_allow_html=True)

# KPI Cards
st.markdown("<div class='kpi'>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>$12,345<br><span style='font-size:0.8em;'>Label</span></div>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>45.6 %<br><span style='font-size:0.8em;'>Label</span></div>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>1,234<br><span style='font-size:0.8em;'>Label</span></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Charts
st.markdown("<div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Button
st.markdown("<br><button class='generate-btn'>Generate</button>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© All rights reserved by AthiramolPS, Published on June 2025</div>", unsafe_allow_html=True)
