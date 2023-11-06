from fastapi import FastAPI
from opensearchpy import OpenSearch

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# OpenSearch Configuration
opensearch_client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)


app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/prefix_match/autocomplete")
async def autocomplete(query: str):
    index_name = "prefix_match_netflix"
    wildcard_query = {
        "query": {
            "match_phrase_prefix": {
                "title": {"query": query, "slop": 3, "max_expansions": 10}
            }
        }
    }
    res = opensearch_client.search(index=index_name, body=wildcard_query)

    # Extract and return only the titles from the response
    autocomplete_results = [hit["_source"]["title"] for hit in res["hits"]["hits"]]

    return autocomplete_results


@app.get("/n_gram/autocomplete")
async def autocomplete(query: str):
    index_name = "n_gram_netflix"
    wildcard_query = {
        "query": {"match": {"title": {"query": query, "analyzer": "standard"}}}
    }
    res = opensearch_client.search(index=index_name, body=wildcard_query)

    # Extract and return only the titles from the response
    autocomplete_results = [hit["_source"]["title"] for hit in res["hits"]["hits"]]

    return autocomplete_results


@app.get("/completion/autocomplete")
async def autocomplete(query: str):
    index_name = "completion_netflix"
    wildcard_query = {
        "suggest": {"autocomplete": {"prefix": query, "completion": {"field": "title"}}}
    }
    res = opensearch_client.search(index=index_name, body=wildcard_query)

    # Extract and return only the titles from the response
    autocomplete_results = [hit["_source"]["title"] for hit in res["hits"]["hits"]]

    return autocomplete_results


@app.get("/search_as_you_type/autocomplete")
async def autocomplete(query: str):
    index_name = "search_as_you_type_netflix"
    wildcard_query = {
        "query": {
            "multi_match": {
                "query": query,
                "type": "bool_prefix",
                "fields": ["title", "title._2gram", "title._3gram"],
            }
        },
        "size": 3,
    }
    res = opensearch_client.search(index=index_name, body=wildcard_query)

    # Extract and return only the titles from the response
    autocomplete_results = [hit["_source"]["title"] for hit in res["hits"]["hits"]]

    return autocomplete_results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
