from demo.order_repo import Order
from demo.order_repo import OrderRepo
from mold import singleton


@singleton()
class InMemoryOrderRepo(OrderRepo):
    def __init__(self):
        self._orders = dict()

    def get_order(self, id: str) -> Order:
        return self._orders.get(id)

    def save(self, order: Order):
        self._orders[order.id] = order
