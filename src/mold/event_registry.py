from collections import defaultdict
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

from mold.util import Singleton


class EventRegistry(Singleton):
    _events: Dict[type, List[Callable]]

    def __init__(self):
        self._events = defaultdict(list)

    def register(self, event: type, handler: Callable):
        self._events[event].append(handler)

    def get_handlers(self, event: type) -> List[Callable]:
        return self._events[event]