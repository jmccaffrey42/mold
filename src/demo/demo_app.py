from dataclasses import dataclass

from demo.order_repo import SqlSession
from demo.order_service import OrderService
from mold import BeanContext
from mold import BeanRegistry
from mold import EventRegistry
from mold import event_handler
from mold import factory


@dataclass
class DemoEvent:
    msg: str


@event_handler()
def demo_order_handler_foo(event: DemoEvent, order_service: OrderService):
    print('FOO')
    return order_service.get_order('test')


@event_handler()
def demo_order_handler_bar(event: DemoEvent, order_service: OrderService):
    print('BAR')
    return order_service.get_order('test')


def handle_event(event):
    for handler in EventRegistry.get().get_handlers(type(event)):
        handler(event)


def main():
    use_sql = True

    with BeanContext():
        if use_sql:
            @factory()
            def sql_session_factory() -> SqlSession:
                return SqlSession()

        BeanRegistry.get().dump()

        event = DemoEvent(msg="test")
        handle_event(event)


if __name__ == '__main__':
    main()
