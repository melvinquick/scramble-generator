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

        self.setWindowTitle("Scramble Generator")
        self.setMinimumSize(360, 100)
        self.setWindowIcon(QIcon(icon))

        page = QVBoxLayout()
        inputs = QHBoxLayout()

        button = QPushButton("Generate Scramble")
        button.setStyleSheet(
            "background-color: #44475a; color: #bd93f9;"
            "border: 1px solid #6272a4; border-radius: 4px;"
            "padding: 8px 16px; cursor: pointer;"
        )

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(["2x2", "3x3"])
        self.puzzle_type.setCurrentIndex(1)
        self.puzzle_type.setStyleSheet(
            "background-color: #383c44; color: #f8f8f2;"
            "border: 1px solid #6272a4; border-radius: 4px;"
            "padding: 4px 8px;"
        )

        self.num_moves = QSpinBox()
        self.num_moves.setRange(9, 130)
        self.num_moves.setValue(25)
        self.num_moves.lineEdit().setReadOnly(True)
        self.num_moves.setStyleSheet(
            "background-color: #383c44; color: #f8f8f2;"
            "border: 1px solid #6272a4; border-radius: 4px;"
            "padding: 4px 8px;"
        )

        self.scramble = QLabel()
        self.scramble.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )
        self.scramble.setStyleSheet("color: #f8f8f2;")

        inputs.addWidget(button)
        inputs.addWidget(self.puzzle_type)
        inputs.addWidget(self.num_moves)

        page.addLayout(inputs)
        page.addWidget(self.scramble)

        button.pressed.connect(self.get_moves)

        gui = QWidget()
        gui.setLayout(page)

        self.setCentralWidget(gui)
        self.setStyleSheet(
            "background-color: #282a3c;"
        )

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
