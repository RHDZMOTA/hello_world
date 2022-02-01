from typing import Optional

from .settings import HELLO_DEFAULT


def hello_world(name: Optional[str] = None) -> str:
    name = name or HELLO_DEFAULT
    return f"Hello, {name}"
