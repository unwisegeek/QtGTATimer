import sys, os, time
import pandas as pd

from typing import Type
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


# Import Data or create a .qtgtatimer data file in the user home directory
def load_config():
    if os.path.isfile('./.gtatimer'):
        timers = pd.read_csv('./.gtatimer')
    else:
        data = {'nightclub': [0],
                'bunker': [0],
                'coke': [0],
                'meth': [0],
                'cash': [0]}
        # df = pd.DataFrame(data)
        df = pd.DataFrame(data, columns=['nightclub','bunker','coke','meth','cash'])
        df.to_csv('./.gtatimer')
        if os.path.isfile('./.gtatimer'):
            timers = pd.read_csv('./.gtatimer')
        else:
            sys.exit(1)
    return timers

def write_config(timers):
    timers.to_csv('./.gtatimer')

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.main_win.setWindowTitle("QtGTATimer")

        # Set Initial Values from Config
        timers = load_config()
        self.ui.labelNightclubStart.setText(time.ctime(int(timers['nightclub'][0])))

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win: Type[MainWindow] = MainWindow()
    main_win.show()
    sys.exit(app.exec())
