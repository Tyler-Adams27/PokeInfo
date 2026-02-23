from PyQt6.QtWidgets import QPushButton, QMessageBox
from PyQt6 import QtWidgets


def pokemon_does_not_exist(name):
    window = QMessageBox()
    window.setText(f"The Pokemon '{name}' does not exist. Please try again.")
    window.setWindowTitle("Info")
    window.setIcon(QMessageBox.Icon.Information)

    window.exec()

