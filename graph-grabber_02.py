#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:53:28 2020

@author: vgk
"""
import os
import sys
import math as m
from graph_grabber_gui_02 import * #UI file

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QWidget, QScrollArea
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5 import QtWidgets,uic

x_origin_px, y_origin_px = 10, 10
x_origin_unit, y_origin_unit = 0, 0
x_scale, y_scale = 1, 1
x_select, y_select = 1, 1
x_calibrated, y_calibrated = 0, 0
data_extracted_list = []
x_extracted, y_extracted = None, None
x_log, y_log = 0, 0

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
        self.ui.btn_ScaleImage.clicked.connect(self.fit_image)
        self.ui.btn_clear_image.clicked.connect(self.clear_marked_points)
        self.ui.btn_delete_data.clicked.connect(self.delete_last_point)
        self.ui.btn_print_data.clicked.connect(self.print_extracted_data)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.reset()
        # self.ui.pushButton.clicked.connect(self.reSize_image)
        self.ScaleFactor = 1.05
        self.pixmap = None
        self.filename = None
        self.image_width, self.image_height = None, None

        #Setting label and widget geometry
        self.widget_width, self.widget_height = 1300, 790
        self.image_label_width, self.image_label_height = 1230, 750  # self.icon_label.size().width()
        self.widget_pos_x, self.widget_pos_y  = 30, 10 #self.widget_id.x()  # 30
        self.label_pos_x, self.label_pos_y  = 10, 10  # self.icon_label.x()  # 10

        name_label = 'label_3'
        name_widget = 'widget'
        self.icon_label = self.findChild(QLabel, name_label)
        self.widget_id = self.findChild(QWidget, name_widget)
        self.widget_id.setGeometry(self.widget_pos_x, self.widget_pos_y, self.widget_width, self.widget_height)
        self.icon_label.setGeometry(self.label_pos_x, self.label_pos_y, self.image_label_width, self.image_label_height)

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
        global x_origin_px, y_origin_px, x_origin_unit, y_origin_unit,x_scale, y_scale, x_select, y_select, x_calibrated, y_calibrated, data_extracted_list, x_extracted, y_extracted, x_log, y_log
        x_origin_px, y_origin_px = 10,10
        x_origin_unit,y_origin_unit = 0,0
        x_scale, y_scale = 1,1
        x_select, y_select = 1,1
        x_calibrated, y_calibrated = 0,0
        data_extracted_list = []
        x_extracted, y_extracted = None, None
        self.image_width, self.image_height = None, None
        x_log, y_log = 0, 0
        self.ScaleFactor = 1.05
        self.ui.infobox.append('Data reset')

    # def wheelEvent(self, event):
    #     d = event.angleDelta().y()
    #     x = event.position().x()
    #     y = event.position().y()
    #     self.reSize_image(d,x,y)

    def reSize_image(self,scroll,x,y):
        # print(icon_label.pixmap().size())
        if scroll>0:
            #self.icon_label.resize(1.05 * self.icon_label.size())
            offset_x = (x-self.widget_pos_x-self.label_pos_x) * (0.05)
            offset_y = (y-self.widget_pos_y-self.label_pos_y) * (0.05)
            label_width = (self.icon_label.size().width())*1.05
            label_height = (self.icon_label.size().height())*1.05
            self.icon_label.setGeometry(self.label_pos_x-offset_x, self.label_pos_y-offset_y, label_width, label_height)
        elif scroll<0:
            self.icon_label.resize(0.95 * self.icon_label.size())

    def fit_image(self):
        self.icon_label.setGeometry(self.label_pos_x, self.label_pos_y, self.image_label_width, self.image_label_height)
        self.ScaleFactor = 1.05

    def load_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","png(*.png),jpg(*.jpg)",options=options)
        if self.filename:
            # name = 'label_3'
            # icon_label = self.findChild(QLabel, name)
            self.pixmap = QPixmap(self.filename)
            self.image_width = self.pixmap.size().width()
            self.image_height = self.pixmap.size().height()
            self.icon_label.setScaledContents(True)
            self.icon_label.setPixmap(self.pixmap)

    def clear_marked_points(self):
        self.pixmap = QPixmap(self.filename)
        self.icon_label.setPixmap(self.pixmap)

    def mark_point(self,x,y):
        scale_width = self.icon_label.size().width()/self.image_width
        scale_height = self.icon_label.size().height()/self.image_height

        # create painter instance with pixmap
        self.painterInstance = QtGui.QPainter(self.pixmap)
        #self.painterInstance.begin(icon_label)

        # set rectangle color and thickness
        self.penRectangle = QtGui.QPen(QtCore.Qt.green)
        self.penRectangle.setWidth(5)

        # draw rectangle on painter
        offset_x = self.widget_pos_x + self.label_pos_x
        offset_y = self.widget_pos_y + self.label_pos_y
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawPoint((x-offset_x)/scale_width, (y-offset_y)/scale_height)

        # set pixmap onto the label widget
        self.icon_label.setPixmap(self.pixmap)
        self.icon_label.show()
        self.painterInstance.end()


    def mousePressEvent(self, event):
        global x_select, y_select, x_extracted, y_extracted
        x_select, y_select = event.x(), event.y()
        print('x:%i'%x_select + ' y:%i'%y_select)
        self.ui.label_x_select.setText(str(x_select)) 
        self.ui.label_y_select.setText(str(y_select))
        self.mark_point(x_select,y_select)
        global x_calibrated, y_calibrated
        if x_calibrated == 1 and y_calibrated == 1:
            global x_origin_px, x_scale, y_origin_px, y_scale, x_origin_unit, y_origin_unit, x_log, y_log
            if x_log == 0:
                x_extracted = x_origin_unit+((x_select-x_origin_px)*x_scale)
                self.ui.label_x_extract.setText(str(format(x_extracted, '.2f')))
            else:
                modulo_tick = int(x_select/x_scale)
                last_major_tick = modulo_tick * x_scale
                minor_tick =(x_select-x_origin_px-(modulo_tick*x_scale))/x_scale
                x_extracted = (x_origin_unit*pow(10,modulo_tick))*pow(10,minor_tick)
                self.ui.label_x_extract.setText(str(format(x_extracted, '.2f')))
            if y_log == 0:
                y_extracted = y_origin_unit+((y_select-y_origin_px)*y_scale)
                self.ui.label_y_extract.setText(str(format(y_extracted, '.2f')))
            else:
                modulo_tick = int(y_select/y_scale)
                last_major_tick = modulo_tick * y_scale
                minor_tick =(y_select-y_origin_px-(modulo_tick*y_scale))/y_scale
                y_extracted = (y_origin_unit*pow(10,modulo_tick))*pow(10,minor_tick)
                self.ui.label_y_extract.setText(str(format(y_extracted, '.2f')))
            if event.button() == Qt.RightButton:
                self.store_data_point()
                self.ui.infobox.append('Saved x: %s'%(str(x_extracted)) + ' y: %s'%(str(y_extracted)))

        
    def calibrate(self):
        btn_name=self.sender()
        global x_select, y_select, x_origin_unit, y_origin_unit, x_origin_px, y_origin_px, x_scale, y_scale, x_calibrated, y_calibrated, x_log, y_log

        if btn_name == self.ui.btn_x1:
            x_origin_px=x_select
            try:
                x_origin_unit=float(self.ui.lineEdit_x1.text())
                self.ui.btn_x2.setEnabled(True)
            except:
                self.ui.infobox.append('Enter value!!')
        elif btn_name == self.ui.btn_x2:
            x_buffer_px=x_select
            try:
                x_buffer_unit = float(self.ui.lineEdit_x2.text())
                if self.ui.checkBox_log_x.isChecked() == True:
                    x_log = 1
                    x_scale = (x_buffer_px-x_origin_px)/m.log((x_buffer_unit/x_origin_unit),10)
                else:
                    x_log = 0
                    x_scale=(x_buffer_unit-x_origin_unit)/(x_buffer_px-x_origin_px)
                x_calibrated=1
            except:
                self.ui.infobox.append('Enter value!!')
        elif btn_name == self.ui.btn_y1:
            y_origin_px=y_select
            try:
                y_origin_unit=float(self.ui.lineEdit_y1.text())
                self.ui.btn_y2.setEnabled(True)
            except:
                self.ui.infobox.append('Enter value!!')
        elif btn_name == self.ui.btn_y2:
            y_buffer_px=y_select
            try:
                y_buffer_unit=float(self.ui.lineEdit_y2.text())
                if self.ui.checkBox_log_y.isChecked() == True:
                    y_log = 1
                    y_scale = (y_buffer_px-y_origin_px)/m.log((y_buffer_unit/y_origin_unit),10)
                else:
                    y_log = 0
                    y_scale=(y_buffer_unit-y_origin_unit)/(y_buffer_px-y_origin_px)
                y_calibrated = 1
            except:
                self.ui.infobox.append('Enter value!!')
        if x_calibrated == 1 and y_calibrated == 1:
            self.ui.label_status.setText('Calibrated!!!')
            self.ui.infobox.append('Calibration done!')
            self.ui.btn_delete_data.setEnabled(True)
            self.clear_marked_points()

    def store_data_point(self):
        global data_extracted_list, x_extracted, y_extracted
        if x_extracted is not None:
            if y_extracted is not None:
                data_extracted_list.append((x_extracted,y_extracted))

    def delete_last_point(self):
        global data_extracted_list
        if len(data_extracted_list)>0:
            del data_extracted_list[-1]
            print('Deleted last data point.')
            self.ui.infobox.append('Deleted last data point.')
        else:
            self.ui.infobox.append('How about selecting some data first?')

    def print_extracted_data(self):
        global data_extracted_list
        print(data_extracted_list)


app = QtWidgets.QApplication([])
 
win = mywindow()
 
win.show()
 
sys.exit(app.exec())

