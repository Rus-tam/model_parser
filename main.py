import time

from writer import Writer
from model import Model
from connector import Connector

file_path = rf'D:\Python\HysysModels\1.hsc'
case = Connector.case(file_path)

model_inst = Model(case)

changing_cells = {'B1': 0.1, 'B4': 5, 'B6': 0.02777777}
monitoring_cells = ['B1', 'B4', 'B6', 'B5', 'B7', 'B8']

model_inst.change_data(changing_cells)
data = model_inst.get_data(monitoring_cells)
Writer.write_csv(data)

while changing_cells['B1'] <= 5:
    changing_cells['B1'] += 0.1
    changing_cells['B4'] = 5

    while changing_cells['B4'] <= 50:
        changing_cells['B4'] += 1
        changing_cells['B6'] = 0.0277777777

        while changing_cells['B6'] <= 5.5555556:
            changing_cells['B6'] += 0.00027777778

            model_inst.change_data(changing_cells)
            data = model_inst.get_data(monitoring_cells)

            Writer.write_csv(data)

            time.sleep(0.3)

Writer.make_overall_csv()
