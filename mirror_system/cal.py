from datetime import date, timedelta
from dateutil import easter
from dateutil.relativedelta import *
import datetime
from unusual_holidays import Holidays


class Calendar:
    today = datetime.date.today()
    year = today.year
    month = today.month

    def get_holidays(self):
        output = {}
        today = datetime.date.today()
        year = today.year
        month = today.month
        easter_sunday = easter.easter(year)
        holidays = {'Nowy Rok': date(year, 1, 1),
                    'Trzech Kroli': date(year, 1, 6),
                    '!Dzień Babci': date(year, 1, 21),
                    '!Dzień Dziadka': date(year, 1, 22),
                    '!Walentynki': date(year, 2, 14),
                    '!Dzień Kobiet': date(year, 3, 8),
                    'Niedziela Wielkanocna': easter_sunday,
                    'Poniedziałek wielkanocny': easter_sunday + timedelta(days=1),
                    'Święto Pracy': date(year, 5, 1),
                    '!Święto Flagi': date(year, 5, 2),
                    'Święto Konstytucji 3 Maja': date(year, 5, 3),
                    '!Dzień Ojca': date(year, 6, 23),
                    'Zielone Świątki': easter_sunday + relativedelta(days=+1, weekday=SU(+7)),
                    'Boże Ciało': easter_sunday + relativedelta(weekday=TH(+9)),
                    '!Dzień Powstania Warszawskiego': date(year, 8, 1),
                    'Wniebowzięcie Najświętszej Maryi Panny': date(year, 8, 15),
                    'Wszystkich Świętych': date(year, 11, 1),
                    'Święto Niepodległości': date(year, 11, 11),
                    'Pierwszy Dzień Świąt Bożego Narodzenia': date(year, 12, 25),
                    'Drugi Dzień Świąt Bozego Narodzenia': date(year, 12, 26)}
        for value, key in holidays.items():
            temp = str(key)[0:7]
            actual = "{}-{}".format(year, month)
            if temp == actual:
                day = str(key)
                output[day] = value
        return output

    def get_unusual_day(self):
        u_holidays = Holidays()
        return u_holidays.get_holiday(self.today.day, self.today.month)

    def get_day(self):
        now = datetime.datetime.now()
        name = now.strftime("%A")
        if str(name) == "Monday":
            name = name.replace("Monday", "Poniedziałek")
        if str(name) == "Tuesday":
            name = name.replace("Tuesday", "Wtorek")
        if str(name) == "Wednesday":
            name = name.replace("Wednesday", "Środa")
        if str(name) == "Thursday":
            name = name.replace("Thursday", "Czwartek")
        if str(name) == "Friday":
            name = name.replace("Friday", "Piątek")
        if str(name) == "Saturday":
            name = name.replace("Saturday", "Sobota")
        if str(name) == "Sunday":
            name = name.replace("Sunday", "Niedziela")
        output = "{}, {}.{}.{}".format(name, now.day, now.month, now.year)
        return output




