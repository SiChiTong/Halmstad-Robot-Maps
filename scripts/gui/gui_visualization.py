# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_visualization.ui'
#
# Created: Wed Jul 26 19:19:18 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1888, 1084)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_src_load = QtGui.QPushButton(self.centralwidget)
        self.pushButton_src_load.setGeometry(QtCore.QRect(10, 950, 130, 27))
        self.pushButton_src_load.setObjectName("pushButton_src_load")
        self.comboBox_tform_type = QtGui.QComboBox(self.centralwidget)
        self.comboBox_tform_type.setGeometry(QtCore.QRect(1080, 950, 201, 24))
        self.comboBox_tform_type.setObjectName("comboBox_tform_type")
        self.comboBox_tform_type.addItem("")
        self.comboBox_tform_type.addItem("")
        self.comboBox_tform_type.addItem("")
        self.comboBox_tform_type.addItem("")
        self.comboBox_tform_type.addItem("")
        self.textEdit_src_path = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_src_path.setGeometry(QtCore.QRect(146, 951, 660, 26))
        self.textEdit_src_path.setReadOnly(False)
        self.textEdit_src_path.setObjectName("textEdit_src_path")
        self.pushButton_dst_load = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dst_load.setGeometry(QtCore.QRect(10, 979, 130, 27))
        self.pushButton_dst_load.setObjectName("pushButton_dst_load")
        self.textEdit_dst_path = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_dst_path.setGeometry(QtCore.QRect(146, 980, 660, 26))
        self.textEdit_dst_path.setReadOnly(False)
        self.textEdit_dst_path.setObjectName("textEdit_dst_path")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(983, 953, 91, 20))
        self.label_7.setObjectName("label_7")
        self.textEdit_tform_frw = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_tform_frw.setGeometry(QtCore.QRect(1381, 950, 240, 80))
        self.textEdit_tform_frw.setReadOnly(False)
        self.textEdit_tform_frw.setObjectName("textEdit_tform_frw")
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1380, 930, 240, 21))
        self.label_8.setObjectName("label_8")
        self.checkBox_show_keypoints = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_show_keypoints.setGeometry(QtCore.QRect(1080, 980, 110, 21))
        self.checkBox_show_keypoints.setChecked(True)
        self.checkBox_show_keypoints.setObjectName("checkBox_show_keypoints")
        self.pushButton_src_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_src_next.setGeometry(QtCore.QRect(886, 950, 70, 27))
        self.pushButton_src_next.setObjectName("pushButton_src_next")
        self.pushButton_src_previous = QtGui.QPushButton(self.centralwidget)
        self.pushButton_src_previous.setGeometry(QtCore.QRect(816, 950, 70, 27))
        self.pushButton_src_previous.setObjectName("pushButton_src_previous")
        self.pushButton_dst_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dst_next.setGeometry(QtCore.QRect(886, 980, 70, 27))
        self.pushButton_dst_next.setObjectName("pushButton_dst_next")
        self.pushButton_dst_previous = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dst_previous.setGeometry(QtCore.QRect(816, 980, 70, 27))
        self.pushButton_dst_previous.setObjectName("pushButton_dst_previous")
        self.graphicsView_main = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_main.setGeometry(QtCore.QRect(10, 10, 1871, 921))
        self.graphicsView_main.setObjectName("graphicsView_main")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1640, 930, 240, 21))
        self.label_9.setObjectName("label_9")
        self.textEdit_tform_inv = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_tform_inv.setGeometry(QtCore.QRect(1640, 950, 240, 80))
        self.textEdit_tform_inv.setReadOnly(False)
        self.textEdit_tform_inv.setObjectName("textEdit_tform_inv")
        self.checkBox_show_association = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_show_association.setGeometry(QtCore.QRect(1080, 1000, 111, 21))
        self.checkBox_show_association.setChecked(True)
        self.checkBox_show_association.setObjectName("checkBox_show_association")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1888, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_src_load.setText(QtGui.QApplication.translate("MainWindow", "Load Source Map", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tform_type.setItemText(0, QtGui.QApplication.translate("MainWindow", "similarity", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tform_type.setItemText(1, QtGui.QApplication.translate("MainWindow", "polynomial", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tform_type.setItemText(2, QtGui.QApplication.translate("MainWindow", "affine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tform_type.setItemText(3, QtGui.QApplication.translate("MainWindow", "piecewise-affine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tform_type.setItemText(4, QtGui.QApplication.translate("MainWindow", "projective", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dst_load.setText(QtGui.QApplication.translate("MainWindow", "Load Destination Map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Transform Class</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Forward Transform Matrix </span>(5 points precision)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_show_keypoints.setText(QtGui.QApplication.translate("MainWindow", "show key points", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_src_next.setText(QtGui.QApplication.translate("MainWindow", "Next>>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_src_previous.setText(QtGui.QApplication.translate("MainWindow", "<< Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dst_next.setText(QtGui.QApplication.translate("MainWindow", "Next>>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dst_previous.setText(QtGui.QApplication.translate("MainWindow", "<< Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Forward Transform Matrix </span>(5 points precision)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_show_association.setText(QtGui.QApplication.translate("MainWindow", "show association", None, QtGui.QApplication.UnicodeUTF8))
