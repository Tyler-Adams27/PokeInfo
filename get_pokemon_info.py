import requests

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.attack = 0
        self.special_attack = 0
        self.defense = 0
        self.special_defence = 0
        self.speed = 0
        self.pokemon_info = ""
        self.pokemon_sprite_forward = ""
        self.pokemon_sprite_backward = ""
        self.pokemon_sprite_shiny = ""

    def get_pokemon_info(self):
        base_url = "https://pokeapi.co/api/v2/"
        pokemon_name = self.pokemon_name
        pokemon_info_request_url = requests.get(f"{base_url}pokemon/{pokemon_name}")
        if pokemon_info_request_url.status_code != 200:
            print(f"Unable to get data. Error {pokemon_info_request_url.status_code} please try again.")
            return None
        else:
            return pokemon_info_request_url.json()

