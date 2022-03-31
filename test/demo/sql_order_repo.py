from demo.order_repo import Order
from demo.order_repo import OrderRepo
from mold import singleton


class SqlSession:
    pass


@singleton(primary=True)
class SqlOrderRepo(OrderRepo):
    def __init__(self, session: SqlSession):
        self._session = session

    def get_order(self, id: str) -> Order:
        pass

    def save(self, order: Order):
        pass
