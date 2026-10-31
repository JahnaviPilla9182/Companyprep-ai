"""
app.py — CompanyPrep AI Entry Point & Role-Based Dashboard
Architecture:
- Landing Page (Public default initial route, no sidebar)
- Login Page (Standalone auth view, no sidebar)
- Role-Based Dashboards (User Dashboard & Admin Dashboard with dedicated sidebar)
"""
import streamlit as st
import uuid
import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(__file__))

# Initialize DB on first run
from database.db_manager import (
    init_db, upsert_user, save_roadmap, save_roadmap_weeks,
    get_progress_summary, get_roadmap, get_roadmap_weeks,
    get_user_resume_checkpoint, update_user_active_roadmap,
    get_user_assessments
)
init_db()

# Page config
st.set_page_config(
    page_title="CompanyPrep AI — Technical Interview Preparation",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components.ui_helpers import (
    inject_custom_css, show_header, show_metric_card,
    show_empty_state, show_disclaimer, show_info_card, show_ai_badge,
    progress_bar_custom, init_session_auth, render_sidebar_auth,
    render_login_page, render_landing_page, render_admin_dashboard,
    render_resume_hero_card, render_account_security_card
)
from backend.services.llm_service import get_provider_info
from backend.core.roadmap_generator import generate_roadmap

# Restore session state & auth token
init_session_auth()

# Sync query params with view state
if "view" in st.query_params:
    requested_view = st.query_params["view"]
    if requested_view in ("landing", "login", "dashboard"):
        st.session_state.view = requested_view

user_is_logged_in = st.session_state.get("logged_in", False)

# ---------------------------------------------------------------------------
# Unauthenticated Navigation Flow: Landing Page -> Login Page
# ---------------------------------------------------------------------------
if not user_is_logged_in:
    current_view = st.session_state.get("view", "landing")
    if current_view == "login":
        render_login_page()
        st.stop()
    else:
        render_landing_page()
        st.stop()

# ---------------------------------------------------------------------------
# Authenticated Navigation Flow: Role-Based Dashboard (with Sidebar)
# ---------------------------------------------------------------------------
inject_custom_css(hide_sidebar=False)

user_id = st.session_state.get("user_id")
user_role = st.session_state.get("role", "USER")
display_name = st.session_state.get("display_name", "Student")

# ---- Dashboard Sidebar ----
with st.sidebar:
    st.markdown("""
    <div style='padding: 0.8rem 0.5rem 0.5rem 0.5rem;'>
        <div style='display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.4rem;'>
            <div style='width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg, #4F46E5, #6366F1);
                        display: flex; align-items: center; justify-content: center; font-size: 1.3rem; color: #FFF;'>
                🎯
            </div>
            <div>
                <h3 style='margin:0; font-size:1.1rem; font-weight:800; color:#0F172A;'>CompanyPrep AI</h3>
                <span style='color:#64748B; font-size:0.75rem; font-weight:600;'>GMRIT Project 08</span>
            </div>
        </div>
    </div>
    <hr style='border: none; height: 1px; background: #E2E8F0; margin: 0.5rem 0 0.8rem 0;'>
    """, unsafe_allow_html=True)

    # User Profile & Sign Out
    render_sidebar_auth()

    provider_info = get_provider_info()
    show_ai_badge(provider_info["provider"], provider_info["demo_mode"])

    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.75rem; text-transform:uppercase; font-weight:700; color:#64748B; letter-spacing:0.06em; margin-bottom:0.4rem;'>Modules</p>", unsafe_allow_html=True)
    st.page_link("app.py", label="🏠 Home Dashboard")
    st.page_link("pages/02_📋_Create_Roadmap.py", label="📋 Create Roadmap")
    st.page_link("pages/03_📅_Weekly_Roadmap.py", label="📅 Weekly Roadmap")
    st.page_link("pages/04_❓_Interview_Questions.py", label="❓ Interview Questions")
    st.page_link("pages/05_🎯_Skill_Assessment.py", label="🎯 Skill Assessment")
    st.page_link("pages/06_📄_JD_Analyzer.py", label="📄 JD Analyzer")
    st.page_link("pages/07_📊_Progress_Dashboard.py", label="📊 Progress Dashboard")
    st.page_link("pages/08_🔄_Revision_Planner.py", label="🔄 Revision Planner")
    st.page_link("pages/09_⚖️_Compare_Roadmaps.py", label="⚖️ Compare Roadmaps")
    st.page_link("pages/10_💼_Resume_Advisor.py", label="💼 Resume Advisor")
    st.page_link("pages/11_📥_Export_Calendar.py", label="📥 Export Calendar")

    st.markdown("""
    <hr style='border: none; height: 1px; background: #E2E8F0; margin: 1.4rem 0 0.8rem 0;'>
    <div style='font-size: 0.75rem; color: #64748B; text-align: center;'>
        CompanyPrep AI • v1.0<br>
        <span style='color: #94A3B8;'>GMRIT Student Project 08</span>
    </div>
    """, unsafe_allow_html=True)


# ---- Role-Based Main Content ----
if user_role == "ADMIN":
    # -----------------------------------------------------------------------
    # Admin Dashboard
    # -----------------------------------------------------------------------
    render_admin_dashboard()
else:
    # -----------------------------------------------------------------------
    # User Dashboard
    # -----------------------------------------------------------------------
    # Welcome Banner
    st.markdown(f"""
    <div style='padding: 1.8rem 2rem; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px;
                box-shadow: 0 4px 16px rgba(0,0,0,0.03); margin-bottom: 1.8rem;'>
        <div style='display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;'>
            <div>
                <div style='display: inline-flex; align-items: center; gap: 0.4rem; background: #EEF2FF;
                            color: #4338CA; font-size: 0.75rem; font-weight: 700; padding: 2px 10px; border-radius: 12px; margin-bottom: 0.5rem;'>
                    ⚡ STUDENT DASHBOARD
                </div>
                <h1 style='font-size: 2.2rem; font-weight: 800; color: #0F172A; margin: 0 0 0.4rem 0;'>
                    Welcome back, {display_name}! 👋
                </h1>
                <p style='color: #64748B; font-size: 0.98rem; margin: 0; max-width: 800px;'>
                    Track your registered interview preparation tracks, resume where you stopped, review past assessment scores, and practice coding challenges.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Active Registered Tracks & Resume Checkpoint
    checkpoint = get_user_resume_checkpoint(user_id) if user_id else None
    if checkpoint:
        if not st.session_state.get("roadmap_id"):
            st.session_state.roadmap_id = checkpoint["roadmap_id"]
            st.session_state.roadmap_data = checkpoint["roadmap_data"]
            st.session_state.roadmap_weeks = checkpoint["weeks"]
        render_resume_hero_card(checkpoint)
    else:
        st.markdown("""
        <div style='background: #FFFFFF; border: 1px dashed #CBD5E1; border-radius: 16px; padding: 1.8rem; text-align: center; margin-bottom: 1.8rem;'>
            <div style='font-size: 2.2rem; margin-bottom: 0.4rem;'>📋</div>
            <h3 style='margin: 0 0 0.3rem 0; color: #0F172A; font-size: 1.2rem; font-weight: 700;'>No Active Track Registered Yet</h3>
            <p style='color: #64748B; font-size: 0.92rem; margin: 0 0 1.2rem 0; max-width: 580px; margin-inline: auto;'>
                Select one of the 1-click curated company tracks below or build a custom curriculum to start generating and tracking your tasks.
            </p>
        </div>
        """, unsafe_allow_html=True)
