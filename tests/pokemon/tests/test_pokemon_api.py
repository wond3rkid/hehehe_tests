from tests.pokemon.methods.work_pokemon import get_pokemon_info


class TestPokemonApi:
    def test_pokemon_api_1(self, mocker):
        """Мокируем ответ от сервера с покемонами и проверяем полученные данные"""
        mock_data = {
            "name": "clefairy",
            "abilities": [
                {"ability": {"name": "cute-charm"}},
                {"ability": {"name": "magic-guard"}},
                {"ability": {"name": "friend-guard"}}
            ]
        }
        mock_response = mocker.MagicMock()
        mock_response.json.return_value = mock_data
        mocker.patch("requests.get", return_value=mock_response)
        pokemon_data = get_pokemon_info(p_id=35)
        expected_data = {
            "name": "clefairy",
            "abilities": ["cute-charm", "magic-guard", "friend-guard"]
        }
        assert pokemon_data == expected_data

    def test_pokemon_api_2(self, mocker):
        """Тест проверяет формирование URL, к которой мы обращаемся"""
        mock_get = mocker.patch('requests.get')
        get_pokemon_info("charizard")
        mock_get.assert_called_once_with("https://pokeapi.co/api/v2/pokemon/charizard")
