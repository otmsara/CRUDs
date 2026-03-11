from fastapi import FastAPI

app = FastAPI()

products = {
    1: {
        "name": "Laptop",
        "price": 1000
        },
    2: {
        "name": "phone",
        "price": 500
        }
}

# e-commerce store CRUD

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    if product_id in products :
            return products[product_id] 
    return {"Data": "Not found"}
       
@app.post("/products/{product_id}")
def create_product(product_id: int, name: str, price: float):
    if product_id in products:
        return {"Data": "Product already exists"}
    products[product_id] = {"name": name, "price": price}
    return products[product_id]
     
    
