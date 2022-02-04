import os
import fire
from typing import Optional


DEFAULT_HELLO = os.environ.get(
    "DEFAULT_HELLO",
    default="World"
)


def hello(name: Optional[str] = None) -> str:
    name = name or DEFAULT_HELLO
    return f"Hello, {name}!"


class CLI:

    @staticmethod
    def run(name: Optional[str] = None) -> str:
        return hello(name=name)


if __name__ == "__main__":
    fire.Fire(CLI)
