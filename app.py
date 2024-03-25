# --- Libraries --- #

import sys
import functions

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup window title
        self.setWindowTitle("Scramble Generator")

        # Setup page layout
        page = QVBoxLayout()
        button = QPushButton("Generate Scramble")
        self.scramble = QLabel()
        self.scramble.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        page.addWidget(button)
        page.addWidget(self.scramble)

        # Connect button to function to get scramble moves
        button.pressed.connect(self.get_moves)

        # Create dummy widget to hold layout and then set the central widget to the dummy widget
        gui = QWidget()
        gui.setLayout(page)

        self.setCentralWidget(gui)

    def get_moves(self):
        self.scramble.setText(functions.moves())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
