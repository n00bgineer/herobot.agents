from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a GET endpoint at the root path "/"
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Optional: Add another endpoint with a path parameter
@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}