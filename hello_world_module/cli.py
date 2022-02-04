from typing import Optional

from .utils import hello
from .settings import DEFAULT_HELLO


class CLI:

    @staticmethod
    def run(name: Optional[str] = None) -> str:
        return hello(name=name or DEFAULT_HELLO)
