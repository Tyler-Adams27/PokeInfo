from get_pokemon_info import Pokemon


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

    def get_stats(self):
        temp_pokemon = Pokemon(self.pokemon)
        info_temp = temp_pokemon.get_pokemon_info()
        if info_temp is None:
            print("Couldn't fetch stats.")
            return None
        else:
            self.hp = info_temp["stats"][0]["base_stat"]
            self.attack = info_temp["stats"][1]["base_stat"]
            self.defense = info_temp["stats"][2]["base_stat"]
            self.special_attack= info_temp["stats"][3]["base_stat"]
            self.special_defence = info_temp["stats"][4]["base_stat"]
            self.speed = info_temp["stats"][5]["base_stat"]
            self.height = info_temp["height"]
            self.weight = info_temp["weight"]
            self.total = int(self.hp) + int(self.attack) + int(self.defense) + int(self.special_attack) + int(self.special_defence) + int(self.speed)

            return None

test = StatFetcher(pokemon="ditto")
test.get_stats()