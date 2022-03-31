import abc
from dataclasses import dataclass


@dataclass
class Order:
    id: str


class OrderRepo(abc.ABC):
    def get_order(self, id: str) -> Order:
        raise NotImplementedError()

    def save(self, order: Order):
        raise NotImplementedError()
