from datetime import date
from datetime import datetime, timedelta


class Step:
    def __init__(self):
        self.yearmonth = None

    def getYearMonth(self):
        today = date.today()
        diff = 1
        if today.day < 15:
            diff = 2

        if today.month < 10:
            self.yearmonth = str(today.year) + '0' + str(today.month - diff)

        return self.yearmonth

    def getDate(self):
        today = date.today() + timedelta(days=-2)
        return today
