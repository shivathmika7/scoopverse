from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from bson import ObjectId

from database import products_collection


app = FastAPI(title="ScoopVerse API")


# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Product Model
# -----------------------------

class Product(BaseModel):
    name: str
    category: str
    description: str
    price: float = Field(gt=0)
    image: str
    stock: int = Field(ge=0)


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to ScoopVerse 🍦"
    }


# -----------------------------
# Get All Products
# -----------------------------

@app.get("/products")
def get_products():

    products = list(
        products_collection.find()
    )

    for product in products:
        product["_id"] = str(product["_id"])

    return products


# -----------------------------
# Add Product
# -----------------------------

@app.post("/products")
def add_product(product: Product):

    result = products_collection.insert_one(
        product.model_dump()
    )

    return {
        "message": "Ice cream added successfully!",
        "id": str(result.inserted_id)
    }


# -----------------------------
# Get One Product
# -----------------------------

@app.get("/products/{product_id}")
def get_product(product_id: str):

    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid product ID"
        )

    product = products_collection.find_one(
        {"_id": ObjectId(product_id)}
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product["_id"] = str(product["_id"])

    return product