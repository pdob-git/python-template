from simple_python import hello_world


def test_hello_world() -> None:
    """Test that hello_world returns the expected message."""
    assert hello_world() == "Hello, World!"


def test_hello_world_type() -> None:
    """Test that hello_world returns a string."""
    result = hello_world()
    assert isinstance(result, str)
