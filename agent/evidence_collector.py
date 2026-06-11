from elastic.search_queries import (
    get_payment_failures,
    get_checkout_complaints,
    get_negative_reviews,
    get_related_events
)

from agent.config import (
    INVESTIGATION_CONFIG
)


def extract_sources(records):

    return [
        hit["_source"]
        for hit in records
    ]


def collect_evidence(investigation_type):

    config = INVESTIGATION_CONFIG.get(
        investigation_type
    )

    if not config:

        return {
            "payment_failures": [],
            "complaints": [],
            "reviews": [],
            "events": []
        }

    # Reviews
    reviews = get_negative_reviews(
        config["review_keyword"]
    )

    # Events
    events = get_related_events(
        config["event_keyword"]
    )

    # Optional Sources
    payment_failures = []
    complaints = []

    if config["include_failures"]:

        payment_failures = (
            get_payment_failures()
        )

    if config["include_complaints"]:

        complaints = (
            get_checkout_complaints()
        )

    evidence = {

        "payment_failures":
            extract_sources(
                payment_failures
            ),

        "complaints":
            extract_sources(
                complaints
            ),

        "reviews":
            extract_sources(
                reviews
            ),

        "events":
            extract_sources(
                events
            )
    }

    return evidence


if __name__ == "__main__":

    for investigation_type in [
        "payment",
        "app",
        "shipping"
    ]:

        print(
            f"\n{investigation_type.upper()} INVESTIGATION"
        )

        evidence = collect_evidence(
            investigation_type
        )

        print(
            evidence.keys()
        )