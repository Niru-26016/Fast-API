from fastapi import FastAPI
from model import product
app= FastAPI()

@app.get("/")
def greet():
    return (f"Hello, niru!")

products=[
    product(id=1,name="phone",price=99.99),
    product(id=2,name="bag",price=49.99),
    product(id=4,name="book",price=9.99)
]

@app.get("/products")
def getAllProducts():
    return products 

@app.get("/product/{id}")
def getProduct(id: int):
    for product in products:
        if(product.id==id):
            return product
    return "Product not found"

@app.post("/product")
def addProduct(product:product):
    products.append(product)
    return product

@app.put("/product")
def editproduct(id: int ,product:product):
    for i in range (len(products)):
        if(products[i].id==id):
            products[i]=product;
            return "product updated successfully"
    return "Product not found"

@app.delete("/products")
def deleteProduct(id:int):
    for i in range(len(products)):
        if(products[i].id==id):
            del products[i];
            return "Product Deleted"
    return "product not found"




