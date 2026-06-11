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
You are an expert Business Operations Analyst.

Your job is to investigate business incidents using the provided evidence.

User Question:
{user_query}

Investigation Type:
{investigation_type}

Evidence:
{evidence}

Analyze the evidence and generate a professional business investigation report.

Use the following structure exactly:

# Executive Summary

Provide a brief overview of the incident.

# Root Cause

Identify the most likely root cause and explain why.

# Confidence Level

State:
- High
- Medium
- Low

and explain your confidence.

# Business Impact

Describe:
- Revenue impact
- Customer impact
- Operational impact
- Reputational impact

# Recommended Actions

Provide:
1. Immediate Actions
2. Short-Term Actions
3. Long-Term Preventive Actions

Important Rules:
- Base conclusions only on the provided evidence.
- Do not invent facts.
- Do not include any author name.
- Do not include "Prepared By".
- Do not include signatures.
- Return only the report in markdown format.
"""


def investigate(user_query):

    # Step 1: Determine investigation type
    investigation_type = (
        determine_investigation_type(
            user_query
        )
    )

    # Step 2: Collect evidence
    evidence = (
        collect_evidence(
            investigation_type
        )
    )

    # Step 3: Build prompt
    prompt = build_prompt(
        user_query,
        investigation_type,
        evidence
    )

    # Step 4: Generate report
    response = model.generate_content(
        prompt
    )

    # Step 5: Return report
    return response.text


if __name__ == "__main__":

    query = (
        "Investigate app crashes after release"
    )

    report = investigate(
        query
    )

    print(report)