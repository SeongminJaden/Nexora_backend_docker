from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="Login Service",
    description="Simple login API using JSON as fake database",
    version="1.0.0"
)

class LoginRequest(BaseModel):
    username: str
    password: str

# JSON 파일에서 사용자 정보 로드
def load_users():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "fake_db.json")
    with open(db_path, "r") as f:
        data = json.load(f)
    return data["users"]

@app.post("/login")
def login(login_req: LoginRequest):
    try:
        users = load_users()
        for user in users:
            if user["username"] == login_req.username and user["password"] == login_req.password:
                return {"message": "Login success!"}
        raise HTTPException(status_code=401, detail="Invalid username or password")
    except Exception as e:
        print("로그인 처리 중 오류 발생:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
