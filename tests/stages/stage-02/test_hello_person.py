import pytest

@pytest.mark.stage02
def test_hello_person_exists():
    from kadai import hello_person

    assert hello_person() == "Hello, World!"
