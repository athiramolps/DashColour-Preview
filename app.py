import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Current colors from the image for direct mapping
# Note: These are approximated from the image and might need fine-tuning.
COLORS = {
    "Background": "#F3F4F6",
    "Background Input Fields": "#F3F4F6", # This is based on observation from the image, though not explicitly labelled as such in the color picker
    "Theme bar": "#E5E7EB", # Placeholder for the top bar/overall app background not explicitly defined
    "Icons in the side bar": "#6B7280",
    "Text in the side bar": "#8B5CF6",
    "Logo": "#6B1C87", # Approximated from the DashColor text color
    "Sidebar Background": "#6B1C87", # Main sidebar background
    "Primary button": "#3F3F46", # Approximated from the button on the left sidebar
    "Input Cards": "#A355F7",
    "Buttons": "#7C3AED", # The primary button color in the dashboard section
    "Text on buttons": "#9383EA", # This seems to be the text color for the button example
    "Dashboard Background": "#FFFFFF", # The main content area of the dashboard
    "KPI Card": "#FFFFFF", # The background of KPI cards
    "KPI Value Text": "#3F3F46", # Color for $12,345 etc.
    "KPI Label Text": "#6B7280", # Color for 'Label' text below KPI values
    "Chart Card": "#FFFFFF", # Background of the chart cards
    "Line Chart Color": "#8B5CF6", # The color of the line in the line chart
    "Bar Chart Color": "#8B5CF6", # The color of the bars in the bar chart
    "Pie Chart Colors": ["#8B5CF6", "#6B1C87", "#A355F7", "#BA68C8"], # Example colors for the pie chart
    "Button Background": "#7C3AED", # Background for the main button
    "Button Text": "#FFFFFF", # Text color for the main button
    "Dashboard Title": "#3F3F46",
    "Dashboard Subtitle": "#6B7280",
    "Sidebar Button Text": "#FFFFFF", # Text color for sidebar elements
    "Sidebar Button Background": "#8B5CF6", # Background for selected sidebar items
}


# Theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Style Reset and Base CSS ---
st.markdown(f"""
<style>
    /* General Reset and Font */
    body {{
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
        padding: 0;
        background-color: {COLORS["Background"]}; /* Overall page background */
    }}

    /* Streamlit specific adjustments */
    .st-emotion-cache-z5fcl4 {{ /* Main content padding */
        padding-left: 0rem;
        padding-right: 0rem;
        padding-top: 0rem;
    }}
    .st-emotion-cache-1jmve36 {{ /* Specific to wide layout main content padding */
        padding-right: 0rem;
        padding-left: 0rem;
    }}
    .st-emotion-cache-ch5f9d.e1nzilvr5 {{ /* Sidebar overall padding */
        padding-top: 0rem;
    }}

    /* Top Header Bar (simulated) */
    .header-bar {{
        background-color: {COLORS["Background"]}; /* Similar to overall background */
        padding: 1.5rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #eee; /* Light separator */
    }}
    .header-bar h1 {{
        color: {COLORS["Logo"]};
        margin: 0;
        font-size: 24px;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .header-bar h1 .icon {{
        font-size: 28px;
        color: {COLORS["Logo"]};
    }}
    .header-bar p {{
        color: {COLORS["Dashboard Subtitle"]};
        margin: 0;
        font-size: 16px;
    }}

    /* Custom sidebar styling to match image */
    .st-emotion-cache-17l70w9.ezr720f1 {{ /* Target sidebar background */
        background-color: {COLORS["Sidebar Background"]};
        padding-top: 2rem;
    }}
    .st-emotion-cache-17l70w9 .stButton > button {{
        background-color: {COLORS["Sidebar Button Background"]};
        color: {COLORS["Sidebar Button Text"]};
        border-radius: 8px;
        border: none;
        padding: 10px 15px;
        width: 100%;
        text-align: left;
        margin-bottom: 5px;
    }}
    .st-emotion-cache-17l70w9 .stButton > button:hover {{
        background-color: {COLORS["Input Cards"]}; /* Lighter shade on hover */
    }}
    .st-emotion-cache-17l70w9 .stButton > button p {{
        color: {COLORS["Sidebar Button Text"]};
        font-weight: 600;
    }}

    /* Specific styles for sidebar elements based on the image */
    .sidebar-section-title {{
        color: {COLORS["Text in the side bar"]};
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-left: 1rem; /* Indent titles */
    }}
    .sidebar-item {{
        display: flex;
        align-items: center;
        padding: 0.7rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 8px;
        cursor: pointer;
        color: {COLORS["Text in the side bar"]};
    }}
    .sidebar-item:hover {{
        background-color: {COLORS["Input Cards"]}; /* Hover effect */
    }}
    .sidebar-item.selected {{
        background-color: {COLORS["Input Cards"]};
        color: {COLORS["Sidebar Button Text"]};
    }}
    .sidebar-item .icon {{
        font-size: 20px;
        margin-right: 10px;
        color: {COLORS["Icons in the side bar"]};
    }}
    .sidebar-item.selected .icon {{
        color: {COLORS["Sidebar Button Text"]};
    }}

    /* Dashboard Container */
    .dashboard-container {{
        background-color: {COLORS["Dashboard Background"]};
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
        min-height: calc(100vh - 80px - 4rem); /* Adjust based on header/footer */
        margin: 2rem; /* Give some margin from the edges */
    }}

    /* Dashboard Header */
    .dashboard-header {{
        margin-bottom: 2rem;
    }}
    .dashboard-header h2 {{
        font-size: 26px;
        color: {COLORS["Dashboard Title"]};
        margin: 0;
    }}
    .dashboard-header p {{
        font-size: 16px;
        color: {COLORS["Dashboard Subtitle"]};
        margin-top: 5px;
    }}

    /* KPI Grid */
    .kpi-grid {{
        display: flex;
        gap: 1.5rem;
        margin-bottom: 2rem;
        justify-content: space-between;
    }}
    .kpi-card {{
        flex: 1;
        background-color: {COLORS["KPI Card"]};
        padding: 1.5rem;
        border-radius: 10px;
        text-align: left;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        min-width: 200px;
    }}
    .kpi-value {{
        font-size: 32px;
        font-weight: bold;
        color: {COLORS["KPI Value Text"]};
        margin-bottom: 5px;
    }}
    .kpi-label {{
        font-size: 16px;
        color: {COLORS["KPI Label Text"]};
    }}

    /* Chart Row */
    .chart-row {{
        display: flex;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }}
    .chart-box {{
        flex: 1;
        background-color: {COLORS["Chart Card"]};
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 250px; /* Ensure charts have enough height */
    }}
    /* Adjust Streamlit's internal chart container to fill parent */
    .chart-box .stPlotlyChart,
    .chart-box .stLineChart,
    .chart-box .stBarChart {{
        width: 100% !important;
        height: 100% !important;
    }}
    .stPlotlyChart > div, .stLineChart > div, .stBarChart > div {{
        height: 100% !important;
    }}


    /* Button Section */
    .button-section {{
        margin-top: 2rem;
        text-align: center; /* Center the button */
    }}
    .custom-button {{
        background-color: {COLORS["Button Background"]};
        color: {COLORS["Button Text"]};
        padding: 1rem 2.5rem;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }}
    .custom-button:hover {{
        background-color: {COLORS["Input Cards"]}; /* Slightly darker on hover */
    }}


    /* Footer */
    .footer {{
        margin-top: 3rem;
        text-align: center;
        font-size: 0.85rem;
        color: {COLORS["KPI Label Text"]};
        padding-bottom: 1rem;
    }}

    /* Streamlit specific overrides for widgets */
    .st-emotion-cache-1v0mbkd {{ /* Color picker label */
        color: {COLORS["Text in the side bar"]};
    }}
    .st-emotion-cache-1j0314j {{ /* Color picker input */
        background-color: {COLORS["Background Input Fields"]};
        border-color: {COLORS["Background Input Fields"]};
    }}
    .st-emotion-cache-f1jtxg.ezr720f3 {{ /* Subheader in sidebar */
        color: {COLORS["Text in the side bar"]};
    }}
    .st-emotion-cache-1r6psb4.ezr720f4 {{ /* Header in sidebar */
        color: {COLORS["Text in the side bar"]};
    }}

</style>
""", unsafe_allow_html=True)

# --- Top Bar (simulated) ---
# This top bar is outside the main Streamlit content area,
# so we'll simulate it with a markdown div at the very top.
st.markdown(f"""
<div class="header-bar">
    <h1><span class="icon">◎</span> DashColor Preview</h1>
    <p>Dashboard preview styled with the selected colors.</p>
</div>
""", unsafe_allow_html=True)

# --- Main Layout: Sidebar and Content ---
col_sidebar, col_content = st.columns([0.25, 0.75])

