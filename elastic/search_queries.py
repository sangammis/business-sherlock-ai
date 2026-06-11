from elastic.elastic_client import es


def get_payment_failures():

    response = es.search(
        index="sales_data",
        size=5,
        query={
            "term": {
                "payment_status": "Failed"
            }
        }
    )

    return response["hits"]["hits"]


def get_checkout_complaints():

    response = es.search(
        index="support_tickets",
        size=10,
        query={
            "match": {
                "description": "checkout"
            }
        }
    )

    return response["hits"]["hits"]


def get_negative_reviews(keyword):

    response = es.search(
        index="customer_reviews",
        size=10,
        query={
            "match": {
                "review_text": keyword
            }
        }
    )

    return response["hits"]["hits"]


def get_related_events(keyword):

    response = es.search(
        index="product_events",
        size=5,
        query={
            "multi_match": {
                "query": keyword,
                "fields": [
                    "event_type",
                    "description"
                ]
            }
        }
    )

    return response["hits"]["hits"]


if __name__ == "__main__":

    print("\nPAYMENT FAILURES")
    print(get_payment_failures())

    print("\nCHECKOUT COMPLAINTS")
    print(get_checkout_complaints())

    print("\nNEGATIVE REVIEWS")
    print(get_negative_reviews("payment"))

    print("\nRELATED EVENTS")
    print(get_related_events("payment"))