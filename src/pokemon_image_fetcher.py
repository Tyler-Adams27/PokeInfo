from get_pokemon_info import Pokemon



class PokemonImage:
    def get_normal_image(pokemon):
        if pokemon is None:
            return None
        else:
            pokemon_image_normal = pokemon["sprites"]["front_default"]
            print("Showing Normal Front")
            return pokemon_image_normal

    def get_shiny_image(pokemon):

        if pokemon is None:
            return None
        else:
            pokemon_image_shiny = pokemon["sprites"]["front_shiny"]
            print("Showing Shiny Front")
            return pokemon_image_shiny

    def get_shiny_image_back(pokemon):
 
        if pokemon is None:
            return None
        else:
            pokemon_image_shiny_back = pokemon["sprites"]["back_shiny"]
            print("Showing Shiny Back")
            return pokemon_image_shiny_back

    def get_normal_image_back(pokemon):

        if pokemon is None:
            return None
        else:
            pokemon_image_normal_back = pokemon["sprites"]["back_default"]
            print("Showing Normal Back")
            return pokemon_image_normal_back