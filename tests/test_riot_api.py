import allure
import requests


class TestRiotAPI:
    @allure.title("Проверка авторизации без API-ключа")
    def test_riot_api_1(self, base_url):
        with allure.step("Формирование и отправка запроса"):
            summoner_name = "wonderk1d"
            url = f"{base_url}/summoner/v4/summoners/by-name/{summoner_name}"
            response = requests.get(url)

        with allure.step("Проверка ответа"):
            assert response.status_code == 401
            assert response.json()['status']['message'] == 'Unauthorized'


    @allure.title("Проверка успешной авторизации с API-ключом и получение данных об игроке")
    def test_riot_api_2(self, riot_api_key, base_url):
        with allure.step("Формируем и отправляем запрос"):
            tag_line = 3113
            game_name = 'fr3aktrgt'
            api_endpoint = f'/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
            url = f'{base_url}{api_endpoint}?api_key={riot_api_key}'
            response = requests.get(url)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            puuid = response.json()['puuid']
            assert puuid == '-OS_Gch3BD4fGLaumoTkHh-gy4F9WpxaW27HSxsnwToVoaKjbUJpRhAKRayKP9cROjHe55CWK0y0Jg'
            assert response.json()['gameName'] == game_name
            assert response.json()['tagLine'] == str(tag_line)

        with allure.step("Формируем и отправляем запрос"):
            api_endpoint = f'/riot/account/v1/accounts/by-puuid/{puuid}'
            url = f'{base_url}{api_endpoint}?api_key={riot_api_key}'
            response = requests.get(url)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert response.json()['puuid'] == puuid
            assert response.json()['gameName'] == game_name
            assert response.json()['tagLine'] == str(tag_line)

    def test_riot_api_3(self, riot_api_key, base_url):

