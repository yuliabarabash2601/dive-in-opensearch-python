import json
from typing import List, Dict, Any

from opensearchpy.client import OpenSearch
import pandas as pd

SIMPEL_INDEX = {}

N_GRAM_INDEX = {
    "mappings": {
        "properties": {
            "type": {"type": "text", "analyzer": "autocomplete"},
            "title": {"type": "text", "analyzer": "autocomplete"},
            "description": {"type": "text", "analyzer": "autocomplete"},
        }
    },
    "settings": {
        "analysis": {
            "filter": {
                "edge_ngram_filter": {
                    "type": "edge_ngram",
                    "min_gram": 1,
                    "max_gram": 20,
                }
            },
            "analyzer": {
                "autocomplete": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "edge_ngram_filter"],
                }
            },
        }
    },
}


COMPLEMETATION_INDEX = {
    "mappings": {
        "properties": {
            "type": {"type": "completion"},
            "title": {"type": "completion"},
            "description": {"type": "completion"},
        }
    }
}

SEARCH_AS_YOU_TYPE_INDEX = {
    "mappings": {
        "properties": {
            "type": {"type": "search_as_you_type"},
            "title": {"type": "search_as_you_type"},
            "description": {"type": "search_as_you_type"},
        }
    }
}

INDEX_TO_CREATE = [
    {"index_name": "prefix_match_netflix", "index_template": SIMPEL_INDEX},
    {"index_name": "n_gram_netflix", "index_template": N_GRAM_INDEX},
    {"index_name": "completion_netflix", "index_template": COMPLEMETATION_INDEX},
    {
        "index_name": "search_as_you_type_netflix",
        "index_template": SEARCH_AS_YOU_TYPE_INDEX,
    },
]


def create_index(opensearch, index_name, index_template):
    print(f"Creating index: {index_name}")
    if not opensearch.indices.exists(index=index_name):
        opensearch.indices.create(index=index_name, body=index_template)
    else:
        print(f"Index {index_name} already exists")


def load_dataset() -> List[Dict[str, Any]]:
    return json.loads(pd.read_csv("data/netflix_titles.csv").to_json(orient="records"))


def transform_to_bulk(dataset: List[Dict[str, Any]], index_name: str) -> str:
    bulk_opensearch = ""
    for row in dataset:
        bulk_opensearch += '{"index": {"_index": "%s", "_id": "%s"}}\n' % (
            index_name,
            row["show_id"],
        )
        bulk_opensearch += json.dumps(row) + "\n"
    return bulk_opensearch


if __name__ == "__main__":
    print("Initiating OpenSearch client")
    opensearch_client = OpenSearch(
        hosts=[{"host": "localhost", "port": 9200}],
        http_auth=("admin", "admin"),
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    print("Creating indexes")
    for index in INDEX_TO_CREATE:
        create_index(
            opensearch=opensearch_client,
            index_name=index.get("index_name"),
            index_template=index.get("index_template"),
        )
    print("Inserting data")
    dataset_json = load_dataset()
    for index in INDEX_TO_CREATE:
        bulk_opensearch = transform_to_bulk(
            dataset=dataset_json, index_name=index.get("index_name")
        )
        response = opensearch_client.bulk(
            body=bulk_opensearch, index=index.get("index_name")
        )
        print(response)
