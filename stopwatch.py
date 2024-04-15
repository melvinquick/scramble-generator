from PyQt6.QtCore import Qt, QTimer, QTime

class Timer():
    def __init__(self, is_running=False):
        self.is_running = is_running

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
        self.elapsed_time = self.elapsed_time.addMSecs(100) # Increment time by 100 milliseconds
        self.timer_output.setText(self.elapsed_time.toString("mm:ss.z"))

        if not self.is_running:
            self.elapsed_time = QTime(0, 0)