with col_sidebar:
    # Custom Sidebar UI based on image
    st.markdown("""
        <div class="sidebar-section-title">UI Color Inputs</div>
        <div class="sidebar-item selected"><span class="icon">🏠</span> Dashboard</div>
        <div class="sidebar-item"><span class="icon">📈</span> Analytics</div>
        <div class="sidebar-item"><span class="icon">⚙️</span> Settings</div>
        <div class="sidebar-item"><span class="icon">👤</span> Profile</div>
        <div class="sidebar-item"><span class="icon">🔔</span> Notifications</div>
        <div class="sidebar-item"><span class="icon">📊</span> Reports</div>
        <div class="sidebar-item"><span class="icon">💬</span> Feedback</div>
        <div class="sidebar-item"><span class="icon">❓</span> Help</div>
    """, unsafe_allow_html=True)

    # st.sidebar.header("🎛️ UI Color Inputs")
    #
    # # Sectioned Inputs (keeping for functionality, but visually hidden/modified by CSS)
    # def ui_section(title, fields):
    #     st.sidebar.subheader(f"📁 {title}")
    #     return {label: st.sidebar.color_picker(label, default) for label, default in fields}
    #
    # # In a real app, you'd use these color pickers to dynamically change the COLORS dict
    # # For this exercise, we are hardcoding COLORS based on the image.
    # # If you want the color pickers to work, you'd replace the above hardcoded COLORS with these:
    # # colors_from_pickers = {}
    # # colors_from_pickers.update(ui_section("Background Area", [("Background", "#F3F4F6")]))
    # # colors_from_pickers.update(ui_section("Sidebar Area", [("Sidebar Background", "#6B1C87"), ("Icons in the side bar", "#6B7280"), ("Text in the side bar", "#8B5CF6")]))
    # # ... and so on for all relevant colors.
    # # Then merge or use colors_from_pickers in your CSS generation.

with col_content:
    st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)

    # Dashboard Header
    st.markdown("""
        <div class="dashboard-header">
            <h2>Dashboard</h2>
            <p>One-line explantilation</p>
        </div>
    """, unsafe_allow_html=True)

    # KPI Section
    st.markdown("<div class='kpi-grid'>", unsafe_allow_html=True)
    kpis = [
        ("$12,345", "Label"),
        ("45.6 %", "Label"),
        ("1,234", "Label")
    ]
    for value, label in kpis:
        st.markdown(f"""
            <div class='kpi-card'>
                <div class='kpi-value'>{value}</div>
                <div class='kpi-label'>{label}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Chart Section
    st.markdown("<div class='chart-row'>", unsafe_allow_html=True)

    # Chart 1: Line Chart
    st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
    chart_data_line = pd.DataFrame({
        'x': np.arange(10),
        'y': np.random.rand(10) * 50 + 10 # Sample data
    })
    st.line_chart(chart_data_line, y='y', color=COLORS["Line Chart Color"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Chart 2: Bar Chart (approximated as the "bar chart" in the image is more like an area chart with bars)
    st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
    chart_data_bar = pd.DataFrame({
        'x': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'y': [10, 20, 15, 25, 22, 30] # Sample data
    })
    # This chart in the image is more like a simplified bar chart,
    # or an area chart with a bar-like appearance.
    # For simplicity, we'll use a bar chart, but without labels for a more "abstract" look.
    st.bar_chart(chart_data_bar, y='y', color=COLORS["Bar Chart Color"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Chart 3: Pie Chart (using Plotly for better customization for pie)
    st.markdown("<div class='chart-box'>", unsafe_allow_html=True)
    pie_labels = ['Category A', 'Category B', 'Category C', 'Category D']
    pie_values = [30, 25, 20, 25]
    fig_pie = go.Figure(data=[go.Pie(labels=pie_labels, values=pie_values,
                                     marker_colors=COLORS["Pie Chart Colors"],
                                     hole=0.6, # Make it a donut chart
                                     showlegend=False, # Hide legend for simplicity
                                     hoverinfo='label+percent')])
    fig_pie.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False) # Adjust layout to fit
    st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # Close chart-row

    # Button Section (moved to below charts in the image layout)
    st.markdown("<div class='button-section'>", unsafe_allow_html=True)
    st.markdown(f"<button class='custom-button'>Button</button>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # Close dashboard-container

# Footer
st.markdown("<div class='footer'>© 2024 DashColor. All rights reserved.</div>", unsafe_allow_html=True)
