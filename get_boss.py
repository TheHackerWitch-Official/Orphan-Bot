import pandas as pd
from datetime import date, datetime, time
import calendar
pd.options.mode.chained_assignment = None  # default='warn'


def import_data():
    return pd.read_csv('data/BDO_NA_Boss_Times.csv')

def get_day():
    curr_date = date.today()
    return calendar.day_name[curr_date.weekday()]

def get_time():
    time = datetime.now()
    return time.strftime("%H:%M")

def get_boss_schedule():
    data_set = import_data()
    day = get_day()
    return data_set[data_set['Day'].str.contains(day)]

def get_hour_minute(time):
    nums = time.split(':')
    return int(nums[0]), int(nums[1])

def to_time(time_string):
    hrs,mins = get_hour_minute(time_string)
    return time(hour=hrs,minute=mins)
 
def convert_time(schedule):
    schedule['Time_EST'] = schedule['Time_EST'].map(to_time)
    return schedule

def get_remaining_bosses():
    boss_schedule = convert_time(get_boss_schedule())
    curr_time = to_time(get_time())
    leftToday = boss_schedule[boss_schedule['Time_EST'].apply(lambda t : t >= curr_time)]
    print(leftToday[['Boss', 'Time_EST']])

def get_todays_boss_schedule():
    boss_schedule = convert_time(get_boss_schedule())

    print(boss_schedule[['Boss', 'Time_EST']])


def main():
    get_remaining_bosses()

if __name__ == '__main__':
    main()
