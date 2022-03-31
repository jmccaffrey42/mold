import pytest

from mold import BeanRegistry
from mold import scan_beans


@pytest.fixture(autouse=True)
def fresh_registry():
    BeanRegistry.clear()
    yield BeanRegistry.get()


@pytest.fixture()
def demo_beans():
    scan_beans('demo')


