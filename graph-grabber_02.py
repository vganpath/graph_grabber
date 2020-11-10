#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:53:28 2020

@author: vgk
"""
import os
import sys

from graph_grabber_gui_02 import * #UI file

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5 import QtWidgets,uic

x_origin_px, y_origin_px = 10,10
x_origin_unit,y_origin_unit = 0,0
x_scale, y_scale = 1,1

x_select, y_select = 1,1

x_calibrated, y_calibrated = 0,0

class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
 
        super().__init__()
 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Assigning functions to buttons
        self.ui.btn_load.clicked.connect(self.load_image) 
        self.ui.btn_x1.clicked.connect(self.calibrate)
        self.ui.btn_x2.clicked.connect(self.calibrate)
        self.ui.btn_y1.clicked.connect(self.calibrate)
        self.ui.btn_y2.clicked.connect(self.calibrate)
        self.ui.btn_reset.clicked.connect(self.reset)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.reset()
        
    def reset(self):
        #Clearing labels
        self.ui.label_x_select.clear() 
        self.ui.label_y_select.clear() 
        self.ui.label_x_extract.clear() 
        self.ui.label_y_extract.clear()
        self.ui.label_status.clear()
        
        #Disabling buttons
        self.ui.btn_x2.setEnabled(False)
        self.ui.btn_y2.setEnabled(False)
        global x_origin_px, y_origin_px, x_origin_unit, y_origin_unit,x_scale, y_scale, x_select, y_select, x_calibrated, y_calibrated
        x_origin_px, y_origin_px = 10,10
        x_origin_unit,y_origin_unit = 0,0
        x_scale, y_scale = 1,1
        x_select, y_select = 1,1
        x_calibrated, y_calibrated = 0,0
        
    def load_image(self):
        os.chdir("/home/vgk/Spyder-Projects/Graph-grabber")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","png(*.png)",options=options)
        if fileName:
            '''
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(fileName)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.ui.graphicsView.setScene(scene)
            self.ui.graphicsView.fitInView()
            '''
            name='label_3'
            icon_label=self.findChild(QLabel,name)
            pixmap = QPixmap(fileName)
            icon_label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        global x_select, y_select
        x_select, y_select = event.x(), event.y()
        print('x:%i'%x_select + ' y:%i'%y_select)
        self.ui.label_x_select.setText(str(x_select)) 
        self.ui.label_y_select.setText(str(y_select))
        
        global x_calibrated, y_calibrated
        if x_calibrated == 1 and y_calibrated == 1:
            global x_origin_px, x_scale, y_origin_px, y_scale, x_origin_unit, y_origin_unit
            x_extracted = x_origin_unit+((x_select-x_origin_px)*x_scale)
            y_extracted = y_origin_unit+((y_select-y_origin_px)*y_scale)
            #self.ui.label_x_extract.setText(str(x_extracted)) 
            self.ui.label_x_extract.setText(str(format(x_extracted, '.2f')))
            #self.ui.label_y_extract.setText(str(y_extracted))
            self.ui.label_y_extract.setText(str(format(y_extracted, '.2f')))
            
        
    def calibrate(self):
        btn_name=self.sender()
        global x_select, y_select, x_origin_unit, y_origin_unit, x_origin_px, y_origin_px, x_scale, y_scale, x_calibrated, y_calibrated
        if btn_name == self.ui.btn_x1:
            x_origin_px=x_select
            x_origin_unit=float(self.ui.lineEdit_x1.text())
            self.ui.btn_x2.setEnabled(True)
        elif btn_name == self.ui.btn_x2:
            x_buffer_px=x_select
            x_buffer_unit=float(self.ui.lineEdit_x2.text())
            x_scale=(x_buffer_unit-x_origin_unit)/(x_buffer_px-x_origin_px)
            x_calibrated=1
        elif btn_name == self.ui.btn_y1:
            y_origin_px=y_select
            y_origin_unit=float(self.ui.lineEdit_y1.text())
            self.ui.btn_y2.setEnabled(True)
        elif btn_name == self.ui.btn_y2:
            y_buffer_px=y_select
            y_buffer_unit=float(self.ui.lineEdit_y2.text())
            y_scale=(y_buffer_unit-y_origin_unit)/(y_buffer_px-y_origin_px)
            y_calibrated = 1
        if x_calibrated == 1 and y_calibrated == 1:
            self.ui.label_status.setText('Calibrated!!!')
        

app = QtWidgets.QApplication([])
 
win = mywindow()
 
win.show()
 
sys.exit(app.exec())
