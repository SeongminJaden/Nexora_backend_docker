from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kakao_auth import verify_kakao_token
from jwt_utils import create_jwt

app = FastAPI()

class KakaoTokenRequest(BaseModel):
    access_token: str

@app.post("/login/kakao")
async def login_kakao(data: KakaoTokenRequest):
    kakao_user_info = await verify_kakao_token(data.access_token)
    
    if kakao_user_info is None:
        raise HTTPException(status_code=401, detail="Invalid Kakao token")

    # 예: email, nickname 정보 추출
    email = kakao_user_info.get("kakao_account", {}).get("email", "")
    nickname = kakao_user_info.get("kakao_account", {}).get("profile", {}).get("nickname", "")

    # JWT 생성
    jwt_token = create_jwt({"email": email, "nickname": nickname})
    print(jwt_token)
    return {"jwt": jwt_token}
