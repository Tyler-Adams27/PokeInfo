from get_pokemon_info import Pokemon



class PokemonImage:
    def __init__(self, pokemon_json):
        self.hello = "hello"

    def get_normal_image(self, pokemon):
        if pokemon is None:
            return None
        else:
            pokemon_image_normal = pokemon["sprites"]["front_default"]
            return pokemon_image_normal

    def get_shiny_image(self, pokemon):

        if pokemon is None:
            return None
        else:
            pokemon_image_shiny = pokemon["sprites"]["front_shiny"]
            return pokemon_image_shiny

    def get_shiny_image_back(self, pokemon):
 
        if pokemon is None:
            return None
        else:
            pokemon_image_shiny_back = pokemon["sprites"]["back_shiny"]
            return pokemon_image_shiny_back

    def get_normal_image_back(self, pokemon):

        if pokemon is None:
            return None
        else:
            pokemon_image_normal_back = pokemon["sprites"]["back_default"]
            return pokemon_image_normal_back