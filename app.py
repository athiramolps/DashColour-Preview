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
    .dashboard-preview {
        background-color: var(--bg-color);
        padding: 2em;
        border-radius: 12px;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }
    /* Sidebar Area */
    .sidebar-layout {
        background-color: var(--sidebar-layout);
        color: var(--sidebar-texts);
        padding: 1em;
        border-radius: 8px;
        margin-bottom: 1em;
    }
    .sidebar-icons {
        color: var(--sidebar-icons);
    }
    /* Header Area */
    .header-card {
        background-color: var(--header-card);
        padding: 1em;
        border-radius: 8px;
        margin-bottom: 1em;
        color: var(--header-title);
    }
    .header-title {
        color: var(--header-title);
        font-size: 1.8em;
        font-weight: 700;
        margin: 0;
    }
    .header-subtitle {
        color: var(--header-subtitle);
        font-size: 1em;
        margin: 0 0 1em 0;
    }
    .header-buttons button {
        background-color: var(--header-buttons);
        border: none;
        border-radius: 6px;
        color: white;
        padding: 0.5em 1em;
        font-weight: 600;
        cursor: pointer;
        margin-right: 0.5em;
    }
    /* KPI Area */
    .kpi {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1.5em;
    }
    .kpi-card {
        background-color: var(--kpi-card);
        padding: 1em;
        border-radius: 8px;
        width: 32%;
        text-align: center;
        color: var(--kpi-text);
        font-size: 1.2em;
        font-weight: 600;
        position: relative;
    }
    .kpi-icons {
        position: absolute;
        top: 10px;
        right: 10px;
        color: var(--kpi-icons);
        font-size: 1.5em;
    }
    /* Chart Area */
    .charts {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1.5em;
    }
    .chart-card {
        background-color: var(--chart-card);
        width: 30%;
        border-radius: 8px;
        padding: 1em;
        color: var(--chart-title);
        box-sizing: border-box;
    }
    .chart-title {
        font-weight: 700;
        font-size: 1.1em;
        margin: 0 0 0.2em 0;
        color: var(--chart-title);
    }
    .chart-subtitle {
        font-size: 0.9em;
        color: var(--chart-subtitle);
        margin: 0 0 1em 0;
    }
    .chart-icons {
        color: var(--chart-icons);
        font-size: 1.2em;
        margin-bottom: 0.5em;
    }
    .chart-values {
        font-size: 1.4em;
        font-weight: 700;
        color: var(--chart-values);
    }
    /* Button Area */
    .button-primary {
        background-color: var(--button-primary);
        border: none;
        border-radius: 6px;
        color: white;
        padding: 0.7em 1.5em;
        font-weight: bold;
        cursor: pointer;
        margin-right: 1em;
    }
    .button-secondary {
        background-color: var(--button-secondary);
        border: none;
        border-radius: 6px;
        color: white;
        padding: 0.7em 1.5em;
        font-weight: bold;
        cursor: pointer;
    }
    /* Tooltip */
    .tooltip-card {
        background-color: var(--tooltip-card-bg);
        padding: 1em;
        border-radius: 8px;
        color: var(--tooltip-text);
        width: max-content;
        margin-top: 2em;
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

# --- New Color Inputs ---
st.sidebar.header("🎛️ Color Input Fields")

# Background Area
background = st.sidebar.color_picker("Background", "#F3F4F6")

# Sidebar Area
sidebar_layout = st.sidebar.color_picker("Sidebar Layout", "#E5E7EB")
sidebar_icons = st.sidebar.color_picker("Sidebar Icons", "#6B7280")
sidebar_texts = st.sidebar.color_picker("Sidebar Texts", "#374151")

# Header Area
header_card = st.sidebar.color_picker("Header Card", "#D1C4E9")
header_title = st.sidebar.color_picker("Header Title", "#4A148C")
header_subtitle = st.sidebar.color_picker("Header Subtitle", "#7B1FA2")
header_buttons = st.sidebar.color_picker("Header Buttons", "#8E24AA")

# KPI Area
kpi_card = st.sidebar.color_picker("KPI Card", "#A355F7")
kpi_text = st.sidebar.color_picker("KPI Text", "#3F3F46")
kpi_icons = st.sidebar.color_picker("KPI Icons", "#7E57C2")

# Chart Area
chart_card = st.sidebar.color_picker("Chart Card", "#9383EA")
chart_title = st.sidebar.color_picker("Chart Title", "#5E35B1")
chart_subtitle = st.sidebar.color_picker("Chart Subtitle", "#9575CD")
chart_icons = st.sidebar.color_picker("Chart Icons", "#512DA8")
chart_values = st.sidebar.color_picker("Chart Values", "#311B92")

# Button Area
button_primary = st.sidebar.color_picker("Button Primary", "#7C3AED")
button_secondary = st.sidebar.color_picker("Button Secondary", "#9575CD")

# Tooltip
tooltip_card_bg = st.sidebar.color_picker("Tooltip Card Background", "#EDE7F6")
tooltip_text = st.sidebar.color_picker("Tooltip Text", "#4A148C")

# --- Inject dynamic CSS variables ---
theme_css = f"""
<style>
:root {{
    --bg-color: {background};
    --sidebar-layout: {sidebar_layout};
    --sidebar-icons: {sidebar_icons};
    --sidebar-texts: {sidebar_texts};
    --header-card: {header_card};
    --header-title: {header_title};
    --header-subtitle: {header_subtitle};
    --header-buttons: {header_buttons};
    --kpi-card: {kpi_card};
    --kpi-text: {kpi_text};
    --kpi-icons: {kpi_icons};
    --chart-card: {chart_card};
    --chart-title: {chart_title};
    --chart-subtitle: {chart_subtitle};
    --chart-icons: {chart_icons};
    --chart-values: {chart_values};
    --button-primary: {button_primary};
    --button-secondary: {button_secondary};
    --tooltip-card-bg: {tooltip_card_bg};
    --tooltip-text: {tooltip_text};
}}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# --- Dashboard Preview ---
st.markdown("<div class='dashboard-preview'>", unsafe_allow_html=True)

# Sidebar preview (just a box with icons and text)
st.markdown(f"""
<div class="sidebar-layout">
    <div style="font-weight:700;">Sidebar</div>
    <div class="sidebar-icons" style="font-size:1.5em;">🔍 📁 ⚙️</div>
    <div style="color: var(--sidebar-texts); margin-top:0.5em;">Sidebar Texts</div>
</div>
""", unsafe_allow_html=True)

# Header preview
st.markdown(f"""
<div class="header-card">
    <h2 class="header-title">Dashboard Header</h2>
    <div class="header-subtitle">Subtitle of the dashboard</div>
    <div class="header-buttons">
        <button>Save</button><button>Export</button>
    </div>
</div>
""", unsafe_allow_html=True)

# KPI Cards
st.markdown("<div class='kpi'>", unsafe_allow_html=True)
st.markdown(f"""
<div class='kpi-card'>
    <div class='kpi-icons'>📈</div>
    $12,345<br><span style='font-size:0.8em;'>Revenue</span>
</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div class='kpi-card'>
    <div class='kpi-icons'>👥</div>
    45.6 %<br><span style='font-size:0.8em;'>Growth</span>
</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div class='kpi-card'>
    <div class='kpi-icons'>⚙️</div>
    1,234<br><span style='font-size:0.8em;'>Orders</span>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Charts Area
st.markdown("<div class='charts'>", unsafe_allow_html=True)
for i in range(3):
    st.markdown(f"""
    <div class='chart-card'>
        <div class='chart-title'>Chart Title {i+1}</div>
        <div class='chart-subtitle'>Chart Subtitle</div>
        <div class='chart-icons'>📊</div>
        <div class='chart-values'>75%</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Buttons
st.markdown(f"""
<button class="button-primary">Primary Action</button>
<button class="button-secondary">Secondary Action</button>
""", unsafe_allow_html=True)

# Tooltip preview
st.markdown(f"""
<div class="tooltip-card">Tooltip text styled with chosen colors.</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© All rights reserved by AthiramolPS, Published on June 2025</div>", unsafe_allow_html=True)
