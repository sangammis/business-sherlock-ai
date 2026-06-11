import streamlit as st

from agent.reasoning import (
    investigate
)

st.set_page_config(
    page_title="Business Sherlock AI",
    page_icon="🔎",
    layout="wide"
)

st.title(
    "🔎 Business Sherlock AI"
)

st.subheader(
    "Autonomous Business Investigation Agent"
)

query = st.text_input(
    "What would you like to investigate?",
    placeholder="Investigate revenue decline in March"
)

if st.button(
    "Investigate"
):

    with st.spinner(
        "Analyzing business data..."
    ):

        report = investigate(
            query
        )

    st.markdown(
        report
    )