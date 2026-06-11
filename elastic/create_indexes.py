from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
from elastic.elastic_client import es


# print(es.info())
# create sales index
sales_mapping = {
    "mappings": {
        "properties": {
            "order_id": {"type": "keyword"},
            "customer_id": {"type": "keyword"},
            "order_date": {"type": "date"},
            "region": {"type": "keyword"},
            "category": {"type": "keyword"},
            "revenue": {"type": "float"},
            "payment_status": {"type": "keyword"},
            "shipping_status": {"type": "keyword"}
        }
    }
}
if not es.indices.exists(index="sales_data"):
    es.indices.create(
        index="sales_data",
        body=sales_mapping
    )
    print("Created sales_data index")

# create web_analytics index
web_analytics_mapping = {
    "mappings": {
        "properties": {
            "date": {"type": "date"},
            "visitors": {"type": "integer"},
            "sessions": {"type": "integer"},
            "conversion_rate": {"type": "float"},
            "bounce_rate": {"type": "float"},
            "checkout_failures": {"type": "integer"}
        }
    }
}
if not es.indices.exists(index="web_analytics"):
    es.indices.create(
        index="web_analytics",
        body=web_analytics_mapping
    )
    print("Created web_analytics index")

# create support_ticket index
support_tickets_mapping = {
    "mappings": {
        "properties": {
            "ticket_id": {"type": "keyword"},
            "customer_id": {"type": "keyword"},
            "date": {"type": "date"},
            "issue_type": {"type": "keyword"},
            "priority": {"type": "keyword"},
            "description": {"type": "text"},
            "source_event": {"type": "keyword"}
        }
    }
}
if not es.indices.exists(index="support_tickets"):
    es.indices.create(
        index="support_tickets",
        body=support_tickets_mapping
    )
    print("Created support_tickets index")

# create customer_review index
customer_reviews_mapping = {
    "mappings": {
        "properties": {
            "review_id": {"type": "keyword"},
            "customer_id": {"type": "keyword"},
            "date": {"type": "date"},
            "rating": {"type": "integer"},
            "review_text": {"type": "text"},
            "source_event": {"type": "keyword"}
        }
    }
}
if not es.indices.exists(index="customer_reviews"):
    es.indices.create(
        index="customer_reviews",
        body=customer_reviews_mapping
    )
    print("Created customer_reviews index")

  

# create product_events index
product_events_mapping = {
    "mappings": {
        "properties": {
            "event_id": {"type": "keyword"},
            "date": {"type": "date"},
            "event_type": {"type": "keyword"},
            "description": {"type": "text"}
        }
    }
}
if not es.indices.exists(index="product_events"):
    es.indices.create(
        index="product_events",
        body=product_events_mapping
    )
    print("Created product_events index")