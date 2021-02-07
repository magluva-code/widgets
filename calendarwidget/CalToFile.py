import calendar
import pathlib

def get_current_month(yy, mm):
    """
    @param
        yy: Full year. Must be int or a value that can be type casted to int.
        mm: Day of the month. Must be int or a value that can be type casted to int.
    @return
        Text object calendar representation
    """
    if not isinstance(yy, int):
        yy = int(yy)
    if not isinstance(mm, int):
        mm = int(mm)
    c = calendar.TextCalendar(calendar.MONDAY)
    return c.formatmonth(yy, mm)

def write_to_file(txt):
    """
    @param
        file_name: str of wanted file name.
        txt: str of text that will be written to the file.
    @return void
    """
    cwd = pathlib.Path(__file__).parent.absolute()
    file_name = "{0}/current_month.txt".format(cwd)
    with open(file_name, 'w') as f:
        f.write(txt)
    return file_name
