import pytest

@pytest.fixture(scope="module", autouse=True)
def base_url():
    return "https://pokeapi.co/api/v2/"


