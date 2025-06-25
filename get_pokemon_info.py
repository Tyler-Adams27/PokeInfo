import requests
import sys


class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.attack = 0
        self.spattack = 0
        self.defense = 0
        self.spdefence = 0
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
            sys.exit(0)
        else:
            return pokemon_info_request_url

    def sort_pokemon_info(self):
        temp_info = self.get_pokemon_info()
        self.pokemon_info = temp_info.json()
        self.pokemon_sprite_shiny = self.pokemon_info["sprites"]["front_shiny"]
        print(self.pokemon_sprite_shiny)




    def sort_pokemon_stats(self):
        pass

    def sort_pokemon_types(self):
        pass




