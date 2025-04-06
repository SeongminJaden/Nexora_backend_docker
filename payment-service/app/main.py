from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class PaymentRequest(BaseModel):
    username: str

DB_SERVICE_URL = "http://db:8000"

@app.post("/purchase")
def purchase_items(req: PaymentRequest):
    # 1. 유저의 장바구니 정보 요청
    try:
        res = requests.get(f"{DB_SERVICE_URL}/user/data?username={req.username}")
        user_data = res.json()
    except Exception:
        raise HTTPException(status_code=500, detail="DB service unreachable")

    if res.status_code != 200 or "cart" not in user_data:
        raise HTTPException(status_code=404, detail="User not found or invalid response from DB service")

    cart = user_data["cart"]
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # 2. 구매내역으로 옮기기 (DB에 요청)
    update_payload = {
        "username": req.username,
        "items": cart
    }
    update_res = requests.post(f"{DB_SERVICE_URL}/user/purchase", json=update_payload)

    if update_res.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to update purchase history")

    return {
        "message": "Purchase completed successfully",
        "purchased_items": cart
    }
