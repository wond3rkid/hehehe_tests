import requests

base_url = 'https://europe.api.riotgames.com'
riot_api_key = 'RGAPI-d5f6f048-a42a-4451-bb18-272da869e0f8'


class TestRiotAPI:
    def test_riot_api_1(self):
        summoner_name = "wonderk1d"
        url = f"{base_url}/summoner/v4/summoners/by-name/{summoner_name}"
        response = requests.get(url)
        assert response.status_code == 401
        assert response.json()['status']['message'] == 'Unauthorized'

    def test_riot_api_2(self):
        tag_line = 3113
        game_name = 'fr3aktrgt'
        api_endpoint = f'/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
        url = f'{base_url}{api_endpoint}?api_key={riot_api_key}'
        response = requests.get(url)

        assert response.status_code == 200
        puuid = response.json()['puuid']
        assert puuid == '-OS_Gch3BD4fGLaumoTkHh-gy4F9WpxaW27HSxsnwToVoaKjbUJpRhAKRayKP9cROjHe55CWK0y0Jg'
        assert response.json()['gameName'] == game_name
        assert response.json()['tagLine'] == str(tag_line)
        print(f'response for first request {response.json()}')

        api_endpoint = f'/riot/account/v1/accounts/by-puuid/{puuid}'
        url = f'{base_url}{api_endpoint}?api_key={riot_api_key}'
        response = requests.get(url)

        assert response.status_code == 200
        assert response.json()['puuid'] == puuid
        assert response.json()['gameName'] == game_name
        assert response.json()['tagLine'] == str(tag_line)
        print(f'response for second request {response.json()}')
