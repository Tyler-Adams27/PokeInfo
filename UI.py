import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QFont
from get_pokemon_info import *

app = QApplication([])
window = QWidget()
window.setWindowTitle("PokeAPI")
window.setGeometry(1000, 1000, 1280, 720)

title = QLabel("PokeAPI", parent=window)
title.setFont(QFont("Arial", 30))
title.move(580, 50)

info_text = QLabel("Enter a Pokemon's name below to grab its stats!", parent=window)
info_text.move(500, 100)

pokemon_name_input = QLineEdit("", parent=window)
pokemon_name_input.move(580, 150)

search_button = QPushButton("Search!", parent=window)
search_button.move(605, 200)

pokemon_shiny_front = QLabel(parent=window)
pokemon_shiny_front.setGeometry(540, 250, 200, 200)
pokemon_shiny_front.setScaledContents(True)

pokemon_normal_front = QLabel(parent=window)
pokemon_normal_front.setGeometry(540, 250, 200, 200)
pokemon_normal_front.setScaledContents(True)

def search():
    pokemon = Pokemon(pokemon_name_input.text())
    try:
        response = requests.get(pokemon.pokemon_sprite_shiny)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        pokemon_shiny_front.setPixmap(pixmap)

    except Exception as e:
        print(f"Error loading image: {e}")
        pokemon_shiny_front.setText("Image not found.")



window.show()
sys.exit(app.exec())
