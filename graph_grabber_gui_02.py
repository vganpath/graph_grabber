# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_grabber_gui_02.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1060)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(290, 830, 291, 120))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_y1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_y1.setObjectName("lineEdit_y1")
        self.gridLayout_2.addWidget(self.lineEdit_y1, 2, 2, 1, 1)
        self.btn_x1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_x1.setObjectName("btn_x1")
        self.gridLayout_2.addWidget(self.btn_x1, 0, 1, 1, 1)
        self.btn_x2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_x2.setObjectName("btn_x2")
        self.gridLayout_2.addWidget(self.btn_x2, 1, 1, 1, 1)
        self.btn_y1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_y1.setObjectName("btn_y1")
        self.gridLayout_2.addWidget(self.btn_y1, 2, 1, 1, 1)
        self.btn_y2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_y2.setObjectName("btn_y2")
        self.gridLayout_2.addWidget(self.btn_y2, 3, 1, 1, 1)
        self.lineEdit_x2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_x2.setObjectName("lineEdit_x2")
        self.gridLayout_2.addWidget(self.lineEdit_x2, 1, 2, 1, 1)
        self.lineEdit_y2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_y2.setObjectName("lineEdit_y2")
        self.gridLayout_2.addWidget(self.lineEdit_y2, 3, 2, 1, 1)
        self.lineEdit_x1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_x1.setObjectName("lineEdit_x1")
        self.gridLayout_2.addWidget(self.lineEdit_x1, 0, 2, 1, 1)
        self.checkBox_log_x = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_log_x.setObjectName("checkBox_log_x")
        self.gridLayout_2.addWidget(self.checkBox_log_x, 0, 0, 1, 1)
        self.checkBox_log_y = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_log_y.setObjectName("checkBox_log_y")
        self.gridLayout_2.addWidget(self.checkBox_log_y, 2, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(630, 820, 160, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_x_select = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_x_select.setFrameShape(QtWidgets.QFrame.Box)
        self.label_x_select.setObjectName("label_x_select")
        self.gridLayout_3.addWidget(self.label_x_select, 0, 1, 1, 1)
        self.label_y_select = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_y_select.setFrameShape(QtWidgets.QFrame.Box)
        self.label_y_select.setObjectName("label_y_select")
        self.gridLayout_3.addWidget(self.label_y_select, 1, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(820, 810, 101, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 810, 160, 182))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_reset = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout.addWidget(self.btn_reset)
        self.btn_load = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_load.setObjectName("btn_load")
        self.verticalLayout.addWidget(self.btn_load)
        self.btn_ScaleImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ScaleImage.setEnabled(False)
        self.btn_ScaleImage.setObjectName("btn_ScaleImage")
        self.verticalLayout.addWidget(self.btn_ScaleImage)
        self.btn_clear_image = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_clear_image.setObjectName("btn_clear_image")
        self.verticalLayout.addWidget(self.btn_clear_image)
        self.btn_delete_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_delete_data.setObjectName("btn_delete_data")
        self.verticalLayout.addWidget(self.btn_delete_data)
        self.btn_print_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_print_data.setObjectName("btn_print_data")
        self.verticalLayout.addWidget(self.btn_print_data)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(630, 910, 131, 17))
        self.label_status.setObjectName("label_status")
        self.infobox = QtWidgets.QTextBrowser(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(630, 940, 181, 41))
        self.infobox.setObjectName("infobox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 810, 281, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 950, 211, 41))
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 1301, 791))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 411, 271))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(930, 810, 311, 141))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_x_extract = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_x_extract.setFont(font)
        self.label_x_extract.setFrameShape(QtWidgets.QFrame.Box)
        self.label_x_extract.setObjectName("label_x_extract")
        self.gridLayout_4.addWidget(self.label_x_extract, 0, 0, 1, 1)
        self.label_y_extract = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_y_extract.setFont(font)
        self.label_y_extract.setFrameShape(QtWidgets.QFrame.Box)
        self.label_y_extract.setObjectName("label_y_extract")
        self.gridLayout_4.addWidget(self.label_y_extract, 1, 0, 1, 1)
        self.label_pixel_color = QtWidgets.QLabel(self.centralwidget)
        self.label_pixel_color.setGeometry(QtCore.QRect(890, 960, 91, 21))
        self.label_pixel_color.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pixel_color.setText("")
        self.label_pixel_color.setObjectName("label_pixel_color")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_x1.setText(_translate("MainWindow", "x-1"))
        self.btn_x2.setText(_translate("MainWindow", "x-2"))
        self.btn_y1.setText(_translate("MainWindow", "y-1"))
        self.btn_y2.setText(_translate("MainWindow", "y-2"))
        self.checkBox_log_x.setText(_translate("MainWindow", "Log"))
        self.checkBox_log_y.setText(_translate("MainWindow", "Log"))
        self.label.setText(_translate("MainWindow", "x [px]:"))
        self.label_2.setText(_translate("MainWindow", "y [px]:"))
        self.label_x_select.setText(_translate("MainWindow", "TextLabel"))
        self.label_y_select.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "x [unit]:"))
        self.label_5.setText(_translate("MainWindow", "y [unit]:"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_load.setText(_translate("MainWindow", "Load image"))
        self.btn_ScaleImage.setText(_translate("MainWindow", "Scale image"))
        self.btn_clear_image.setText(_translate("MainWindow", "Clear image"))
        self.btn_delete_data.setText(_translate("MainWindow", "Delete last point"))
        self.btn_print_data.setText(_translate("MainWindow", "Print data"))
        self.label_status.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Calibration:"))
        self.label_7.setText(_translate("MainWindow", "Right click to save data point after calibration."))
        self.label_x_extract.setText(_translate("MainWindow", "TextLabel"))
        self.label_y_extract.setText(_translate("MainWindow", "TextLabel"))
