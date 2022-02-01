import os
from typing import Optional

import fire

HELLO_DEFAULT = os.environ.get(
    "HELLO_DEFAULT",
    default="World"
)


class Main:

    @staticmethod
    def run(name: Optional[str] = None):
        name = name or HELLO_DEFAULT
        print(f"Hello {name}!")


if __name__ == "__main__":
    fire.Fire(Main)
