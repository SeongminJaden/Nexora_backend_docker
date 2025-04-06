# 🧩 FastAPI 마이크로서비스 예제

이 프로젝트는 **FastAPI 기반 마이크로서비스 아키텍처**를 사용하여 다음과 같은 서비스를 제공합니다:

1. 🔐 로그인 서비스  
2. 📦 DB 조회 서비스 (위시리스트, 장바구니, 구매 내역)  
3. 🛒 상품 리스트 서비스  
4. 💳 결제 서비스  

모든 서비스는 **Docker**를 이용해 컨테이너화 되어 있으며, `docker-compose`를 통해 통합 실행됩니다.

---

## 📁 프로젝트 구조
```
project-root/
├── docker-compose.yml
├── login-service/
│   ├── app/
│   │   ├── fake_db.json
│   │   └── main.py
│   └── Dockerfile
├── user-db-service/
│   ├── app/
│   │   ├── fake_user_data.json
│   │   └── main.py
│   └── Dockerfile
├── product-service/
│   ├── app/
│   │   ├── fake_product_data.json
│   │   └── main.py
│   └── Dockerfile
└── payment-service/
├── app/
│   └── main.py
└── Dockerfile
```


---

## 🐳 실행 방법

### 1. Docker 빌드 및 실행

```bash
docker-compose up --build
```
모든 서비스가 실행되며, 각각의 FastAPI 서버가 컨테이너에서 작동합니다.
🌐 서비스 엔드포인트

| 서비스명	| 포트	| Swagger UI 주소 |
|----------|----|---------------|
| 로그인 서비스 |	8000	| http://localhost:8000/docs |
| DB 조회 서비스 |	8001	| http://localhost:8001/docs |
| 상품 리스트 서비스 |	8002	| http://localhost:8002/docs |
| 결제 서비스 |	8003	| http://localhost:8003/docs |


## 🔍 테스트 예시
### ✅ 로그인 요청

```bash
curl -X POST http://localhost:8000/login \
-H "Content-Type: application/json" \
-d '{"username": "seongmin", "password": "1234"}'
```
### ✅ DB 조회

```bash
curl http://localhost:8001/user/seongmin
```
### ✅ 상품 리스트 조회
```bash
curl http://localhost:8002/products
```
### ✅ 결제 요청

```bash
curl -X POST http://localhost:8003/pay \
-H "Content-Type: application/json" \
-d '{"username": "seongmin"}'
```
### 📝 참고사항
데이터베이스는 현재 각 서비스 내부에 존재하는 JSON 파일을 임시 DB로 사용합니다.

실제 서비스 연결 시 다음 항목들이 추가될 수 있습니다:

- JWT 인증 시스템
- 실 데이터베이스(PostgreSQL, MongoDB 등)
- API Gateway
- 서비스 간 메시지 브로커 (Kafka, RabbitMQ 등)

### 📝 Swager UI 사용방법 
![{F0272E62-C3B8-4285-8995-9E5BD313453A}](https://github.com/user-attachments/assets/67d1495a-7269-48f9-85a9-d8e21b9c99a8)
API엔드포인트를 SwagerUI에서 확인할 수 있습니다.

##🔄 개발 중 Docker 반영 방법

```bash
docker-compose down
docker-compose up --build
```
## 💡 TODO (확장 아이디어)
- JWT 기반 인증 시스템
- PostgreSQL 또는 MongoDB 연동
- Kafka 또는 RabbitMQ로 서비스 간 메시징
- API Gateway 통합
- 서비스 헬스 체크 & 모니터링
