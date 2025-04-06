from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

app = FastAPI()

class PurchaseUpdate(BaseModel):
    username: str
    items: list[str]

DB_PATH = "app/fake_user_data.json"

def load_data():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/user/purchase")
def update_purchase(data: PurchaseUpdate):
    users = load_data()
    if data.username not in users:
        return {"error": "User not found"}

    users[data.username]["purchases"].extend(data.items)
    users[data.username]["cart"] = []  # 장바구니 비우기
    save_data(users)
    return {"message": "Purchase updated successfully"}
