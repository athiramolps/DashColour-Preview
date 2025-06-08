import streamlit as st

# Set page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Session state to handle theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Custom CSS Layout & Button Styles ---
custom_css = """
<style>
    body { font-family: 'Segoe UI', sans-serif; }
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
        background-color: var(--kpi-card);
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
        background-color: var(--chart-card);
        margin-right: 2%;
    }
    .button-primary {
        background-color: var(--button-primary);
        color: var(--button-primary-text);
        border: none;
        border-radius: 6px;
        padding: 0.7em 1.5em;
        font-weight: bold;
        cursor: pointer;
        margin-right: 1em;
    }
    .button-secondary {
        background-color: var(--button-secondary);
        color: var(--button-secondary-text);
        border: none;
        border-radius: 6px;
        padding: 0.7em 1.5em;
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

# --- Title and Toggle ---
col1, col2 = st.columns([8, 1])
with col1:
    st.markdown("<h1 style='color:#7B1FA2;'>🎨 DashColor Preview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:-10px;'>Dashboard preview styled with the selected colors.</p>", unsafe_allow_html=True)
with col2:
    st.toggle("🌙 Dark Mode", key="dark_mode")

# --- Sidebar Color Inputs with Section Titles ---
st.sidebar.header("🎛️ UI Color Inputs")

# Background Area
st.sidebar.subheader("🌄 Background Area")
background = st.sidebar.color_picker("Background", "#F3F4F6")

# Sidebar Area
st.sidebar.subheader("📚 Sidebar Area")
sidebar_layout = st.sidebar.color_picker("Sidebar Layout", "#E5E7EB")
sidebar_icons = st.sidebar.color_picker("Sidebar Icons", "#6B7280")
sidebar_texts = st.sidebar.color_picker("Sidebar Texts", "#374151")

# Header Area
st.sidebar.subheader("🧾 Header Area")
header_card = st.sidebar.color_picker("Header Card", "#EDE7F6")
header_title = st.sidebar.color_picker("Header Title", "#681C87")
header_subtitle = st.sidebar.color_picker("Header Subtitle", "#6B2146")
header_buttons = st.sidebar.color_picker("Header Buttons", "#9575CD")

# KPI Area
st.sidebar.subheader("📊 KPI Area")
kpi_card = st.sidebar.color_picker("KPI Card", "#A355F7")
kpi_text = st.sidebar.color_picker("KPI Text", "#FFFFFF")
kpi_icons = st.sidebar.color_picker("KPI Icons", "#E0E0E0")

# Chart Area
st.sidebar.subheader("📈 Chart Area")
chart_card = st.sidebar.color_picker("Chart Card", "#9383EA")
chart_title = st.sidebar.color_picker("Chart Title", "#4A148C")
chart_subtitle = st.sidebar.color_picker("Chart Subtitle", "#7E57C2")
chart_icons = st.sidebar.color_picker("Chart Icons", "#CE93D8")
chart_values = st.sidebar.color_picker("Chart Values", "#311B92")

# Button Area
st.sidebar.subheader("🧷 Button Area")
button_primary = st.sidebar.color_picker("Button Primary", "#7C3AED")
button_primary_text = st.sidebar.color_picker("Button Primary Text", "#FFFFFF")
button_secondary = st.sidebar.color_picker("Button Secondary", "#9575CD")
button_secondary_text = st.sidebar.color_picker("Button Secondary Text", "#FFFFFF")

# Tooltip Area
st.sidebar.subheader("💬 Tooltip")
tooltip_card_bg = st.sidebar.color_picker("Tooltip Card Background", "#F0F4C3")
tooltip_text = st.sidebar.color_picker("Tooltip Text", "#333333")

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
    --button-primary-text: {button_primary_text};
    --button-secondary: {button_secondary};
    --button-secondary-text: {button_secondary_text};
    --tooltip-card-bg: {tooltip_card_bg};
    --tooltip-text: {tooltip_text};
}}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# --- Dashboard Preview Section ---
st.markdown("<div class='dashboard-preview'>", unsafe_allow_html=True)

# Header
st.markdown(f"<h2 style='color:{header_title}; margin-bottom:0;'>Dashboard Header</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{header_subtitle}; margin-top:0;'>A quick overview of your data</p>", unsafe_allow_html=True)

# KPI Cards
st.markdown("<div class='kpi'>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>$12,345<br><span style='font-size:0.8em;'>Revenue</span></div>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>45.6 %<br><span style='font-size:0.8em;'>Conversion</span></div>", unsafe_allow_html=True)
st.markdown("<div class='kpi-card'>1,234<br><span style='font-size:0.8em;'>Users</span></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Charts
st.markdown("<div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("<div class='chart'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Buttons
st.markdown(f"""
    <br>
    <button class="button-primary">Primary Action</button>
    <button class="button-secondary">Secondary Action</button>
""", unsafe_allow_html=True)

# Close dashboard preview container
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© All rights reserved by AthiramolPS, Published on June 2025</div>", unsafe_allow_html=True)
