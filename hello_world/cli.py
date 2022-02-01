from typing import Optional

from .utils import hello_world


class CLI:

    @staticmethod
    def run(name: Optional[str] = None) -> str:
        return hello_world(name=name)
