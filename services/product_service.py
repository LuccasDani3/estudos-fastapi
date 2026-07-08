from repositories.product_repository import ProductRepository

from schemas.product import ProductCreate

class ProductService:
    def __init__(self, repository):
        self.repository = repository


    def create(
        self,
        product: ProductCreate,
    ):
        return self.repository.create(product)
    

    def list(
        self,
        min_price: float | None,
        max_price: float | None,
    ):
        return self.repository.list(min_price, max_price)
    

    def get_by_id(
        self,
        product_id: int,
    ):
        return self.repository.get_by_id(product_id)
    

    def update(self, product_id: int):
        pass
    

    def delete(self, product_id: int):
        pass

        
def get_product_service():
    repository = ProductRepository()
    service = ProductService(repository)
    return service