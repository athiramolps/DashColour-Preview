import streamlit as st

# Set page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Custom CSS for layout and styles ---
custom_css = """
<style>
    .color-box input[type='color'] {
        width: 100%;
        padding: 0.4em;
        border: none;
        height: 2.5em;
    }
    .dashboard-preview {
        background-color: var(--bg-color);
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
        background-color: var(--card-bg);
        padding: 1em;
        border-radius: 8px;
        width: 32%;
        text-align: center;
        color: var(--kpi-text);
        font-size: 1.2em;
        font-weight: 600;
    }
    .chart {
        display: inline-block;
        width: 30%;
        height: 150px;
        border-radius: 8px;
        background-color: var(--chart-color);
        margin-right: 2%;
    }
    .generate-btn {
        background-color: var(--btn-color);
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
        color: var(--footer-text);
        background-color: var(--footer-bg);
        padding: 1em;
        border-radius: 6px;
    }
    .title-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# --- Title and toggle ---
st.markdown("<div class='title-bar'>", unsafe_allow_html=True)
st.markdown("<h1 style='color:#7B1FA2;'>📊 DashColor Preview</h1>", unsafe_allow_html=True)
st.toggle("🌙 Dark Mode", key="dark_mode")
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<p style='margin-top:-10px;'>Dashboard preview styled with the selected colors.</p>", unsafe_allow_html=True)

# --- Color Inputs ---
st.sidebar.header("🎛️ Color Input Fields")
background = st.sidebar.color_picker("Background", "#F3F4F6")
sidebar = st.sidebar.color_picker("Sidebar Background", "#E5E7EB")
sidebar_icons = st.sidebar.color_picker("Sidebar Icons", "#6B7280")
sidebar_text = st.sidebar.color_picker("Sidebar Text", "#4B5563")
header_bg = st.sidebar.color_picker("Header Background", "#FFFFFF")
header_text = st.sidebar.color_picker("Header Text", "#111827")
logo = st.sidebar.color_picker("Logo", "#8B5CF6")
title = st.sidebar.color_picker("Title", "#681C87")
subtitles = st.sidebar.color_picker("Subtitles", "#6B2146")
text = st.sidebar.color_picker("Text", "#3F3F46")
kpi = st.sidebar.color_picker("KPI Cards Background", "#A355F7")
kpi_text = st.sidebar.color_picker("KPI Text", "#FFFFFF")
button = st.sidebar.color_picker("Primary Button", "#7C3AED")
hover_button = st.sidebar.color_picker("Hover Button", "#5B21B6")
chart = st.sidebar.color_picker("Charts Background", "#9383EA")
table_bg = st.sidebar.color_picker("Table Background", "#F9FAFB")
table_text = st.sidebar.color_picker("Table Text", "#111827")
alert = st.sidebar.color_picker("Alert Color", "#EF4444")
footer_bg = st.sidebar.color_picker("Footer Background", "#F3F4F6")
footer_text = st.sidebar.color_picker("Footer Text", "#6B7280")

# --- Inject dynamic CSS variables ---
theme_css = f"""
<style>
:root {{
    --bg-color: {background};
    --card-bg: {kpi};
    --kpi-text: {kpi_text};
    --text-color: {text};
    --chart-color: {chart};
    --btn-color: {button};
    --footer-bg: {footer_bg};
    --footer-text: {footer_text};
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
st.markdown("""
<div class='footer'>
    © All rights reserved by Athiramol PS<br>
    Published on: June 2025<br>
    This project, “DashColor Preview: A Visual Tool for Dashboard Color Planning,” is an original creation by Athiramol PS.
</div>
""", unsafe_allow_html=True)
