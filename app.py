import sys, os
import functions

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QComboBox,
    QHBoxLayout,
    QSpinBox,
)

basedir = os.path.dirname(__file__)
icon = os.path.join(basedir, "images/logo-512x512.ico")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup window title
        self.setWindowTitle("Scramble Generator")

        # Set minimum window size
        self.setMinimumSize(360, 100)

        # Set window icon to logo
        self.setWindowIcon(QIcon(icon))

        # Setup page layout and create widgets
        page = QVBoxLayout()
        inputs = QHBoxLayout()

        button = QPushButton("Generate Scramble")

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(["2x2", "3x3"])
        self.puzzle_type.setCurrentIndex(1)

        self.num_moves = QSpinBox()
        self.num_moves.setRange(9, 130)
        self.num_moves.lineEdit().setReadOnly(True)

        self.scramble = QLabel()
        self.scramble.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        inputs.addWidget(button)
        inputs.addWidget(self.puzzle_type)
        inputs.addWidget(self.num_moves)

        page.addLayout(inputs)
        page.addWidget(self.scramble)

        # Connect button to function to get scramble moves
        button.pressed.connect(self.get_moves)

        # Create dummy widget to hold layout and then set the central widget to the dummy widget
        gui = QWidget()
        gui.setLayout(page)

        self.setCentralWidget(gui)

    # Function for getting the moves for the output by making use of moves() in functions.py
    def get_moves(self):
        self.scramble.setText(
            functions.moves(self.num_moves.value(), self.puzzle_type.currentText())
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
