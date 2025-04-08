from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_jwt_secret"  # 🚨 실서비스에선 더 안전하게 보관해야 함
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def create_jwt(payload: dict) -> str:
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
