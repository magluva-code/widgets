
import pathlib
import sys

from PySide6.QtWidgets import QApplication

from clockwidget.ClockWidget import ClockWidget
from calendarwidget.CalendarWidget import CalendarWidget


def run(package, widget):
    cwd = pathlib.Path(__file__).parent.absolute()
    stylesheet ="{0}/{1}/style.qss".format(cwd, package)

    w = widget()
    w.show()
    w.set_style(app, stylesheet)



if __name__ == "__main__":

    cwd = pathlib.Path(__file__).parent.absolute()
    app = QApplication([])
    #run("clockwidget", ClockWidget)
    #run("calendarwidget", CalendarWidget)
    clock = ClockWidget()
    clock.show()
    clock_style = "{0}/clockwidget/style.qss".format(cwd)
    clock.set_style(clock, clock_style)
    calendar = CalendarWidget()
    calendar.show()
    calendar_style = "{0}/calendarwidget/style.qss".format(cwd)
    calendar.set_style(calendar, calendar_style)
    sys.exit(app.exec_())
