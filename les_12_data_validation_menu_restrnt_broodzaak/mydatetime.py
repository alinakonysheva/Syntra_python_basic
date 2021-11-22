from datetime import date, datetime


class MyDateTime():
    __date = datetime.now()

    def __init__(self, value=None):
        if value is not None:
            self.mydate = value

    @property
    def mydate(self, value):
        if value and type(value) is datetime:
            pass
