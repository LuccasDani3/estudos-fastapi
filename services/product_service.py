from fastapi import Depends, HTTPException

from repositories.product_repository import ProductRepository, get_product_repository

from schemas.product import ProductCreate

class ProductService:  
    def create(
        self,
        product: ProductCreate,
        repository: ProductRepository = Depends(get_product_repository)
    ):
        return repository.create(product)
    
    def list(
        self,
        min_length: float | None,
        max_length: float | None,
        repository: ProductRepository = Depends(get_product_repository)
    ):
        return repository.list()
    
    def get(
        self,
        product_id: int,
        repository: ProductRepository = Depends(get_product_repository)
    ):
        return repository.get_by_id(product_id)

        
def get_product_service():
    return ProductService()