"""
Planner Module

Purpose:
Determine which type of investigation should be executed
based on the user's query.

Investigation Types:
- payment
- app
- shipping
- unknown
"""


def determine_investigation_type(user_query):

    query = user_query.lower()

    # Payment / Revenue Investigation
    if any(
        keyword in query
        for keyword in [
            "revenue",
            "payment",
            "checkout",
            "transaction",
            "sales",
            "purchase"
        ]
    ):
        return "payment"

    # Mobile App Investigation
    elif any(
        keyword in query
        for keyword in [
            "app",
            "mobile",
            "login",
            "crash",
            "performance",
            "authentication"
        ]
    ):
        return "app"

    # Shipping Investigation
    elif any(
        keyword in query
        for keyword in [
            "shipping",
            "delivery",
            "package",
            "tracking",
            "shipment",
            "logistics"
        ]
    ):
        return "shipping"

    # Unknown Investigation
    else:
        return "unknown"


if __name__ == "__main__":

    test_queries = [
        "Investigate revenue decline in March",
        "Investigate payment failures",
        "Why are customers unable to checkout?",
        "Investigate app crashes after release",
        "Why is mobile login failing?",
        "Investigate delivery delays",
        "Why are packages arriving late?",
        "Investigate customer satisfaction"
    ]

    print("\nPlanner Test Results")
    print("-" * 50)

    for query in test_queries:

        investigation_type = determine_investigation_type(
            query
        )

        print(
            f"Query: {query}"
        )

        print(
            f"Investigation Type: {investigation_type}"
        )

        print("-" * 50)