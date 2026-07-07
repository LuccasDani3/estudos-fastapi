from fastapi import HTTPException

from schemas.product import ProductCreate

products = [
    {"name": "Mouse", "price": 25, "id": 1},
    {"name": "Teclado", "price": 150, "id": 2},
    {"name": "Monitor", "price": 799, "id": 3},
    {"name": "Notebook", "price": 2999, "id": 4}
]

class ProductRepository:
    def create(self, product: ProductCreate):
        products.append(product.model_dump())
        return product
    
    def get_by_id(self, product_id: int):
        for product in products:
            if product["id"] == product_id:
                return product

    def list(
        self, 
        min_price: float | None,
        max_price: float | None
        ):
        
        filtered = products

        if min_price is not None:
            filtered = [
                p for p in filtered 
                if p["price"] >= min_price
            ]

        if max_price is not None:
            filtered = [
                p for p in filtered
                if p["price"] <= max_price
            ]
        return filtered

    def delete():
        pass

def get_product_repository():
    return ProductRepository()