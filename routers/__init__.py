from.user import router as users_router
from.product import router as products_router

routers = [
    users_router,
    products_router
]

def register_routers(app):
    for route in routers:
        app.include_router(route)