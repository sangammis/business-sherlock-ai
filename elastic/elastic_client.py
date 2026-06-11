from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

es = Elasticsearch(
    os.getenv("ELASTIC_URL"),
    basic_auth=(
        os.getenv("ELASTIC_USERNAME"),
        os.getenv("ELASTIC_PASSWORD")
    )
)

if not es.ping():
    raise Exception("Elastic connection failed")

print("Elastic connection successful")
