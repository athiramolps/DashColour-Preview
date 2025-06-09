import streamlit as st

# Set page config
st.set_page_config(page_title="DashColor Preview", layout="wide")

# Title Section
st.markdown("""
    <div style="text-align:center; padding-top:10px;">
        <h1 style="color:#8B5CF6;">🎨 DashColor Preview</h1>
        <p style="color:#6B7280; font-size:18px; max-width:700px; margin:auto;">
            Dashboard preview styled with the selected colors.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar Input Fields
st.sidebar.header("🎨 Color Input Fields")

bg = st.sidebar.color_picker("Background", "#F3F4F6")
sidebar = st.sidebar.color_picker("Side bar", "#E5E7EB")
icons_sidebar = st.sidebar.color_picker("Icons in the side bar", "#6B7280")
logo = st.sidebar.color_picker("Logo", "#8B5CF6")
title = st.sidebar.color_picker("Title", "#681C87")
kpi = st.sidebar.color_picker("KPI Cards", "#A355F7")
button = st.sidebar.color_picker("Buttons", "#7C3AED")
charts = st.sidebar.color_picker("Charts", "#9383EA")

# Layout Section
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(f"""
        <div style='background-color:{bg}; padding:30px; border-radius:10px;'>

            <!-- Dashboard Header -->
            <h2 style='color:{title};'>Dashboard</h2>
            <p style='color:{icons_sidebar}; margin-top:-10px;'>One-line explanitiation</p>

            <!-- KPI Cards -->
            <div style='display:flex; gap:20px; margin-top:25px;'>
                <div style='flex:1; background-color:{sidebar}; padding:20px; border-radius:8px; color:{title}; text-align:center;'>
                    <h3>$12,345</h3><p>Label</p>
                </div>
                <div style='flex:1; background-color:{sidebar}; padding:20px; border-radius:8px; color:{title}; text-align:center;'>
                    <h3>45.6 %</h3><p>Label</p>
                </div>
                <div style='flex:1; background-color:{sidebar}; padding:20px; border-radius:8px; color:{title}; text-align:center;'>
                    <h3>1,234</h3><p>Label</p>
                </div>
            </div>

            <!-- Charts & Graphs Section -->
            <div style='display:flex; gap:20px; margin-top:25px;'>
                <div style='flex:2; background-color:#F5F3FF; padding:20px; border-radius:8px;'>
                    <p style='color:{charts}; text-align:center;'>📈 Line Chart</p>
                </div>
                <div style='flex:1; background-color:#F5F3FF; padding:20px; border-radius:8px;'>
                    <p style='color:{charts}; text-align:center;'>🟣 Pie Chart</p>
                </div>
            </div>

            <div style='display:flex; gap:20px; margin-top:25px;'>
                <div style='flex:1; background-color:#F5F3FF; padding:20px; border-radius:8px;'>
                    <button style='background-color:{button}; color:white; width:100%; padding:10px; border:none; border-radius:5px;'>Button</button>
                </div>
                <div style='flex:2; background-color:#F5F3FF; padding:20px; border-radius:8px;'>
                    <p style='color:{charts}; text-align:center;'>📊 Bar Chart</p>
                </div>
            </div>

        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""<br><br><hr style="border: 0.5px solid #ccc;">""", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; color:gray; font-size:13px;">
        © 2024 DashColor. All rights reserved.
    </div>
""", unsafe_allow_html=True)
