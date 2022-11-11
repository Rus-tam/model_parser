class Model:
    def __init__(self, case):
        self.case = case
        self.table = self.case.Flowsheet.Operations.Item('Table-1').Imports

        print('---- Подключение прошло успешно ----')
        print(' ')

    def change_data(self, changing_cells):
        changing_cells_names = self.__rebuild_cell_names(changing_cells)
        changing_cells_values = list(changing_cells.values())

        changing_cells = dict(zip(changing_cells_names, changing_cells_values))

        for cell in changing_cells_names:
            self.table.Item(cell).CellValue = changing_cells[cell]

    def get_data(self, monitoring_cells):
        values = {}
        changing_cells_names = self.__rebuild_cell_names(monitoring_cells)

        for cell in changing_cells_names:
            values[cell.split(':')[1]] = round(self.table.Item(cell).CellValue, 4)

        return values

    def __rebuild_cell_names(self, cells):
        if type(cells) == dict:
            all_cells_names = self.table.Names
            changing_cells_names = [cell for elem in list(cells.keys()) for cell in all_cells_names if elem in cell]

            return changing_cells_names
        if type(cells) == list:
            all_cells_names = self.table.Names
            changing_cells_names = [cell for elem in cells for cell in all_cells_names if elem in cell]

            return changing_cells_names
