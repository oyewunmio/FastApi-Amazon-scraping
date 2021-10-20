from fastapi import FastAPI
from typing import Optional

from controllers import main

app = FastAPI()

@app.get('/list_products')
def list_products(is_best_seller: Optional[bool] = None, rating: Optional[float] = None, product_name: Optional[str]=None):
    """Returns a list with all products in the page with optional filters"""
    return main.list_products(is_best_seller=is_best_seller, rating=rating, product_name=product_name)

