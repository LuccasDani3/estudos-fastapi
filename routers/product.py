from fastapi import APIRouter, Depends

from schemas.product import ProductCreate

from services.product_service import ProductService, get_product_service

router = APIRouter(
    prefix="/products",
    tags=["Produtos"]
)

@router.post('/')
def list_products(
    product: ProductCreate,
    service: ProductService = Depends(get_product_service)):
    return service.create(product)


@router.get('/')
def create_product(
        min_price: float | None = None,
        max_price: float | None = None,
        service: ProductService = Depends(get_product_service)
        ):

    return service.list(min_price, max_price)


@router.get('/{product_id}')
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)):

    return service.get_by_id(product_id)