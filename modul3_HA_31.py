import datetime as dt
from datetime import timedelta, datetime as dtdt
def get_days_from_today(date):
    today_date = dtdt.now().date()
    date=dtdt.strptime(date, '%Y-%m-%d').date()
    diff = (today_date - date).days
    return diff

try:
    date = input("Enter a date in YYYY-MM-DD format: ")
    print(get_days_from_today(date))
except ValueError:
    print("Invalid date format. Please enter a date in YYYY-MM-DD format.")