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
        t = "<span style=\"color:#93ebd5;\">{0}</span><span style=\"color:#00afd7;\">:</span><span style=\"color:#d5f6ff;\">{1}</span>".format(hourDisplay, minuteDisplay)
        self.current_time = QLabel(t)
        self.current_time.setObjectName("current_time")
        self.current_time.setAlignment(Qt.AlignRight)
        #self.hour = QLabel(hourDisplay)
        #self.hour.setObjectName("hr")
        #self.hour.setAlignment(Qt.AlignRight)
        #self.separator = QLabel(" : ")
        #self.separator.setObjectName("sep")
        #self.separator.setAlignment(Qt.AlignCenter)
        #self.minute = QLabel(minuteDisplay)
        #self.minute.setObjectName("min")
        #self.minute.setAlignment(Qt.AlignLeft)

        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.current_time)
        #self.layout.addWidget(self.hour)
        #self.layout.addWidget(self.separator)
        #self.layout.addWidget(self.minute)
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
        t = "<span style=\"color:#93ebd5;\">{0}</span><span style=\"color:#00afd7;\">:</span><span style=\"color:#d5f6ff;\">{1}</span>".format(hourDisplay, minuteDisplay)
        self.current_time.setText(t)
        #self.hour.setText(hourDisplay)
        #self.minute.setText(minuteDisplay)

    @staticmethod
    def set_style(app, stylesheet):
        with open(stylesheet, "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
