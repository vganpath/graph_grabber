#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:53:28 2020

@author: vgk
"""

import pyautogui
import pyscreenshot as ImageGrab

"""
a=pyautogui.position()

print(a)
print(a[0])
print(a[1])

#part of the screen
im = ImageGrab.grab(bbox=(a[0], a[1], 1000, 1000))  # X1,Y1,X2,Y2

# save image file
im.save("box.png")

"""

import os
import sys

from graph_grabber_gui_01 import * #UI file

from PyQt5.QtWidgets import* #QMainWindow, QApplication, QPushButton, QTextEdit, QLabel, QLCDNumber
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5 import QtWidgets,uic

p1_x,p1_y,p2_x,p2_y=0,0,1000,1000

class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
 
        super().__init__()
 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_save.clicked.connect(self.save_image) #
       
    def keyPressEvent(self, event):
        global p1_x,p1_y,p2_x,p2_y
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Q:
                a=pyautogui.position()
                print(a)
                p1_x=a[0]
                p1_y=a[1]
            elif event.key() == QtCore.Qt.Key_W:
                a=pyautogui.position()
                print(a)
                p2_x=a[0]
                p2_y=a[1]
                
    def save_image(self):
        global p1_x,p1_y,p2_x,p2_y
        im=ImageGrab.grab(bbox=(p1_x,p1_y,(p2_x-p1_x),(p2_y-p1_y))) 
        im.save("box.png")
        self.display_image()
    
    def display_image(self):
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap("box.png")
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)
        
        

app = QtWidgets.QApplication([])
 
win = mywindow()
 
win.show()
 
sys.exit(app.exec())
