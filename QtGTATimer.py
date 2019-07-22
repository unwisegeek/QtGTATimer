import sys, os, time
import pandas as pd

from typing import Type
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from datetime import datetime
from datetime import timedelta

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

def convert_epoch_to_string(secs):
    # return time.strftime("%m/%d/%y %H:%m", time.strptime(time.ctime(secs)))
    conv_time = datetime.fromtimestamp(secs)
    hours = str(conv_time.hour).zfill(2)
    mins = str(conv_time.minute).zfill(2)
    sec = str(conv_time.second).zfill(2)
    retval = "{}:{}:{}".format(hours, mins, sec)
    return retval

def convert_seconds_to_hms(secs):
    remaining = str(timedelta(seconds=secs))
    return remaining[:8]

def start_new_timer(timers, target):
    timers[target][0] = time.time()
    write_config(timers)
    main_win.refresh()

def get_timer_stats(timers, target, offset):
    curr_time = time.time()
    start_time = int(timers[target][0])
    end_time = start_time + offset
    rem_time = (start_time + offset) - curr_time
    perc_time = 100 - (((end_time - curr_time) / offset) * 100)
    return start_time, end_time, rem_time, perc_time


class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.main_win.setWindowTitle("QtGTATimer")

        timers = load_config()

        self.qTimer = QTimer()
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(lambda: self.refresh())
        self.qTimer.start()

        self.ui.pushNightclub.clicked.connect(lambda: start_new_timer(timers, "nightclub"))
        self.ui.pushBunker.clicked.connect(lambda: start_new_timer(timers, "bunker"))
        self.ui.pushCoke.clicked.connect(lambda: start_new_timer(timers, "coke"))
        self.ui.pushMeth.clicked.connect(lambda: start_new_timer(timers, "meth"))
        self.ui.pushCash.clicked.connect(lambda: start_new_timer(timers, "cash"))
        self.ui.actionQuit.triggered.connect(lambda: self.clicked_quit(timers))

    def show(self):
        self.main_win.show()

    def clicked_quit(self, timers):
        os.sys.exit(0)

    def refresh(self):

        timers = load_config()

        # Set Nightclub Information
        start_time, end_time, rem_time, perc_time = get_timer_stats(timers, "nightclub", 72000)
        self.ui.labelNightclubStart.setText(convert_epoch_to_string(start_time))
        self.ui.labelNightclubEnd.setText(convert_epoch_to_string(end_time))
        self.ui.labelNightclubRem.setText(convert_seconds_to_hms(rem_time))
        self.ui.progressNightclub.setValue(perc_time)

        # Set Bunker Information
        start_time, end_time, rem_time, perc_time = get_timer_stats(timers, "bunker", 8400)
        self.ui.labelBunkerStart.setText(convert_epoch_to_string(start_time))
        self.ui.labelBunkerEnd.setText(convert_epoch_to_string(end_time))
        self.ui.labelBunkerRem.setText(convert_seconds_to_hms(rem_time))
        self.ui.progressBunker.setValue(perc_time)

        # Set Coke Lockup Information
        start_time, end_time, rem_time, perc_time = get_timer_stats(timers, "coke", 7200)
        self.ui.labelCokeStart.setText(convert_epoch_to_string(start_time))
        self.ui.labelCokeEnd.setText(convert_epoch_to_string(end_time))
        self.ui.labelCokeRem.setText(convert_seconds_to_hms(rem_time))
        self.ui.progressCoke.setValue(perc_time)

        # Set Meth Lab Information
        start_time, end_time, rem_time, perc_time = get_timer_stats(timers, "meth", 8640)
        self.ui.labelMethStart.setText(convert_epoch_to_string(start_time))
        self.ui.labelMethEnd.setText(convert_epoch_to_string(end_time))
        self.ui.labelMethRem.setText(convert_seconds_to_hms(rem_time))
        self.ui.progressMeth.setValue(perc_time)

        # Set Cash Factory Information
        start_time, end_time, rem_time, perc_time = get_timer_stats(timers, "cash", 9600)
        self.ui.labelCashStart.setText(convert_epoch_to_string(start_time))
        self.ui.labelCashEnd.setText(convert_epoch_to_string(end_time))
        self.ui.labelCashRem.setText(convert_seconds_to_hms(rem_time))
        self.ui.progressCash.setValue(perc_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win: Type[MainWindow] = MainWindow()
    main_win.show()
    sys.exit(app.exec())