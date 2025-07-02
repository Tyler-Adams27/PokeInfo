from get_pokemon_info import Pokemon

class PokemonImage:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def get_normal_image(self):
        temp_pokemon = Pokemon(self.pokemon)
        info_temp = temp_pokemon.get_pokemon_info()
        if info_temp is None:
            print("Could not get image")
            return None
        else:
            pokemon_image_normal = info_temp["sprites"]["front_default"]
            return pokemon_image_normal

    def get_shiny_image(self):
        temp_pokemon = Pokemon(self.pokemon)
        info_temp = temp_pokemon.get_pokemon_info()
        if info_temp is None:
            print("Could not get image")
            return None
        else:
            pokemon_image_shiny = info_temp["sprites"]["front_shiny"]
            return pokemon_image_shiny