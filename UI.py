import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QFont, QMovie
from get_pokemon_info import *
from pokemon_image_fetcher import PokemonImage
from pokemon_stat_fetcher import StatFetcher
app = QApplication([])
window = QWidget()
window.setWindowTitle("PokeAPI")
window.setGeometry(1000, 1000, 1280, 720)
title = QLabel("PokeAPI", parent=window)
title.setFont(QFont("Arial", 30))
title.move(580, 50)
prompt_text = QLabel("Enter a Pokemon's name below to grab its stats!", parent=window)
prompt_text.move(500, 100)
stats_info = QLabel("Stats:", parent=window)
stats_info.move(10, 10)
hp_stat = QLabel("HP =        ", parent=window)
hp_stat.move(10, 30)
attack_stat = QLabel("Attack =        ", parent=window)
attack_stat.move(10, 50)
defence_stat = QLabel("Defence =        ", parent=window)
defence_stat.move(10, 70)
sp_attack_stat = QLabel("Special Attack =        ", parent=window)
sp_attack_stat.move(10, 90)
sp_defence_stat = QLabel("Special Defence =        ", parent=window)
sp_defence_stat.move(10, 110)
speed_stat = QLabel("Speed =        ", parent=window)
speed_stat.move(10, 130)
total_stat = QLabel("Total Base =             ", parent=window)
total_stat.move(10, 150)
normal_image_text = QLabel("Normal Version:", parent=window)
normal_image_text.move(60, 280)
shiny_image_text = QLabel("Shiny Version:", parent=window)
shiny_image_text.move(60, 480)
pokemon_name_input = QLineEdit("", parent=window)
pokemon_name_input.move(580, 150)
pokemon_shiny_front = QLabel(parent=window)
pokemon_shiny_front.setGeometry(5, 450, 200, 200)
pokemon_shiny_front.setScaledContents(True)
pokemon_normal_front = QLabel(parent=window)
pokemon_normal_front.setGeometry(5, 250, 200, 200)
pokemon_normal_front.setScaledContents(True)

def search_images():
    pokemon_images = PokemonImage(pokemon_name_input.text())
    try:
        image_url_shiny = pokemon_images.get_shiny_image()
        response_shiny = requests.get(image_url_shiny)
        response_shiny.raise_for_status()

        pixmap = QPixmap()
        pixmap.loadFromData(response_shiny.content)
        pokemon_shiny_front.setPixmap(pixmap)

        image_url_normal = pokemon_images.get_normal_image()
        response_normal = requests.get(image_url_normal)
        response_normal.raise_for_status()

        pixmap = QPixmap()
        pixmap.loadFromData(response_normal.content)
        pokemon_normal_front.setPixmap(pixmap)

    except Exception as e:
        print(f"Error loading image: {e}")
        pokemon_shiny_front.setText("Pokemon not found.")
        pokemon_normal_front.setText("Pokemon not found.")

def search_stats():
    pokemon_stats = StatFetcher(pokemon_name_input.text())
    pokemon_stats.get_stats()
    hp_stat.setText(f"HP = {pokemon_stats.hp}")
    attack_stat.setText(f"Attack = {pokemon_stats.attack}")
    defence_stat.setText(f"Defence = {pokemon_stats.defense}")
    sp_attack_stat.setText(f"Special Attack = {pokemon_stats.special_attack}")
    sp_defence_stat.setText(f"Special Defence = {pokemon_stats.special_defence}")
    speed_stat.setText(f"Speed = {pokemon_stats.speed}")
    total_stat.setText(f"Total Stats = {pokemon_stats.total}")

def full_search():
    search_stats()
    search_images()

search_button = QPushButton("Search!", parent=window)
search_button.move(605, 200)
search_button.pressed.connect(full_search)


window.show()
sys.exit(app.exec())
