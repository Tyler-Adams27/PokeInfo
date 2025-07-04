import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QFont, QMovie

import links
from get_pokemon_info import *
from pokemon_image_fetcher import PokemonImage
from pokemon_stat_fetcher import StatFetcher
from links import open_github, open_linkedin

app = QApplication([])
window = QWidget()
window.setWindowTitle("PokeInfo")
window.setFixedSize(1280, 720)
title = QLabel("<b>PokeInfo</b>", parent=window)
title.setFont(QFont("Arial", 30))
title.move(580, 50)
prompt_text = QLabel("<i>Enter a Pokemon's name below to grab its stats!</i>", parent=window)
prompt_text.move(500, 100)
stats_info = QLabel(f"<b>Statistics:</b>", parent=window)
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
total_stat.move(10, 190)
weight_stat = QLabel("Weight =             ", parent=window)
weight_stat.move(10, 150)
height_stat = QLabel("Height =             ", parent=window)
height_stat.move(10, 170)
pokemon_name_input = QLineEdit("ditto", parent=window)
pokemon_name_input.move(580, 150)
pokemon_shiny_front = QLabel(parent=window)
pokemon_shiny_front.setGeometry(5, 450, 200, 200)
pokemon_shiny_front.setScaledContents(True)
pokemon_normal_front = QLabel(parent=window)
pokemon_normal_front.setGeometry(5, 250, 200, 200)
pokemon_normal_front.setScaledContents(True)
pokemon_normal_back = QLabel(parent=window)
pokemon_normal_back.setGeometry(200, 250, 200, 200)
pokemon_normal_back.setScaledContents(True)
pokemon_shiny_back = QLabel(parent=window)
pokemon_shiny_back.setGeometry(200, 450, 200, 200)
pokemon_shiny_back.setScaledContents(True)

stats_info = QLabel(f"Made By Tyler Adams.", parent=window)
stats_info.move(1135,698)

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

        image_url_shiny_back = pokemon_images.get_shiny_image_back()
        response_shiny_back = requests.get(image_url_shiny_back)
        response_shiny_back.raise_for_status()

        pixmap = QPixmap()
        pixmap.loadFromData(response_shiny_back.content)
        pokemon_shiny_back.setPixmap(pixmap)

        image_url_normal_back = pokemon_images.get_normal_image_back()
        response_normal_back = requests.get(image_url_normal_back)
        response_normal_back.raise_for_status()

        pixmap = QPixmap()
        pixmap.loadFromData(response_normal_back.content)
        pokemon_normal_back.setPixmap(pixmap)

    except Exception as e:
        print(f"Error loading image: {e}")
        pokemon_shiny_front.setText("Pokemon not found.")
        pokemon_normal_front.setText("Pokemon not found.")
        pokemon_normal_back.setText("Pokemon not found.")
        pokemon_shiny_back.setText("Pokemon not found.")
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
    weight_stat.setText(f"Weight = {pokemon_stats.weight}")
    height_stat.setText(f"Height = {pokemon_stats.height}")

def full_search():
    search_stats()
    search_images()

search_button = QPushButton("Search!", parent=window)
search_button.move(605, 200)
search_button.pressed.connect(full_search)

github_button = QPushButton(" My GitHub ", parent=window)
github_button.move(1150, 660)
github_button.pressed.connect(links.open_github)

linkedin_button = QPushButton("My LinkedIn", parent=window)
linkedin_button.move(1150, 630)
linkedin_button.pressed.connect(links.open_linkedin)

pfp_image = QPixmap("pfp.png")
pfp = QLabel(parent=window)
pfp.setGeometry(1150, 520, 100, 100)
pfp.setScaledContents(True)
pfp.setPixmap(pfp_image)



window.show()
sys.exit(app.exec())
