from fastapi import FastAPI
import json

app = FastAPI()

def load_products():
    with open("app/product_data.json", "r") as f:
        data = json.load(f)
    return data["products"]

@app.get("/products")
def get_all_products():
    products = load_products()
    return {"products": products}
