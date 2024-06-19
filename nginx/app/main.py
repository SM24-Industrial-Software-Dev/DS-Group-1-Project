from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/echo/{text}")
def read_item(text: str):
    return {"Echo": text}