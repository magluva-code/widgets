
import datetime
import pathlib
import sys

from PySide6.QtCore import Qt, QDateTime, QTimer, QCalendar
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QHBoxLayout

from calendarwidget import CalToFile


class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
        self.timers()

    def setup(self):
        self.setGeometry(100, 350, 400, 200)
        self.current_date = QDateTime.currentDateTime()
        self.current_year = self.current_date.toString('yyyy')
        self.current_month = self.current_date.toString('MM')
        self.current_day = self.current_date.toString('dd')
        month = self.get_calendar()

        self.c_label = QLabel("{0} {1} {2}".format(self.current_day, self.current_month, self.current_year))
        self.c_label.setObjectName("c_label")
        self.layout = QGridLayout()
        self.layout.addWidget(self.c_label, 0, 1, 1, 5)
        for week in range(len(month)):
            for day in range(len(month[week])):
                qlabel = QLabel(month[week][day])
                qlabel.setObjectName(month[week][day])
                self.layout.addWidget(qlabel, week+1, day)

        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

    def timers(self):
        calendar_interval = 1000*60*60
        current_interval = 1000*60
        self.calendar_timer = QTimer()
        self.calendar_timer.timeout.connect(self.update_calendar)
        self.calendar_timer.start(calendar_interval)
        self.current_timer = QTimer()
        self.current_timer.timeout.connect(self.update_current)
        self.current_timer.start(current_interval)

    def update_calendar(self):
        updated_month = self.get_calendar()
        for week in range(len(updated_month)):
            for day in range(len(updated_month[week])):
                child = self.findChild(QLabel, updated_month[week][day])
                child.setText(updated_month[week][day])

    def update_current(self):
        updated_current_year = self.current_date.toString('yyyy')
        updated_current_month = self.current_date.toString('MM')
        updated_current_day = self.current_date.toString('dd')
        self.c_label.setText("{0} {1} {2}".format(updated_current_day, updated_current_month, updated_current_year))

    def get_calendar(self):
        cal = CalToFile.get_current_month(self.current_year, self.current_month)
        file_name = CalToFile.write_to_file(cal)
        with open(file_name, 'r') as f:
            month = [i.split() for i in f][1::]
        return month

    @staticmethod
    def set_style(app, stylesheet):
        with open(stylesheet, "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
