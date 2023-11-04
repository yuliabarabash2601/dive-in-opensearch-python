from fastapi import FastAPI, Form
import requests

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Welcome to the homepage!"}


@app.post("/pipe")
async def pipe(data: str = Form(...)):
    payload = {}
    headers = {}
    url = f"http://127.0.0.1:4000/autocomplete?query={data}"
    response = requests.get(url, headers=headers, data=payload)
    return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
