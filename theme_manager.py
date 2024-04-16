class ThemeManager:
    def __init__(self):
        pass

    def set_theme(main_window):
        if main_window.theme == "dark":
            main_window.theme_stylesheet = """
                background-color: #1c1c1c;
                color: #d0d0d0;
                border: 1px solid #585858;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """
        elif main_window.theme == "light":
            main_window.theme_stylesheet = """
                background-color: #eeeeee;
                color: #444444;
                border: 1px solid #bcbcbc;
                border-radius: 4px;
                padding: 2px 4px; /* Adjust padding */
            """

    def apply_theme(widget, main_window):
        widget.setStyleSheet(main_window.theme_stylesheet)

    def toggle_theme(main_window):
        main_window.theme = "light" if main_window.theme == "dark" else "dark"
        ThemeManager.set_theme(main_window)
        ThemeManager.apply_theme(main_window)
        # Apply theme to all child widgets
        for widget in main_window.findChildren(QWidget):
            ThemeManager.apply_theme(widget, main_window)
        if main_window.theme == "dark":
            main_window.theme_toggle.setText("Dark Mode")
        else:
            main_window.theme_toggle.setText("Light Mode")
