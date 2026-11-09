import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.11.13"},
    {"name": "Jane Smith", "birthday": "1990.11.15"}
]

def get_birthdays_per_week(users):
    today = dtdt.now()
    birthdays = []
    for user in users:
        birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d")
        birthday_this_year = birthday.replace(year=today.year)
        if today <= birthday_this_year <= today + dt.timedelta(days=7):
            birthdays.append((user["name"], birthday_this_year.strftime("%Y.%m.%d")))
    return birthdays

print(get_birthdays_per_week(users))