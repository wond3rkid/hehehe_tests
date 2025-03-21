from pokemon.methods.work_pokemon import *


class TestPokemonDB:
    def test_pokemon_db_1(self, mocker):
        """Мокируем обращение в базу данных и возвращаемое значение"""
        pokemon_data = (2, 25, 'pikachu', 'static', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png')
        mock_conn = mocker.MagicMock()
        mock_cursor = mocker.MagicMock()
        mocker.patch("sqlite3.connect", return_value=mock_conn)
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = pokemon_data
        pokemon = get_pokemon_from_db(25)

        sqlite3.connect.assert_called_once_with("pokemon/methods/example.db")
        mock_conn.cursor.assert_called_once()

        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM pokemons WHERE pokemon_id = ?",
            (25,)
        )
        mock_conn.close.assert_called_once()
        assert pokemon == pokemon_data

    def test_pokemon_db_2(self, mocker):
        """Мокируем ответ на запрос несуществующего покемона"""
        mock_conn = mocker.MagicMock()
        mock_cursor = mocker.MagicMock()

        mocker.patch("sqlite3.connect", return_value=mock_conn)
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        result = get_pokemon_from_db(999)

        assert result is None
        mock_conn.close.assert_called_once()

    def test_pokemon_db_3(self, mocker):
        """Мокируем небезопасный запрос в базу"""
        mock_conn = mocker.MagicMock()
        mock_cursor = mocker.MagicMock()
        mocker.patch("sqlite3.connect", return_value=mock_conn)
        mock_conn.cursor.return_value = mock_cursor
        dangerous_input = "25; DROP TABLE pokemons;--"
        get_pokemon_from_db(dangerous_input)
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM pokemons WHERE pokemon_id = ?",
            (dangerous_input,)
        )