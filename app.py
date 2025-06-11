import streamlit as st

st.set_page_config(page_title="DashColor Preview", layout="wide")

# --- Sidebar ---
st.sidebar.markdown("<h3 style='color:#8E44AD;'>🎨 Color Input Fields</h3>", unsafe_allow_html=True)

# Color Inputs
bg_color = st.sidebar.color_picker("Background", "#F3F4F6")
sidebar_color = st.sidebar.color_picker("Side bar", "#E5E7EB")
icon_color = st.sidebar.color_picker("Icons in the side bar", "#6B7280")
logo_color = st.sidebar.color_picker("Logo", "#8B5CF6")
title_color = st.sidebar.color_picker("Title", "#681C87")
subtitle_color = st.sidebar.color_picker("Subtitles", "#6B2146")
text_color = st.sidebar.color_picker("Text", "#3F3F46")
kpi_color = st.sidebar.color_picker("KPI Cards", "#A355F7")
button_color = st.sidebar.color_picker("Buttons", "#7C3AED")
chart_color = st.sidebar.color_picker("Charts", "#9383EA")

# --- Top Header ---
st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center;'>
        <div>
            <h1 style='color:{title_color};'>🧩 DashColor Preview</h1>
            <p style='color:{subtitle_color}; font-size:18px;'>Dashboard preview styled with the selected colors.</p>
        </div>
        <div>
            <label class="switch">
                <input type="checkbox">
                <span class="slider round"></span>
            </label>
        </div>
    </div>
    <hr style='margin:10px 0;'>
""", unsafe_allow_html=True)

# --- Dashboard Preview Layout ---
st.markdown(f"""
<div style='display: flex; background-color:{bg_color}; border-radius:10px;'>
    <!-- Sidebar -->
    <div style='width:80px; background-color:{sidebar_color}; padding:20px; border-top-left-radius:10px; border-bottom-left-radius:10px;'>
        <div style='color:{icon_color}; font-size:24px; margin-bottom:20px;'>🏠</div>
        <div style='color:{icon_color}; font-size:24px;'>📊</div>
    </div>

    <!-- Main Dashboard -->
    <div style='flex:1; padding:20px;'>
        <h2 style='color:{title_color};'>Dashboard</h2>
        <p style='color:{subtitle_color}; margin-bottom:20px;'>One-line explantilation</p>

        <!-- KPI Cards -->
        <div style='display:flex; gap:15px;'>
            <div style='flex:1; background-color:{kpi_color}; padding:20px; border-radius:10px; text-align:center; color:white;'>
                <h3>$12,345</h3><p>Label</p>
            </div>
            <div style='flex:1; background-color:{kpi_color}; padding:20px; border-radius:10px; text-align:center; color:white;'>
                <h3>45.6 %</h3><p>Label</p>
            </div>
            <div style='flex:1; background-color:{kpi_color}; padding:20px; border-radius:10px; text-align:center; color:white;'>
                <h3>1,234</h3><p>Label</p>
            </div>
        </div>

        <!-- Charts & Button -->
        <div style='display:flex; gap:15px; margin-top:20px;'>
            <div style='flex:2; background-color:{chart_color}20; border-radius:10px; padding:20px;'>📈</div>
            <div style='flex:1; background-color:{chart_color}20; border-radius:10px; padding:20px;'>🥧</div>
        </div>
        <div style='display:flex; gap:15px; margin-top:15px;'>
            <div style='flex:1; background-color:{chart_color}20; border-radius:10px; padding:20px;'>
                <button style='background-color:{button_color}; color:white; width:100%; padding:10px; border:none; border-radius:5px;'>Button</button>
            </div>
            <div style='flex:2; background-color:{chart_color}20; border-radius:10px; padding:20px;'>📊</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr style='margin:40px 0;'>
    <p style='text-align:center; color:gray;'>&copy; 2024 DashColor. All rights reserved.</p>
""", unsafe_allow_html=True)
