import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from  PyQt5 import QtCore
import pyqtgraph as pg
import numpy as np
# pyqt 5.11.3

import RPi.GPIO as GPIO
from hx711 import HX711

# set up the load cell
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.reset()
hx.tare()
L = np.zeros(1)
#import force_read as f_r

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Alarge Coefficient of Friction Tester'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):
    x = np.zeros(1)
    y = np.zeros(1)
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Main Menu")
        self.tabs.addTab(self.tab2, "Test")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton2 = QPushButton("Start the test")
        self.pushButtonTare = QPushButton("Tare")
        self.pushButtonWeight = QPushButton("Weight")

        # Set Plotter
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.graphicsView = pg.PlotWidget(title="")
        self.tab2.layout.addWidget(self.pushButton2)
        self.tab2.layout.addWidget(self.pushButtonTare)
        self.tab2.layout.addWidget(self.pushButtonWeight)

        self.tab2.setLayout(self.tab2.layout)
        self.tab2.layout.addWidget(self.graphicsView)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphicsView.plot(self.x, self.y, pen=pen)
        # button events
        self.pushButton2.clicked.connect(self.btn_clk) # plot when clicked
        self.pushButtonTare.clicked.connect(self.btn_tare) # tare when clicked
        self.pushButtonWeight.clicked.connect(self.btn_weight) # weight when clicked

        # timer set and update plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()


    def btn_clk(self):
        val = hx.get_weight(5)
        np.append(L, val)

        self.graphicsView.plot(L, pen=pg.mkPen('r', width=3))  # this line plots red

    def btn_tare(self):
        hx.tare()

    def btn_weight(self):
        val = hx.get_weight(5)

        print(val)

    def update_plot(self):
        val = hx.get_weight(5)

        self.x.append(val)
        self.y.append(0.05)
        print(val)
        self.data_line.setData(self.x, self.y)
       # Add tabs to widget


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    """
            # Add plot to second tab
            self.graphicsView = pg.PlotWidget()
            self.tab2.layout = QVBoxLayout(self)
            self.graphicsView.setObjectName("graphicsView")
            self.tab2.layout.addWidget(self.graphicsView)
            self.pushButton2 = QPushButton("Plot that shit")

            self.pushButton2.clicked.connect(self.btn_clk)
    """