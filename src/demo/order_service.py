from demo.order_repo import Order
from demo.order_repo import OrderRepo
from mold import singleton


@singleton()
class OrderService:
    def __init__(self, order_repo: OrderRepo):
        self._order_repo = order_repo

    def get_order(self, id: str) -> Order:
        return self._order_repo.get_order(id)
