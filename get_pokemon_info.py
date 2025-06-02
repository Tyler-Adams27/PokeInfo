import requests
import sys



def get_pokemon_info():
    base_url = "https://pokeapi.co/api/v2/"
    pokemon_name = input("Pokemon Name ")
    pokemon_info_request_url = requests.get(f"{base_url}pokemon/{pokemon_name}")
    if pokemon_info_request_url.status_code != 200:
        print(f"Unable to get data. Error {pokemon_info_request_url.status_code} please try again.")
        sys.exit(0)
    else:
        return pokemon_info_request_url

def sort_pokemon_info(pokemon_info):
    pokemon_name_temp = pokemon_info["name"]
    pokemon_name = pokemon_name_temp.capitalize()
    pokemon_height_temp = pokemon_info["height"]
    pokemon_height = float(pokemon_height_temp) / 10
    print("")
    print(f"Information about {pokemon_name}:")
    print("")
    print(f"It's ID number is {pokemon_info["id"]}.")
    print(f"It's height is {pokemon_height}m.")
    print(f"It's weight is {pokemon_info["weight"]}kg.")

def sort_pokemon_stats(pokemon_info):
    stats = pokemon_info["stats"]
    print("")
    print("Base Stats:")
    print("")
    print(f"It's base HP is {stats[0]["base_stat"]}.")
    print(f"It's base attack is {stats[1]["base_stat"]}.")
    print(f"It's base defence is {stats[2]["base_stat"]}.")
    print(f"It's base SP-Attack is {stats[3]["base_stat"]}.")
    print(f"It's base SP-Defense is {stats[4]["base_stat"]}.")
    print(f"It's base speed is {stats[5]["base_stat"]}.")

def sort_pokemon_types(pokemon_info):
    types = pokemon_info["types"]
    print("")
    if len(types) > 1:
        print(f"It is a {types[0]["type"]["name"]} and {types[1]["type"]["name"]} type.")
    else:
        print(f"It is a {types[0]["type"]["name"]} type.")




def main():
    pokemon_info = get_pokemon_info().json()
    sort_pokemon_info(pokemon_info)
    sort_pokemon_stats(pokemon_info)
    sort_pokemon_types(pokemon_info)




main()
