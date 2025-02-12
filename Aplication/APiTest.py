from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, os

items = []

app = FastAPI(
    title="API Test",
    description="API Test",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONT_URL")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Anomaly": "Lo mejor del mundo"}

@app.get("/items/")
def read_items():
    return items

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = items[item_id]
    items.pop(item_id)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8030))
    uvicorn.run(app, host="0.0.0.0", port=port)