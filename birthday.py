import calendar 
from datetime import datetime, date

users = [
    {"name": "Ivan", "birthday": datetime(year=2000, month=11, day=5)},
    {"name": "Denis", "birthday": datetime(year=1976, month=10, day=9)},
    {"name": "Bogdan", "birthday": datetime(year=2000, month=11, day=17)},
    {"name": "Oleg", "birthday": datetime(year=2008, month=9, day=21)},
    {"name": "Roma", "birthday": datetime(year=2010, month=9, day=9)},
    {"name": "Andrii", "birthday": datetime(year=2008, month=10, day=20)},
    {"name": "Vadim", "birthday": datetime(year=2004, month=1, day=22)},
    {"name": "Mykola", "birthday": datetime(year=2005, month=4, day=23)}]
def get_birthdays_per_week(user_list):
    result = []
    
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
        for week in weeks_list:
            if this_day in week:
                cur_week = week
                ind = weeks_list.index(week)
                pre_week = weeks_list[ind-1]
                working_week = pre_week[-2:]+cur_week[0:-2]
                if Day not in working_week:
                    print("Not this time")
                    continue

                elif Day in working_week[0:2]:
                    if 'Monday' in result:
                        result['Monday'].append(person['name'])
                    else:
                        result['Monday'] = []
                        result['Monday'].append(person['name'])
                else:
                    if birthday.strftime('%A') in result:
                        result[week_day].append(person['name'])
                    else:
                        result[week_day] = []
                        result[week_day].append(person['name'])

                print(f"result is - {result}")
                break
            else:
                continue
        print("*"*10)
        for day in result:
            print(f"{day}: {', '.join(result[day])}")

    return "DONE!"


print(get_birthdays_per_week(users))