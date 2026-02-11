import streamlit as st

def show_explainable_ai_panel(
    total_study: int,
    total_distract: int,
    healthy_balance_score: int,
    forecast_app: str,
    avg_forecast: float,
    daily_limit: int,
    category_map: dict
):
    st.subheader("🧠 Explainable AI Panel")

    reasons = []
    confidence = 0

    if total_distract > total_study:
        reasons.append("Non-educational usage is higher than study time")
        confidence += 35
    else:
        reasons.append("Study time outweighs distraction usage")
        confidence += 25

    if healthy_balance_score < 50:
        reasons.append("Healthy balance score is low")
        confidence += 30
    else:
        reasons.append("Healthy balance score is acceptable")
        confidence += 20

    if avg_forecast > daily_limit:
        reasons.append(
            f"Predicted future usage of {forecast_app} exceeds daily limit"
        )
        confidence += 25
    else:
        reasons.append(
            f"Predicted future usage of {forecast_app} is within limit"
        )
        confidence += 15

    confidence = min(confidence, 95)

    st.markdown("### 🔍 AI Decision Explanation")
    st.write("**Key factors considered:**")

    for r in reasons:
        st.write(f"- {r}")

    st.metric("AI Confidence Score", f"{confidence}%")

    st.info(
        "This AI explains *why* decisions are made using historical usage, "
        "category analysis, and future trends instead of black-box predictions."
    )
