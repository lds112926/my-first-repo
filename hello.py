#!/usr/bin/env python3
"""A minimal Python Hello World program."""


def greet(name: str = "World") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
