from fastapi import FastAPI, Query
from opensearch import OpenSearch
from pydantic import BaseModel

app = FastAPI()

# OpenSearch Configuration
NODE_NAME = "myelkfirst"
opensearch_client = OpenSearch([{"host": "localhost", "port": 9200}])


class QueryParams(BaseModel):
    query: str = Query(..., description="Query parameter is Required")


@app.get("/autocomplete")
async def autocomplete(query_params: QueryParams):
    base_query = {
        "_source": [],
        "size": 0,
        "min_score": 0.5,
        "query": {
            "bool": {
                "must": [
                    {"match_phrase_prefix": {"title": {"query": query_params.query}}}
                ],
                "filter": [],
                "should": [],
                "must_not": [],
            }
        },
        "aggs": {
            "auto_complete": {
                "terms": {
                    "field": "title.keyword",
                    "order": {"_count": "desc"},
                    "size": 25,
                }
            }
        },
    }

    res = opensearch_client.search(index=NODE_NAME, size=0, body=base_query)
    return res
