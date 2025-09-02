import pytest

@pytest.mark.stage03
def test_hello_person_returns_yamada():
    from kadai import hello_person

    assert hello_person("Yamada") == "Hello, Yamada!"

@pytest.mark.stage03
def test_hello_person_returns_tanaka():
    from kadai import hello_person

    assert hello_person("Tanaka") == "Hello, Tanaka!"