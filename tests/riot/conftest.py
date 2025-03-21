import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def riot_api_key():
    """
    Возвращает API-ключ и проверяет его наличие.
    """
    key = os.getenv("RIOT_API_KEY")
    if not key:
        pytest.fail("RIOT_API_KEY не указан в .env")
    return key

@pytest.fixture(scope="module")
def base_url():
    return "https://europe.api.riotgames.com"

