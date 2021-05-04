#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:53:28 2020

@author: vgk
"""
import cv2
import numpy as np
import statistics as stat
import sys
import math as m
import subprocess
try:
    subprocess.call("pyuic5 graph_grabber_gui_02.ui -o graph_grabber_gui_02.py", shell=True)
except:
    print('Error: You are not using ubuntu and/or you have not installed pyuic5 module. The .ui file could be outdated.')

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
        self.ui.btn_GetDataPoints.clicked.connect(self.get_data_points)
        self.ui.btn_BottomLeft.clicked.connect(self.DataExtractionLimits)
        self.ui.btn_TopRight.clicked.connect(self.DataExtractionLimits)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.reset()
        # self.ui.pushButton.clicked.connect(self.reSize_image)
        self.ScaleFactor = 1.05
        self.pixmap = None
        self.filename = None
        self.image_width, self.image_height = None, None
        self.cv2image = None
        self.RedSelect, self.GreenSelect, self.BlueSelect = None, None, None

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
        self.RedSelect, self.GreenSelect, self.BlueSelect = None, None, None
        self.GetDataLimit1, self.GetDataLimit2 = None, None
        x_log, y_log = 0, 0
        self.ScaleFactor = 1.05
        self.ui.infobox.append('Data reset')

    # def wheelEvent(self, event):
    #     d = event.angleDelta().y()
    #     x = event.position().x()
    #     y = event.position().y()
    #     self.reSize_image(d,x,y)

    # def reSize_image(self,scroll,x,y):
    #     # print(icon_label.pixmap().size())
    #     if scroll>0:
    #         #self.icon_label.resize(1.05 * self.icon_label.size())
    #         offset_x = (x-self.widget_pos_x-self.label_pos_x) * (0.05)
    #         offset_y = (y-self.widget_pos_y-self.label_pos_y) * (0.05)
    #         label_width = (self.icon_label.size().width())*1.05
    #         label_height = (self.icon_label.size().height())*1.05
    #         self.icon_label.setGeometry(self.label_pos_x-offset_x, self.label_pos_y-offset_y, label_width, label_height)
    #     elif scroll<0:
    #         self.icon_label.resize(0.95 * self.icon_label.size())

    def fit_image(self):
        self.icon_label.setGeometry(self.label_pos_x, self.label_pos_y, self.image_label_width, self.image_label_height)
        self.ScaleFactor = 1.05

    def load_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()","","",options=options) #png(*.png),jpg(*.jpg)
        if self.filename:
            # name = 'label_3'
            # icon_label = self.findChild(QLabel, name)
            self.pixmap = QPixmap(self.filename)
            self.image_width = self.pixmap.size().width()
            self.image_height = self.pixmap.size().height()
            self.icon_label.setScaledContents(True)
            self.icon_label.setPixmap(self.pixmap)
            #load image using cv2
            self.cv2image = cv2.imread(self.filename)

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
        self.painterInstance.drawPoint(int((x-offset_x)/scale_width), int((y-offset_y)/scale_height))

        # set pixmap onto the label widget
        self.icon_label.setPixmap(self.pixmap)
        self.icon_label.show()
        self.painterInstance.end()

    def LabelToImageCoordinates(self,x_select, y_select):
        scale_width = self.icon_label.size().width() / self.image_width
        scale_height = self.icon_label.size().height() / self.image_height
        offset_x = self.widget_pos_x + self.label_pos_x
        offset_y = self.widget_pos_y + self.label_pos_y
        x_pixel, y_pixel = int((x_select - offset_x) / scale_width), int((y_select - offset_y) / scale_height)
        return x_pixel, y_pixel

    def get_pixel_RGB(self,x_select,y_select):
        x_pixel, y_pixel = self.LabelToImageCoordinates(x_select,y_select)
        img = self.pixmap.toImage()
        c = img.pixel(x_pixel, y_pixel)
        colors = QColor(c).getRgbF()
        # print('x:{} y:{}'.format(x_pixel, y_pixel))
        # print(self.cv2image[y_pixel,x_pixel])
        return 255*colors[0], 255*colors[1], 255*colors[2]

    def RGB_to_H(self,r,g,b):
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        if r<0.05 and g<0.05 and b<0.05:
            h,s,v = 0,0,0
        else:
            mx = max(r, g, b)
            mn = min(r, g, b)
            df = mx - mn
            if mx == mn:
                h = 0
            elif mx == r:
                h = (60 * ((g - b) / df) + 360) % 360
            elif mx == g:
                h = (60 * ((b - r) / df) + 120) % 360
            elif mx == b:
                h = (60 * ((r - g) / df) + 240) % 360
            s, v =255, 255
        return int(h*0.5), s, v #divding h by 2 as required by cv2

    def DataExtractionLimits(self):
        global x_select, y_select
        x_pixel, y_pixel = self.LabelToImageCoordinates(x_select, y_select)
        sender = self.sender().text()
        if sender.find('Bottom') != -1:
            self.GetDataLimit1 = None
            self.GetDataLimit1 = [x_pixel,y_pixel]
        else:
            self.GetDataLimit2 = None
            self.GetDataLimit2 = [x_pixel,y_pixel]

    def filter_image(self, img, H, S, V):
        # Convert the img to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Limits
        H1 = H - 15 if H - 15 > 0 else 0
        H2 = H + 15 if H + 15 < 180 else 180

        if H==0 and S==0 and V==0:
            # mask
            lower_red = np.array([0, 0, 0])
            upper_red = np.array([100, 10, 10])
            mask = cv2.inRange(img_hsv, lower_red, upper_red)
            # Apply mask to HSV image
            output_hsv_1 = img_hsv.copy()
            output_hsv_1[np.where(mask == 0)] = [90, 255, 255]
            output_hsv_1[np.where(mask == 255)] = [0, 255, 255]
            lower2 = np.array([0, 255, 255])
            upper2 = np.array([5, 255, 255])
            mask2 = cv2.inRange(output_hsv_1, lower2, upper2)
            output_hsv = output_hsv_1.copy()
            output_hsv[np.where(mask2 == 0)] = 0
        else:
            # mask
            lower_red = np.array([H1, 100, 100])
            upper_red = np.array([H2, 255, 255])
            mask = cv2.inRange(img_hsv, lower_red, upper_red)
            # Apply mask to HSV image
            output_hsv = img_hsv.copy()
            output_hsv[np.where(mask == 0)] = 0

        return output_hsv

    def get_data_points(self):
        print('R:{} G:{} B:{}'.format(self.RedSelect,self.GreenSelect,self.BlueSelect))
        h, s, v = self.RGB_to_H(self.RedSelect,self.GreenSelect,self.BlueSelect)
        # print('H:{}'.format(h))
        output_hsv = self.filter_image(self.cv2image,h,s,v)
        points = int(self.ui.lineEdit_DataPoints.text())
        print('Extracting {} data points'.format(points))
        if self.GetDataLimit1 is None and self.GetDataLimit2 is None:
            height_min, width_min = 0, 0
            height_max = output_hsv.shape[0]
            width_max = output_hsv.shape[1]
        else:
            height_min, height_max = min([self.GetDataLimit1[1],self.GetDataLimit2[1]]), max([self.GetDataLimit1[1],self.GetDataLimit2[1]])
            width_min, width_max = min([self.GetDataLimit1[0], self.GetDataLimit2[0]]), max([self.GetDataLimit1[0], self.GetDataLimit2[0]])
        step = int((width_max-width_min) / points)
        data = []
        for i in range(0, points):
            col = width_min + i * step
            buffer_list_H, buffer_list_S, buffer_list_V, buffer_list_row = [], [], [], []
            for row in range(height_min, height_max - 1):
                buffer_list_H.append(output_hsv[row, col][0])
                buffer_list_S.append(output_hsv[row, col][1])
                buffer_list_V.append(output_hsv[row, col][2])
                buffer_list_row.append(row)
            y_weight_list = []
            for y_index in range(0, len(buffer_list_H)):
                if buffer_list_H[y_index]>0 or buffer_list_S[y_index]>0 or buffer_list_V[y_index]>0:
                    y_weight_list.append(buffer_list_row[y_index])
            try:
                y_point = int(stat.mean(y_weight_list))
                x_point = col
                data.append([x_point, y_point])
            except:
                pass
        self.mark_data_point(data)
        print(data)

    def mark_data_point(self,data):

        # create painter instance with pixmap
        self.painterInstance = QtGui.QPainter(self.pixmap)

        # set rectangle color and thickness
        self.penRectangle = QtGui.QPen(QtCore.Qt.cyan)
        self.penRectangle.setWidth(5)

        # draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        for point in data:
            self.painterInstance.drawPoint(point[0],point[1])

        # set pixmap onto the label widget
        self.icon_label.setPixmap(self.pixmap)
        self.icon_label.show()
        self.painterInstance.end()

    def mousePressEvent(self, event):
        if self.pixmap is not None:
            x_min, y_min = self.widget_pos_x + self.label_pos_x, self.widget_pos_y + self.label_pos_y
            x_max, y_max = x_min + self.icon_label.size().width(), y_min + self.icon_label.size().height()
            if event.x() > x_min and event.x() < x_max and event.y() > y_min and event.y() < y_max:
                global x_select, y_select, x_extracted, y_extracted
                x_select, y_select = event.x(), event.y()
                # print('x:%i'%x_select + ' y:%i'%y_select)
                self.RedSelect, self.GreenSelect, self.BlueSelect = self.get_pixel_RGB(x_select,y_select)
                # print('R: {} ; G: {} ; B: {}'.format(self.RedSelect, self.GreenSelect, self.BlueSelect))
                self.ui.label_pixel_color.setStyleSheet("background-color:rgb({},{},{})".format(self.RedSelect, self.GreenSelect, self.BlueSelect))
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

