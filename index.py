import uvicorn
from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}

# AWS LAMBDA DEPLOYMENT
handler = Mangum(app)

# LOCAL DEVELOPMENT => poetry run uvicorn index:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)