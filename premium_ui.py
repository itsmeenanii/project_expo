import streamlit as st

# -----------------------------
# Apply premium CSS/UI
# -----------------------------
def apply_premium_ui():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    footer {visibility: hidden;}
    header {visibility: hidden;}

    .glass {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 18px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
    }

    .hero {
        background: linear-gradient(135deg, #6366f1, #22d3ee);
        border-radius: 22px;
        padding: 30px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }

    .metric-box {
        background: white;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }

    .metric-title {
        font-size: 14px;
        color: #6b7280;
    }

    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #111827;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)


# -----------------------------
# Hero banner
# -----------------------------
def show_hero_banner():
    st.markdown("""
    <div class="hero">
        <h1>👨‍👩‍👧 Smart Parent–Child Analytics</h1>
        <p>AI-powered monitoring • Predictive insights • Explainable decisions</p>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Metric row
# -----------------------------
def metric_row(study, distract, total, score):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">📘 Study</div>
            <div class="metric-value">{study}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">🎮 Distraction</div>
            <div class="metric-value">{distract}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">⏱ Total</div>
            <div class="metric-value">{total}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        color = "#16a34a" if score >= 60 else "#dc2626"
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">🧠 Balance</div>
            <div class="metric-value" style="color:{color};">{score}%</div>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------
# Section header
# -----------------------------
def section(title: str):
    st.markdown(f"<div class='section-title'>✨ {title}</div>", unsafe_allow_html=True)


# -----------------------------
# Glass container wrapper
# -----------------------------
def glass_container(content_func):
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    content_func()
    st.markdown("</div>", unsafe_allow_html=True)
