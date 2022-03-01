import pandas as pd
from datetime import date
import calendar


def import_data():
    return pd.read_csv('data/BDO_NA_Boss_Times.csv')

def get_day():
    curr_date = date.today()
    return calendar.day_name[curr_date.weekday()]

def get_boss_schedule(data_set, day):
    print(data_set[data_set['Day'].str.contains(day)])

def main():

    # import data
    data_set = import_data()

    # get and print day of the week
    day = get_day()

    # get today's boss schedule
    get_boss_schedule(data_set, day)
    
if __name__ == '__main__':
    main()
