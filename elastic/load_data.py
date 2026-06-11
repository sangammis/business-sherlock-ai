import pandas as pd
from elasticsearch.helpers import bulk
from elastic.elastic_client import es

# generic loader function
def load_csv_to_index(csv_path, index_name):
    df = pd.read_csv(csv_path)
    actions = []
    for _, row in df.iterrows():

        actions.append({
            "_index": index_name,
            "_source": row.to_dict()
        })
    bulk(es, actions)
    print(
        f"Loaded {len(df):,} records into {index_name}"
    )

# load all datasets 
load_csv_to_index(
    "data/generated/sales_data.csv",
    "sales_data"
)

load_csv_to_index(
    "data/generated/web_analytics.csv",
    "web_analytics"
)

load_csv_to_index(
    "data/generated/support_tickets.csv",
    "support_tickets"
)

load_csv_to_index(
    "data/generated/customer_reviews.csv",
    "customer_reviews"
)

load_csv_to_index(
    "data/generated/product_events.csv",
    "product_events"
)