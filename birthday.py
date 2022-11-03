import calendar 
from datatime import date , datatime

users = [
    {"name": "Ivan", "birthday": datetime(year=1999, month=3, day=20)},
    {"name": "Denis", "birthday": datetime(year=1989, month=9, day=22)},
    {"name": "Bogdan", "birthday": datetime(year=2002, month=9, day=17)},
    {"name": "Oleg", "birthday": datetime(year=2006, month=9, day=21)},
    {"name": "Roma", "birthday": datetime(year=1996, month=9, day=22)},
    {"name": "Andrii", "birthday": datetime(year=1996, month=9, day=20)},
    {"name": "Vadim", "birthday": datetime(year=1996, month=9, day=22)},
    {"name": "Mykola", "birthday": datetime(year=1996, month=9, day=23)}
]
def get_birthdays_per_week(user_list):
    current_month = date.today().month
    for person in user_list:

        Month, Day = person['birthday'].month, person['birthday'].day
        this_year = date.today().year
        this_day = date.today().day
        birthday = date(this_year, Month, Day)
        if Month != current_month:
            continue
        else:
            print("\n{:=^50}\n".format('ok, we have some candidats :)'))


        week_day = birthday.strftime('%A')
        weeks_list = calendar.monthcalendar(this_year, Month)