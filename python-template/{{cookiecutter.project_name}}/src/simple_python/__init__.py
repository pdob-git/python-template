__version__ = "0.1.0"


def hello_world() -> str:
    """Return a hello world message."""
    return "Hello, World!"


def main() -> None:
    """Main entry point for the CLI."""
    print(hello_world())
