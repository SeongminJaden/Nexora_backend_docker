import httpx

KAKAO_USER_INFO_URL = "https://kapi.kakao.com/v2/user/me"

async def verify_kakao_token(access_token: str) -> dict | None:
    headers = {"Authorization": f"Bearer {access_token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(KAKAO_USER_INFO_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ 카카오 인증 실패: {response.status_code}, {response.text}")
        return None
