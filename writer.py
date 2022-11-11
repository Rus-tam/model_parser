import pandas as pd
import os
import time


class Writer:
    @staticmethod
    def write_csv(data):
        path = os.getcwd()
        if 'data' not in os.listdir(path):
            os.mkdir(rf'{path}/data')

        df = pd.DataFrame(data, index=[0])
        current_time = time.time()
        df.to_csv(rf'{path}/data/{current_time}.csv', index=False)

        print(f'---- Файл {current_time}.csv записан ----')
        print(' ')

    @staticmethod
    def make_overall_csv():
        path = os.getcwd()
        files = os.listdir(rf'{path}/data')
        data = pd.DataFrame({})
        concat_data = pd.DataFrame({})

        for file in files:
            data = pd.read_csv(rf"{path}/data/{file}")
            concat_data = pd.concat([concat_data, data], axis=0)

        concat_data.to_csv(rf'{path}/data/overall-data.csv', index=False)

        print('---- Файл overall-data.csv записан ----')
        print(' ')
        print('---- Процедура закончена ----')
        print(' ')

