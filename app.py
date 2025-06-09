import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Style Reset and Base CSS ---
st.markdown("""
<style>
    /* These target Streamlit's main content area to remove default padding */
    .st-emotion-cache-z5fcl4 { /* This class might change with Streamlit updates */
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        padding-top: 0rem !important;
    }
    .st-emotion-cache-1jmve36 { /* This class might change with Streamlit updates */
        padding-right: 0rem !important;
        padding-left: 0rem !important;
    }
    /* Ensure the sidebar also doesn't push the content unnecessarily */
    .st-emotion-cache-s8s42d { /* sidebar */
        padding-top: 0rem;
    }


    body { font-family: 'Segoe UI', sans-serif; }

    .dashboard-container {
        background-color: var(--bg-color);
        padding: 2rem; /* Apply padding here for the whole dashboard */
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
        margin: 1rem; /* Add some margin around the whole container if desired */
    }

    .header-box {
        background-color: var(--header-card);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }

    .header-box h2 {
        margin: 0;
        color: var(--header-title);
    }

    .header-box p {
        margin: 0;
        font-size: 16px;
        color: var(--header-subtitle);
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin: 2rem 0 1rem;
        color: var(--section-title-color, #333); /* Made dynamic or fallback to #333 */
    }

    .kpi-grid {
        display: flex;
        gap: 1.2rem;
        margin-bottom: 2rem;
    }

    .kpi-card {
        flex: 1;
        background-color: var(--kpi-card);
        color: var(--kpi-text);
        padding: 1.2rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
    }

    .chart-row {
        display: flex;
        gap: 1.2rem;
        margin-bottom: 2rem;
    }

    .chart-box {
        flex: 1;
        height: 180px; /* Increased height to better accommodate charts */
        background-color: var(--chart-card);
        border-radius: 8px;
        display: flex; /* Use flexbox to center chart */
        justify-content: center; /* Center chart horizontally */
        align-items: center; /* Center chart vertically */
        overflow: hidden; /* Hide overflowing chart elements */
    }
    /* Style for Streamlit's internal chart divs to fill the chart-box */
    /* These classes are Streamlit-generated and might change in future versions */
    .chart-box > div > div > div { /* Target the inner div that contains the chart */
        width: 100% !important;
        height: 100% !important;
    }
    .chart-box .stPlotlyChart,
    .chart-box .stDeckGlChart,
    .chart-box .stVegaLiteChart {
        width: 100% !important;
        height: 100% !important;
    }


    .button-row {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }

    .button-primary {
        background-color: var(--button-primary);
        color: var(--button-primary-text);
        padding: 0.8rem 1.5rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
    }

    .button-secondary {
        background-color: var(--button-secondary);
        color: var(--button-secondary-text);
        padding: 0.8rem 1.5rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
    }

    .footer {
        margin-top: 4rem;
        text-align: center;
        font-size: 0.85rem;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)


# --- Dashboard Preview Area - NOW WRAPPING ALL THE MAIN CONTENT ---
st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)

# --- Title and Toggle ---
col1, col2 = st.columns([9, 1])
with col1:
    st.markdown("<h1 style='color:#9C27B0;'>🎨 DashColor Preview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:-10px;'>Dashboard preview styled with the selected colors.</p>", unsafe_allow_html=True)
with col2:
    st.toggle("🌙 Dark Mode", key="dark_mode")

# Header Section (This was already inside)
st.markdown("<div class='header-box'>", unsafe_allow_html=True)
st.markdown("<h2>Dashboard Header</h2>", unsafe_allow_html=True)
st.markdown("<p>A quick overview of your data</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# KPI Section
st.markdown("<div class='section-title'>📊 KPI Overview</div>", unsafe_allow_html=True)
st.markdown("<div class='kpi-grid'>", unsafe_allow_html=True)
for label, value in [("Revenue", "$12,345"), ("Conversion", "45.6 %"), ("Users", "1,234")]:
    st.markdown(f"<div class='kpi-card'>{value}<br><span style='font-weight: normal; font-size: 0.9em;'>{label}</span></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Chart Section
st.markdown("<div class='section-title'>📈 Charts</div>", unsafe_allow_html=True)
st.markdown("<div class='chart-row'>", unsafe_allow_html=True)

# Chart 1: Line Chart
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
chart_data1 = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(chart_data1)
st.markdown("</div>", unsafe_allow_html=True)

# Chart 2: Bar Chart
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
chart_data2 = pd.DataFrame(np.random.randint(0, 100, size=(20, 3)), columns=['X', 'Y', 'Z'])
st.bar_chart(chart_data2)
st.markdown("</div>", unsafe_allow_html=True)

# Chart 3: Area Chart
st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
chart_data3 = pd.DataFrame(np.random.randn(20, 2), columns=['Data1', 'Data2'])
st.area_chart(chart_data3)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Button Section
st.markdown("<div class='section-title'>🧷 Actions</div>", unsafe_allow_html=True)
st.markdown("<div class='button-row'>", unsafe_allow_html=True)
st.markdown("<button class='button-primary'>Primary Action</button>", unsafe_allow_html=True)
st.markdown("<button class='button-secondary'>Secondary Action</button>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Close the dashboard-container BEFORE the footer ---
st.markdown("</div>", unsafe_allow_html=True)

# Footer (This will now be outside the main styled container, which is common)
st.markdown("<div class='footer'>© All rights reserved by AthiramolPS, Published on June 2025</div>", unsafe_allow_html=True)
