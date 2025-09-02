import pytest

@pytest.mark.stage01
def test_hello_world_exists():
    from kadai import hello_world

    assert hello_world() == "Hello, World!"