import sys, os, yaml

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
icon = os.path.join(basedir, "images/scramble-generator-cube.ico")

config_file = os.path.join(basedir, "configs/config.yml")
with open(config_file, "r") as f:
    config = yaml.safe_load(f)

user_defaults_file = os.path.join(basedir, "configs/user_defaults.yml")
with open(user_defaults_file, "r") as f:
    user_defaults_config = yaml.safe_load(f)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window default settings
        self.setWindowTitle("Scramble Generator")
        self.default_window_min_width = config["min_window_size"]["width"]
        self.default_window_min_height = config["min_window_size"]["height"]
        self.setMinimumSize(
            self.default_window_min_width, self.default_window_min_height
        )
        self.setWindowIcon(QIcon(icon))

        # Define normal variables
        self.is_running = False
        self.elapsed_time = QTime(0, 0)
        self.default_theme = user_defaults_config["defaults"]["theme"]
        self.default_num_moves = user_defaults_config["defaults"]["num_moves"]
        self.default_puzzle_type = user_defaults_config["defaults"]["puzzle_type"]
        self.default_min_num_moves = config["num_moves_range"]["min"]
        self.default_max_num_moves = config["num_moves_range"]["max"]
        self.default_num_moves_for_two_by_two = config["num_moves_per_puzzle_defaults"][
            "2x2"
        ]
        self.default_num_moves_for_three_by_three = config[
            "num_moves_per_puzzle_defaults"
        ]["3x3"]
        self.puzzle_type_list = []
        for puzzle in config["puzzle_type_list"]:
            self.puzzle_type_list.append(puzzle)
        self.theme_list = []
        for theme in config["theme_list"]:
            self.theme_list.append(theme)

        # Create end user widgets and apply settings to them
        self.scramble_button = QPushButton("Generate Scramble")

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(self.puzzle_type_list)
        self.puzzle_type.setCurrentText(self.default_puzzle_type)

        self.num_moves = QSpinBox()
        self.num_moves.setRange(self.default_min_num_moves, self.default_max_num_moves)
        self.num_moves.setValue(self.default_num_moves)
        self.num_moves.lineEdit().setReadOnly(True)

        self.theme_picker = QComboBox()
        self.theme_picker.addItems(self.theme_list)
        self.theme_picker.setCurrentText(self.default_theme)

        self.scramble = QLabel()
        self.scramble.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        self.save_config_button = QPushButton("Save Config")

        self.timer_button = QPushButton("Start Timer")

        self.timer_output = QLabel("00:00.0")
        self.timer_output.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )
        self.timer_output.setMaximumHeight(22)

        self.timer = QTimer()
        self.timer.interval = 10  # Milliseconds

        # Define button connections and/or actions
        self.scramble_button.pressed.connect(self.get_moves)
        self.puzzle_type.currentTextChanged.connect(self.set_default_num_moves)
        self.theme_picker.currentIndexChanged.connect(self.toggle_theme)
        self.save_config_button.pressed.connect(self.save_defaults)
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

        self.timer_section.addWidget(self.save_config_button)
        self.timer_section.addWidget(self.timer_button)
        self.timer_section.addWidget(self.timer_output)

        # Setup overall page layout and set default window theme
        self.page.addLayout(self.inputs)
        self.page.addWidget(self.scramble)
        self.page.addLayout(self.timer_section)

        self.gui = QWidget()
        self.gui.setLayout(self.page)

        self.setCentralWidget(self.gui)

        self.toggle_theme()

    def set_theme(self):
        match self.theme:
            case "Dracula":
                self.theme_stylesheet = """
                background-color: #282a36;
                color: #f8f8f2;
                border: 1px solid #44475a;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Everforest-Light":
                self.theme_stylesheet = """
                background-color: #f3ead3;
                color: #5c6a72;
                border: 1px solid #b9c0ab;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Everforest-Dark":
                self.theme_stylesheet = """
                background-color: #333c43;
                color: #d3c6aa;
                border: 1px solid #5d6b66;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Gruvbox-Light":
                self.theme_stylesheet = """
                background-color: #fbf1c7;
                color: #282828;
                border: 1px solid #928374;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Gruvbox-Dark":
                self.theme_stylesheet = """
                background-color: #282828;
                color: #fbf1c7;
                border: 1px solid #928374;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Nord-Aurora":
                self.theme_stylesheet = """
                background-color: #bf616a;
                color: #ebcb8b;
                border: 1px solid #d08770;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Nord-Frost":
                self.theme_stylesheet = """
                background-color: #5e81ac;
                color: #8fbcbb;
                border: 1px solid #81a1c1;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
            case "Nord-PolarNight":
                self.theme_stylesheet = """
                background-color: #2e3440;
                color: #4c566a;
                border: 1px solid #3b4252;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
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
                self.num_moves.setValue(self.default_num_moves_for_two_by_two)
            case "3x3":
                self.num_moves.setValue(self.default_num_moves_for_three_by_three)

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

    def save_defaults(self):
        current_configs = {
            "defaults": {
                "theme": self.theme_picker.currentText(),
                "num_moves": self.num_moves.value(),
                "puzzle_type": self.puzzle_type.currentText(),
            }
        }

        with open(user_defaults_file, "w") as f:
            yaml.dump(current_configs, f, default_flow_style=False)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
