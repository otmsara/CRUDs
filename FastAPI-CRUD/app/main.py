# E-commerce store CRUD

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
class Product(BaseModel):
    name: str
    price: float

class UpdateProduct(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

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


# Get all products
@app.get("/products")
def get_all_products():
    return products

# Get one product by its id
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    if product_id in products :
            return products[product_id] 
    return {"Data": "Not found"}
       
# Create a product
@app.post("/products/{product_id}")
def create_product(product_id: int, name: str, price: float):
    if product_id in products:
        return {"Data": "Product already exists"}
    products[product_id] = {"name": name, "price": price}
    return products[product_id]

# Update a product
@app.put("/products/{product_id}")
def update_product(product_id: int, update_product: UpdateProduct):
    if product_id in products:
        current_product = products[product_id]
        if update_product.name is not None:
            current_product["name"] = update_product.name
        if update_product.price is not None:
            current_product["price"] = update_product.price
        return current_product
    return {"Data": "Not Found"}
         
# Delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id in products:
        del products[product_id]
        return {"Data": "Product deleted successfully"}
    return {"Data": "Product not found"}