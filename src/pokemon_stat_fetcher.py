from get_pokemon_info import Pokemon

"""
Fetches stats from the JSON provided by the Pokemon API.
"""

class StatFetcher:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.hp = 000
        self.attack = 000
        self.defense = 000
        self.special_attack = 000
        self.special_defence = 000
        self.speed = 000
        self.total = 000
        self.weight = 000
        self.height = 000

    def get_stats(self, pokemon):
        if pokemon is None:
            print("Couldn't fetch stats.")
            return None
        else:
            self.hp = pokemon["stats"][0]["base_stat"]
            self.attack = pokemon["stats"][1]["base_stat"]
            self.defense = pokemon["stats"][2]["base_stat"]
            self.special_attack= pokemon["stats"][3]["base_stat"]
            self.special_defence = pokemon["stats"][4]["base_stat"]
            self.speed = pokemon["stats"][5]["base_stat"]
            self.height = pokemon["height"]
            self.weight = pokemon["weight"]
            self.total = int(self.hp) + int(self.attack) + int(self.defense) + int(self.special_attack) + int(self.special_defence) + int(self.speed)
            return None


