import streamlit as st

# Set page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Toggle for Dark Mode
theme_mode = st.toggle("🌗 Toggle Dark Mode", value=False)

# Title and Purpose
st.markdown(f"""
    <div style="text-align:center; padding-top:10px;">
        <h1 style="color:#9C27B0;">🎨 DashColor Preview</h1>
        <p style="color:gray; font-size:18px; max-width:700px; margin:auto;">
            Experiment with custom color schemes for dashboards. Choose your colors for each UI component and preview how your dashboard will look in light or dark mode.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar Input Section
st.sidebar.header("🎛️ Customize Your Theme")

bg_color = st.sidebar.color_picker("Background", "#ffffff" if not theme_mode else "#1e1e1e")
logo_color = st.sidebar.color_picker("Logo", "#1976D2")
title_color = st.sidebar.color_picker("Title", "#000000" if not theme_mode else "#ffffff")
subtitle_color = st.sidebar.color_picker("Subtitle", "#444444" if not theme_mode else "#dddddd")
text_color = st.sidebar.color_picker("Text", "#333333" if not theme_mode else "#cccccc")
kpi_color = st.sidebar.color_picker("KPI Cards", "#f5f5f5" if not theme_mode else "#2d2d2d")
button_color = st.sidebar.color_picker("Buttons", "#6200ea")
chart_color = st.sidebar.color_picker("Charts", "#4caf50")

# Layout: Input on Left, Preview on Right
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"""
        <div style='background-color:{bg_color}; padding:40px; border-radius:12px;'>

            <!-- Logo -->
            <div style='color:{logo_color}; font-size:28px; font-weight:bold;'>🔷 Your Logo</div>

            <!-- Title & Subtitle -->
            <h1 style='color:{title_color}; margin-bottom:5px;'>Dashboard Title</h1>
            <h4 style='color:{subtitle_color}; margin-top:0;'>Your Subtitle Here</h4>

            <!-- KPI Cards -->
            <div style='display:flex; gap:20px; margin-top:30px;'>
                {"".join([
                    f"<div style='flex:1; background-color:{kpi_color}; padding:20px; border-radius:8px; color:{text_color}; text-align:center;'>"
                    f"<h3>KPI {i}</h3><p>Value</p></div>" for i in range(1, 4)
                ])}
            </div>

            <!-- Button -->
            <div style='margin-top:30px;'>
                <button style='background-color:{button_color}; color:white; padding:10px 20px; border:none; border-radius:5px;'>Click Me</button>
            </div>

            <!-- Chart Section -->
            <div style='margin-top:30px; padding:20px; background-color:{chart_color}; border-radius:8px; color:white; text-align:center;'>
                📊 Chart Preview Area
            </div>

        </div>
    """, unsafe_allow_html=True)

# Footer Notes
st.markdown("""<br><br><hr style="border: 0.5px solid #ccc;">""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; color:gray; font-size:13px;">
        © All rights reserved by Athiramol PS<br>
        Published on: June 8, 2025<br>
        This project, “DashColor Preview: A Visual Tool for Dashboard Color Planning,” is an original creation by Athiramol PS. 
        The layout, interface, and underlying logic are protected under applicable copyright.
    </div>
""", unsafe_allow_html=True)
