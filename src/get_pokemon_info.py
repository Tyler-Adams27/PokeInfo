"""
The base Pokemon class with functions to call the Pokemon API.
"""

import requests
import global_var

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
        self.pokemon_exists = True

    def get_pokemon_info(self, pokemon):
        print("Calling Pokemon API")
        base_url = "https://pokeapi.co/api/v2/"

        pokemon_info_request_url = requests.get(f"{base_url}pokemon/{pokemon}")
        if pokemon_info_request_url.status_code != 200:
            global_var.POKEMON_EXISTS = False
            return None

        else:
            global_var.POKEMON_EXISTS = True
            return pokemon_info_request_url.json()
