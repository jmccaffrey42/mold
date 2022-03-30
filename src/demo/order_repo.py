import abc
from dataclasses import dataclass

from mold import singleton


class SqlSession:
    pass


@dataclass
class Order:
    id: str


class OrderRepo(abc.ABC):
    def get_order(self, id: str) -> Order:
        raise NotImplementedError()

    def save(self, order: Order):
        raise NotImplementedError()


@singleton()
class InMemoryOrderRepo(OrderRepo):
    def __init__(self):
        self._orders = dict()

    def get_order(self, id: str) -> Order:
        return self._orders.get(id)

    def save(self, order: Order):
        self._orders[order.id] = order


@singleton(primary=True)
class SqlOrderRepo(OrderRepo):
    def __init__(self, session: SqlSession):
        self._session = session

    def get_order(self, id: str) -> Order:
        pass

    def save(self, order: Order):
        pass
