from agent.planner import (
    determine_investigation_type
)

from agent.evidence_collector import (
    collect_evidence
)

from agent.gemini_client import model


def build_prompt(
    user_query,
    investigation_type,
    evidence
):
    return f"""
You are a Senior Business Operations Analyst.

User Question:
{user_query}

Investigation Type:
{investigation_type}

Evidence:
{evidence}

Analyze the evidence and provide:

1. Root Cause
2. Confidence Level
3. Business Impact
4. Recommended Actions

Write a professional investigation report.
"""


def investigate(user_query):

    # Step 1
    investigation_type = (
        determine_investigation_type(
            user_query
        )
    )

    # Step 2
    evidence = (
        collect_evidence(
            investigation_type
        )
    )

    # Step 3
    prompt = build_prompt(
        user_query,
        investigation_type,
        evidence
    )

    # Step 4
    response = model.generate_content(
        prompt
    )

    # Step 5
    return response.text


if __name__ == "__main__":

    query = ("Investigate app crashes after release")

    report = investigate(
        query
    )

    print(report)