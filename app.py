import sys, os

from PyQt6.QtCore import Qt, QTimer, QTime
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

from scramble_generator import ScrambleGenerator

basedir = os.path.dirname(__file__)
icon = os.path.join(basedir, "images/logo-512x512.ico")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window default settings
        self.setWindowTitle("Scramble Generator")
        self.setMinimumSize(360, 100)
        self.setWindowIcon(QIcon(icon))

        # Set window default theme
        self.theme = "PaperColor-Light"
        self.set_theme()

        # Define normal variables
        self.is_running = False
        self.elapsed_time = QTime(0, 0)

        # Create end user widgets and apply settings to them
        self.scramble_button = QPushButton("Generate Scramble")

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(["2x2", "3x3"])
        self.puzzle_type.setCurrentIndex(1)

        self.num_moves = QSpinBox()
        self.num_moves.setRange(9, 130)
        self.num_moves.setValue(25)
        self.num_moves.lineEdit().setReadOnly(True)

        self.theme_picker = QComboBox()
        self.theme_picker.addItems(["PaperColor-Light", "PaperColor-Dark"])
        self.theme_picker.setCurrentIndex(1)

        self.scramble = QLabel()
        self.scramble.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        self.timer_button = QPushButton("Start Timer")

        self.timer_output = QLabel("00:00.0")
        self.timer_output.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        self.timer = QTimer()
        self.timer.interval = 10  # Milliseconds

        # Define button connections and/or actions
        self.scramble_button.pressed.connect(self.get_moves)

        self.puzzle_type.currentTextChanged.connect(self.set_default_num_moves)

        self.theme_picker.currentIndexChanged.connect(self.toggle_theme)

        self.timer_button.pressed.connect(self.toggle_timer)

        self.timer.timeout.connect(self.update_time)

        # Create layouts
        self.page = QVBoxLayout()
        self.inputs = QHBoxLayout()
        self.timer_section = QHBoxLayout()

        # Add widgets to layouts
        self.inputs.addWidget(self.scramble_button)
        self.inputs.addWidget(self.puzzle_type)
        self.inputs.addWidget(self.num_moves)
        self.inputs.addWidget(self.theme_picker)

        self.timer_section.addWidget(self.timer_button)
        self.timer_section.addWidget(self.timer_output)

        # Setup overall page layout and do one time toggle of overall window theme
        self.page.addLayout(self.inputs)
        self.page.addWidget(self.scramble)
        self.page.addLayout(self.timer_section)

        self.gui = QWidget()
        self.gui.setLayout(self.page)

        self.setCentralWidget(self.gui)

        self.toggle_theme()  # This is done to make issue of text shifting in num_moves after first theme_toggle not noticeable

    def set_theme(self):
        match self.theme:
            case "PaperColor-Light":
                self.theme_stylesheet = """
                background-color: #eeeeee;
                color: #444444;
                border: 1px solid #bcbcbc;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "PaperColor-Dark":
                self.theme_stylesheet = """
                background-color: #1c1c1c;
                color: #d0d0d0;
                border: 1px solid #585858;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """

    def apply_theme(self, widget):
        widget.setStyleSheet(self.theme_stylesheet)

    def toggle_theme(self):
        self.theme = self.theme_picker.currentText()
        self.set_theme()
        self.apply_theme(self)
        # Apply theme to all child widgets
        for widget in self.findChildren(QWidget):
            self.apply_theme(widget)

    def get_moves(self):
        scramble = ScrambleGenerator(self.puzzle_type.currentText())
        self.scramble.setText(scramble.generate_scramble(self.num_moves.value()))

    def set_default_num_moves(self):
        match self.puzzle_type.currentText():
            case "2x2":
                self.num_moves.setValue(9)
            case "3x3":
                self.num_moves.setValue(25)

    def toggle_timer(self):
        if not self.is_running:
            self.timer.start(100)  # Update display every 100 milliseconds
            self.timer_button.setText("Stop Timer")
            self.is_running = True
        else:
            self.timer.stop()
            self.timer_button.setText("Start Timer")
            self.is_running = False
            self.update_time()

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addMSecs(
            100
        )  # Increment time by 100 milliseconds
        self.timer_output.setText(self.elapsed_time.toString("mm:ss.z"))

        if not self.is_running:
            self.elapsed_time = QTime(0, 0)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
