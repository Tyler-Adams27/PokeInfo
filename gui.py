from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QMovie, QFont
import sys
from get_pokemon_info import *





app = QApplication([])
window = QWidget()
window.setWindowTitle("PokeAPI")
window.setGeometry(1000, 1000, 1280,720)

title = QLabel("PokeAPI", parent=window)
title.setFont(QFont("Arial", 30))
title.move(580,50)
info_text = QLabel("Enter a Pokemon's name below to grab its stats!", parent=window)
info_text.move(500,100)

pokemon_name_input = QLineEdit("ditto", parent=window)
pokemon_name_input.move(580,150)

pokemon = Pokemon(pokemon_name_input.text())
pokemon.sort_pokemon_info()




search_button = QPushButton("Search!", parent=window)
search_button.move(605, 200)
search_button.clicked.connect(lambda: pokemon.get_pokemon_info())





window.show()
sys.exit(app.exec())

