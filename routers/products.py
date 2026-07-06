from fastapi import APIRouter

from schemas.product import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Produtos"]
)


@router.get('/')
def get_products(
        min_price: float | None = None,
        max_price: float | None = None
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


@router.get('/{id}')
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product


@router.post('/')
def create_product(product: ProductCreate):
    products.append(product.model_dump())
    return products
