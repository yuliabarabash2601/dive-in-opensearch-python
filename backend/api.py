from fastapi import FastAPI, Query
from opensearchpy import OpenSearch

from pydantic import BaseModel

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


class QueryParams(BaseModel):
    query: str = Query(..., description="Query parameter is Required")


@app.get("/autocomplete")
async def autocomplete(query: str):
    index_name = "prefix_match_netflix"
    wildcard_query = {
        "_source": ["title"],
        "size": 25,
        "query": {"wildcard": {"title.keyword": f"{query}*"}},
    }

    res = opensearch_client.search(index=index_name, body=wildcard_query)

    # Extract and return only the titles from the response
    autocomplete_results = [hit["_source"]["title"] for hit in res["hits"]["hits"]]

    return autocomplete_results

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
