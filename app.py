import sys, os, functions

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

        self.theme = "light"
        self.set_theme()

        self.page = QVBoxLayout()
        self.inputs = QHBoxLayout()

        self.button = QPushButton("Generate Scramble")
        self.apply_theme(self.button)

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(["2x2", "3x3"])
        self.puzzle_type.setCurrentIndex(1)
        self.apply_theme(self.puzzle_type)

        self.num_moves = QSpinBox()
        self.num_moves.setRange(9, 130)
        self.num_moves.setValue(25)
        self.num_moves.lineEdit().setReadOnly(True)
        self.apply_theme(self.num_moves)

        self.theme_toggle = QPushButton("Dark Mode")
        self.apply_theme(self.theme_toggle)

        self.scramble = QLabel()
        self.scramble.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )
        self.apply_theme(self.scramble)

        self.inputs.addWidget(self.button)
        self.inputs.addWidget(self.puzzle_type)
        self.inputs.addWidget(self.num_moves)
        self.inputs.addWidget(self.theme_toggle)

        self.page.addLayout(self.inputs)
        self.page.addWidget(self.scramble)

        self.button.pressed.connect(self.get_moves)
        self.theme_toggle.pressed.connect(self.toggle_theme)
        self.puzzle_type.currentTextChanged.connect(self.set_default_num_moves)

        self.gui = QWidget()
        self.gui.setLayout(self.page)

        self.setCentralWidget(self.gui)

        self.toggle_theme()  # This is done to make issue of text shifting in num_moves after first theme_toggle not noticeable

    def set_theme(self):
        if self.theme == "dark":
            self.theme_stylesheet = """
                background-color: #1c1c1c;
                color: #d0d0d0;
                border: 1px solid #585858;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
        elif self.theme == "light":
            self.theme_stylesheet = """
                background-color: #eeeeee;
                color: #444444;
                border: 1px solid #bcbcbc;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """

    def apply_theme(self, widget):
        widget.setStyleSheet(self.theme_stylesheet)

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.set_theme()
        self.apply_theme(self)
        # Apply theme to all child widgets
        for widget in self.findChildren(QWidget):
            self.apply_theme(widget)
        if self.theme == "dark":
            self.theme_toggle.setText("Dark Mode")
        else:
            self.theme_toggle.setText("Light Mode")

    def get_moves(self):
        self.scramble.setText(
            functions.moves(self.num_moves.value(), self.puzzle_type.currentText())
        )

    def set_default_num_moves(self):
        match self.puzzle_type.currentText():
            case "2x2":
                self.num_moves.setValue(9)
            case "3x3":
                self.num_moves.setValue(25)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
