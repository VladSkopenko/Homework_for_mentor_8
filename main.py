from datetime import date, datetime, timedelta

users = [{"name": "Bill Gates", "birthday": datetime(1955, 11, 3).date()},
         {"name": "Vlad ", "birthday": datetime(2023, 11, 4).date()},
         {"name": "Oleg", "birthday": datetime(1955, 11, 5).date()},
         {"name": "Alice", "birthday": datetime(2000, 11, 6).date()},
         {"name": "Luda", "birthday": datetime(1980, 11, 7).date()},]


def get_birthdays_per_week(users):
    if not users:
        return {}
    week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    now = date.today()
    birthdays_per_week = {day: [] for day in week.values()}
    for user in users:
        birthday = user['birthday']
        name = user['name']
        next_birthday = birthday.replace(year=now.year)
        if next_birthday < now:
            next_birthday = next_birthday.replace(year=now.year + 1)
        if now <= next_birthday <= now + timedelta(days=7):
            day_of_week = next_birthday.weekday()
            day_name__ = week[day_of_week]
            if day_name__ in ["Saturday", "Sunday"]:
                day_name__ = "Monday"
            birthdays_per_week[day_name__].append(name)

    return dict((key, value) for key, value in birthdays_per_week.items() if value)


print(get_birthdays_per_week(users))

if __name__ == "__main__":
    users = [
         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
     ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
