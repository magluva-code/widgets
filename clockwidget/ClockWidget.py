import sys
import datetime
import pathlib
from PySide6.QtCore import Qt, QDateTime, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


class ClockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
        self.timer()

    def setup(self):
        time = QDateTime.currentDateTime()
        hourDisplay = time.toString('hh')
        minuteDisplay = time.toString('mm')

        self.setGeometry(100, 100, 400, 200)

        self.hour = QLabel(hourDisplay)
        self.hour.setObjectName("hr")
        self.hour.setAlignment(Qt.AlignRight)
        self.separator = QLabel(" : ")
        self.separator.setObjectName("sep")
        self.separator.setAlignment(Qt.AlignCenter)
        self.minute = QLabel(minuteDisplay)
        self.minute.setObjectName("min")
        self.minute.setAlignment(Qt.AlignLeft)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.hour)
        self.layout.addWidget(self.separator)
        self.layout.addWidget(self.minute)
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

    def timer(self):
        interval = 1000
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(interval)

    def update_labels(self):
        time = QDateTime.currentDateTime()
        hourDisplay = time.toString('hh')
        minuteDisplay = time.toString('mm')
        self.hour.setText(hourDisplay)
        self.minute.setText(minuteDisplay)

    @staticmethod
    def set_style(app, stylesheet):
        with open(stylesheet, "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
