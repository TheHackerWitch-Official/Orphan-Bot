import pandas as pd


def import_data():
    return pd.read_csv('data/BDO_NA_Boss_Times.csv')

def main():
    data_set = import_data()
    print(data_set)

if __name__ == '__main__':
    main()
