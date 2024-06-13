import sys

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
from file_handler import FileHandler


icon = FileHandler("images/scramble-generator-cube.ico")

config_file = FileHandler("configs/config.yml")
themes_file = FileHandler("configs/themes.yml")
user_defaults_file = FileHandler("configs/user_defaults.yml")

config = config_file.load_yaml_file()
themes = themes_file.load_yaml_file()
user_defaults = user_defaults_file.load_yaml_file()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # * Set window default settings
        self.setWindowTitle("Scramble Generator")
        self.setMinimumSize(
            config["min_window_size"]["width"], config["min_window_size"]["height"]
        )
        self.setWindowIcon(QIcon(icon.get_file_path()))

        # *  Define normal variables
        self.is_running = False
        self.elapsed_time = QTime(0, 0)
        self.puzzle_type_list = [puzzle for puzzle in config["puzzle_type_list"]]
        self.theme_list = [theme for theme in list(themes)[:-1]]

        # * Create end user widgets and apply settings to them
        self.scramble_button = QPushButton("Generate Scramble")

        self.puzzle_type = QComboBox()
        self.puzzle_type.addItems(self.puzzle_type_list)
        self.puzzle_type.setCurrentText(user_defaults["defaults"]["puzzle_type"])

        self.num_moves = QSpinBox()
        self.num_moves.setRange(
            config["num_moves_range"]["min"], config["num_moves_range"]["max"]
        )
        self.num_moves.setMaximumWidth(config["num_moves_widget_size"]["width"])
        self.num_moves.setValue(user_defaults["defaults"]["num_moves"])
        self.num_moves.lineEdit().setReadOnly(True)

        self.theme_picker = QComboBox()
        self.theme_picker.addItems(self.theme_list)
        self.theme_picker.setCurrentText(user_defaults["defaults"]["theme"])

        self.scramble = QLabel(
            " ", alignment=Qt.AlignmentFlag.AlignCenter, wordWrap=True
        )

        self.save_config_button = QPushButton("Save Config")

        self.timer_button = QPushButton("Start Timer")

        self.timer_output = QLabel(
            "00:00.0", alignment=Qt.AlignmentFlag.AlignCenter, maximumHeight=22
        )

        self.timer = QTimer()
        self.timer.interval = 10  # * Milliseconds

        # * Define button connections and/or actions
        self.scramble_button.pressed.connect(self.get_moves)
        self.puzzle_type.currentTextChanged.connect(self.set_default_num_moves)
        self.theme_picker.currentIndexChanged.connect(self.toggle_theme)
        self.save_config_button.pressed.connect(self.save_defaults)
        self.timer_button.pressed.connect(self.toggle_timer)
        self.timer.timeout.connect(self.update_time)

        # * Create layouts
        self.page = QVBoxLayout()
        self.row_one = QHBoxLayout()
        self.row_three = QHBoxLayout()

        # * Add widgets to layouts
        self.row_one.addWidget(self.scramble_button)
        self.row_one.addWidget(self.puzzle_type)
        self.row_one.addWidget(self.num_moves)
        self.row_one.addWidget(self.theme_picker)

        self.row_three.addWidget(self.save_config_button)
        self.row_three.addWidget(self.timer_button)
        self.row_three.addWidget(self.timer_output)

        # * Setup overall page layout and set default window theme
        self.page.addLayout(self.row_one)
        self.page.addWidget(self.scramble)
        self.page.addLayout(self.row_three)

        self.gui = QWidget()
        self.gui.setLayout(self.page)

        self.setCentralWidget(self.gui)

        self.toggle_theme()

    def toggle_theme(self):
        self.theme = self.theme_picker.currentText()
        self.apply_theme(self)
        for widget in self.findChildren(QWidget):  # * Apply theme to all child widgets
            self.apply_theme(widget)

    def apply_theme(self, widget):
        self.theme_stylesheet = f"""
            background-color: {themes[self.theme]['background-color']};
            color: {themes[self.theme]['color']};
            border: {themes[self.theme]['border']};
            border-radius: {themes['general']['border-radius']};
            padding: {themes['general']['padding']};
            """
        widget.setStyleSheet(self.theme_stylesheet)

    def get_moves(self):
        scramble = ScrambleGenerator(self.puzzle_type.currentText().lower())
        self.scramble.setText(scramble.generate_scramble(self.num_moves.value()))

    def set_default_num_moves(self):
        self.num_moves.setValue(
            config["puzzle_default_moves"][self.puzzle_type.currentText().lower()]
        )

    def toggle_timer(self):
        if not self.is_running:
            self.timer.start(100)  # * Update display every 100 milliseconds
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
        )  # * Increment time by 100 milliseconds
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

        user_defaults_file.save_yaml_file(current_configs)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
