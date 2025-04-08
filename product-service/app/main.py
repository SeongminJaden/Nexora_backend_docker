from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from typing import List, Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

SECRET_KEY = "your_jwt_secret"
ALGORITHM = "HS256"

class CategoryRequest(BaseModel):
    categories: List[str]

@app.post("/categories")
async def receive_categories(
    request: CategoryRequest,
    authorization: Optional[str] = Header(None)
):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        print(f"✅ 토큰 검증 성공! 사용자 ID: {user_id}")
        print(f"✅ 선택된 카테고리: {request.categories}")
        return {"message": "카테고리 수신 성공"}
    except JWTError as e:
        print(f"❌ 토큰 검증 실패: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid JWT token")

@app.get("/creators")
async def get_creators(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        print(f"✅ 토큰 검증 성공! 사용자 ID: {user_id}")

        # JSON 파일에서 작가 리스트 불러오기
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "creators.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return JSONResponse(content=data)
    except JWTError as e:
        print(f"❌ 토큰 검증 실패: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid JWT token")
