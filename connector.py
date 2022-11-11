import win32com.client as win32


class Connector:
    @staticmethod
    def case(file_path):
        print('---- Подключаюсь к хайсис ----')
        print(' ')
        app = win32.DispatchEx('HYSYS.Application.v12.0')
        case = app.SimulationCases.Open(file_path)
        case.Visible = 1

        return case