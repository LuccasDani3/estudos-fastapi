products = [
    {"name": "Mouse", "price": 25, "id": 1},
    {"name": "Teclado", "price": 150, "id": 2},
    {"name": "Monitor", "price": 799, "id": 3},
    {"name": "Notebook", "price": 2999, "id": 4}
]

class ProductService:
    
    def get_all():
        return products
    
def get_product_service():
    return ProductService