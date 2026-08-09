from PyQt6.QtWidgets import QPushButton, QMessageBox
from PyQt6 import QtWidgets

"""
Popups:

When a pokemon does not exist.
When user attempts to search an empty string.

"""

def pokemon_does_not_exist(name):
    if name == "":
        window = QMessageBox()
        window.setText(f"Please enter a pokemon name.")
        window.setWindowTitle("Info")
        window.setIcon(QMessageBox.Icon.Information)
    else:
        window = QMessageBox()
        window.setText(f"The Pokemon {name} does not exist. Please try again.")
        window.setWindowTitle("Info")
        window.setIcon(QMessageBox.Icon.Information)
    window.exec()

