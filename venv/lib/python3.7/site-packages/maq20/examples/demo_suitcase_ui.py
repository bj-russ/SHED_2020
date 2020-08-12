# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_suitcase.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 601)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QtWidgets.QFrame.Box)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23, 0, QtCore.Qt.AlignHCenter)
        self.led_bar_control_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.led_bar_control_checkbox.setObjectName("led_bar_control_checkbox")
        self.horizontalLayout_5.addWidget(self.led_bar_control_checkbox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_11.addWidget(self.line_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.tc_heat_1_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.tc_heat_1_spinbox.setDecimals(1)
        self.tc_heat_1_spinbox.setMinimum(-10.0)
        self.tc_heat_1_spinbox.setMaximum(10.0)
        self.tc_heat_1_spinbox.setSingleStep(0.5)
        self.tc_heat_1_spinbox.setObjectName("tc_heat_1_spinbox")
        self.verticalLayout_9.addWidget(self.tc_heat_1_spinbox)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.tc_heat_2_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.tc_heat_2_spinbox.setDecimals(1)
        self.tc_heat_2_spinbox.setMinimum(-10.0)
        self.tc_heat_2_spinbox.setMaximum(10.0)
        self.tc_heat_2_spinbox.setSingleStep(0.5)
        self.tc_heat_2_spinbox.setObjectName("tc_heat_2_spinbox")
        self.verticalLayout_9.addWidget(self.tc_heat_2_spinbox, 0, QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.int_tc_spinbox_indicator = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.int_tc_spinbox_indicator.setReadOnly(True)
        self.int_tc_spinbox_indicator.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.int_tc_spinbox_indicator.setMinimum(-5000.0)
        self.int_tc_spinbox_indicator.setMaximum(1000.0)
        self.int_tc_spinbox_indicator.setObjectName("int_tc_spinbox_indicator")
        self.verticalLayout_9.addWidget(self.int_tc_spinbox_indicator)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.tc_touch_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tc_touch_line_edit.sizePolicy().hasHeightForWidth())
        self.tc_touch_line_edit.setSizePolicy(sizePolicy)
        self.tc_touch_line_edit.setMaximumSize(QtCore.QSize(90, 16777215))
        self.tc_touch_line_edit.setObjectName("tc_touch_line_edit")
        self.verticalLayout_12.addWidget(self.tc_touch_line_edit)
        self.verticalLayout_9.addLayout(self.verticalLayout_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.freq_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq_slider.sizePolicy().hasHeightForWidth())
        self.freq_slider.setSizePolicy(sizePolicy)
        self.freq_slider.setStyleSheet("Slider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"stop: 0 rgb(255, 200, 200), stop: 1 rgb(255, 0, 40));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:vertical:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:vertical:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.freq_slider.setMinimum(0)
        self.freq_slider.setMaximum(10000)
        self.freq_slider.setSingleStep(500)
        self.freq_slider.setPageStep(500)
        self.freq_slider.setSliderPosition(1000)
        self.freq_slider.setOrientation(QtCore.Qt.Vertical)
        self.freq_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.freq_slider.setObjectName("freq_slider")
        self.verticalLayout_5.addWidget(self.freq_slider)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.freq_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.freq_spinbox.setEnabled(True)
        self.freq_spinbox.setReadOnly(True)
        self.freq_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.freq_spinbox.setKeyboardTracking(True)
        self.freq_spinbox.setProperty("showGroupSeparator", False)
        self.freq_spinbox.setDecimals(3)
        self.freq_spinbox.setMaximum(11.0)
        self.freq_spinbox.setObjectName("freq_spinbox")
        self.verticalLayout_5.addWidget(self.freq_spinbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.vout1_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vout1_slider.sizePolicy().hasHeightForWidth())
        self.vout1_slider.setSizePolicy(sizePolicy)
        self.vout1_slider.setStyleSheet("Slider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"stop: 0 rgb(255, 220, 220), stop: 1 rgb(255, 170, 0));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:vertical:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:vertical:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.vout1_slider.setMinimum(-10)
        self.vout1_slider.setMaximum(10)
        self.vout1_slider.setSingleStep(1)
        self.vout1_slider.setPageStep(1)
        self.vout1_slider.setTracking(True)
        self.vout1_slider.setOrientation(QtCore.Qt.Vertical)
        self.vout1_slider.setInvertedAppearance(False)
        self.vout1_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vout1_slider.setObjectName("vout1_slider")
        self.verticalLayout_6.addWidget(self.vout1_slider)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.vout1_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.vout1_spinbox.setEnabled(True)
        self.vout1_spinbox.setReadOnly(True)
        self.vout1_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.vout1_spinbox.setMinimum(-11.0)
        self.vout1_spinbox.setMaximum(11.0)
        self.vout1_spinbox.setObjectName("vout1_spinbox")
        self.verticalLayout_6.addWidget(self.vout1_spinbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sw1 = QtWidgets.QCheckBox(self.centralwidget)
        self.sw1.setEnabled(False)
        self.sw1.setObjectName("sw1")
        self.horizontalLayout_6.addWidget(self.sw1)
        self.sw1_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw1_slider.sizePolicy().hasHeightForWidth())
        self.sw1_slider.setSizePolicy(sizePolicy)
        self.sw1_slider.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.sw1_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.sw1_slider.setMaximum(1)
        self.sw1_slider.setPageStep(1)
        self.sw1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sw1_slider.setObjectName("sw1_slider")
        self.horizontalLayout_6.addWidget(self.sw1_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sw2 = QtWidgets.QCheckBox(self.centralwidget)
        self.sw2.setEnabled(False)
        self.sw2.setObjectName("sw2")
        self.horizontalLayout_7.addWidget(self.sw2)
        self.sw2_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw2_slider.sizePolicy().hasHeightForWidth())
        self.sw2_slider.setSizePolicy(sizePolicy)
        self.sw2_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sw2_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.sw2_slider.setMaximum(1)
        self.sw2_slider.setPageStep(1)
        self.sw2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sw2_slider.setObjectName("sw2_slider")
        self.horizontalLayout_7.addWidget(self.sw2_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sw3 = QtWidgets.QCheckBox(self.centralwidget)
        self.sw3.setEnabled(False)
        self.sw3.setObjectName("sw3")
        self.horizontalLayout_8.addWidget(self.sw3)
        self.sw3_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw3_slider.sizePolicy().hasHeightForWidth())
        self.sw3_slider.setSizePolicy(sizePolicy)
        self.sw3_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sw3_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.sw3_slider.setMaximum(1)
        self.sw3_slider.setPageStep(1)
        self.sw3_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sw3_slider.setObjectName("sw3_slider")
        self.horizontalLayout_8.addWidget(self.sw3_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sw4 = QtWidgets.QCheckBox(self.centralwidget)
        self.sw4.setEnabled(False)
        self.sw4.setObjectName("sw4")
        self.horizontalLayout_9.addWidget(self.sw4)
        self.sw4_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw4_slider.sizePolicy().hasHeightForWidth())
        self.sw4_slider.setSizePolicy(sizePolicy)
        self.sw4_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sw4_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.sw4_slider.setMaximum(1)
        self.sw4_slider.setPageStep(1)
        self.sw4_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sw4_slider.setObjectName("sw4_slider")
        self.horizontalLayout_9.addWidget(self.sw4_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sw5 = QtWidgets.QCheckBox(self.centralwidget)
        self.sw5.setEnabled(False)
        self.sw5.setObjectName("sw5")
        self.horizontalLayout_10.addWidget(self.sw5)
        self.sw5_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw5_slider.sizePolicy().hasHeightForWidth())
        self.sw5_slider.setSizePolicy(sizePolicy)
        self.sw5_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sw5_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.sw5_slider.setMaximum(1)
        self.sw5_slider.setPageStep(1)
        self.sw5_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sw5_slider.setObjectName("sw5_slider")
        self.horizontalLayout_10.addWidget(self.sw5_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter)
        self.vout2_slider = QtWidgets.QSlider(self.centralwidget)
        self.vout2_slider.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vout2_slider.sizePolicy().hasHeightForWidth())
        self.vout2_slider.setSizePolicy(sizePolicy)
        self.vout2_slider.setAutoFillBackground(False)
        self.vout2_slider.setStyleSheet("Slider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"stop: 0 rgb(180, 220, 220), stop: 1 rgb(85, 255, 0));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:vertical:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:vertical:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.vout2_slider.setMinimum(-10)
        self.vout2_slider.setMaximum(10)
        self.vout2_slider.setPageStep(1)
        self.vout2_slider.setOrientation(QtCore.Qt.Vertical)
        self.vout2_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vout2_slider.setObjectName("vout2_slider")
        self.verticalLayout_7.addWidget(self.vout2_slider)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.vout2_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.vout2_spinbox.setReadOnly(True)
        self.vout2_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.vout2_spinbox.setMinimum(-11.0)
        self.vout2_spinbox.setMaximum(11.0)
        self.vout2_spinbox.setObjectName("vout2_spinbox")
        self.verticalLayout_7.addWidget(self.vout2_spinbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19, 0, QtCore.Qt.AlignHCenter)
        self.vout3_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vout3_slider.sizePolicy().hasHeightForWidth())
        self.vout3_slider.setSizePolicy(sizePolicy)
        self.vout3_slider.setStyleSheet("Slider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:vertical:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:vertical:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.vout3_slider.setMinimum(-10)
        self.vout3_slider.setMaximum(10)
        self.vout3_slider.setPageStep(1)
        self.vout3_slider.setOrientation(QtCore.Qt.Vertical)
        self.vout3_slider.setInvertedAppearance(False)
        self.vout3_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vout3_slider.setObjectName("vout3_slider")
        self.verticalLayout_8.addWidget(self.vout3_slider)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.vout3_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.vout3_spinbox.setReadOnly(True)
        self.vout3_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.vout3_spinbox.setMinimum(-11.0)
        self.vout3_spinbox.setMaximum(11.0)
        self.vout3_spinbox.setObjectName("vout3_spinbox")
        self.verticalLayout_8.addWidget(self.vout3_spinbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.motor_pot_1 = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motor_pot_1.sizePolicy().hasHeightForWidth())
        self.motor_pot_1.setSizePolicy(sizePolicy)
        self.motor_pot_1.setMaximum(20)
        self.motor_pot_1.setPageStep(1)
        self.motor_pot_1.setNotchesVisible(True)
        self.motor_pot_1.setObjectName("motor_pot_1")
        self.verticalLayout_2.addWidget(self.motor_pot_1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.motor_pot_2 = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motor_pot_2.sizePolicy().hasHeightForWidth())
        self.motor_pot_2.setSizePolicy(sizePolicy)
        self.motor_pot_2.setAutoFillBackground(False)
        self.motor_pot_2.setMaximum(20)
        self.motor_pot_2.setPageStep(1)
        self.motor_pot_2.setNotchesVisible(True)
        self.motor_pot_2.setObjectName("motor_pot_2")
        self.verticalLayout_2.addWidget(self.motor_pot_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_11.addWidget(self.line_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.ip_address_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_address_line.setObjectName("ip_address_line")
        self.horizontalLayout_11.addWidget(self.ip_address_line)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.port_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.port_spinbox.setMinimum(1)
        self.port_spinbox.setMaximum(1000)
        self.port_spinbox.setProperty("value", 502)
        self.port_spinbox.setObjectName("port_spinbox")
        self.horizontalLayout_11.addWidget(self.port_spinbox)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.status_line = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.status_line.setFont(font)
        self.status_line.setFrame(False)
        self.status_line.setReadOnly(True)
        self.status_line.setObjectName("status_line")
        self.horizontalLayout_11.addWidget(self.status_line)
        self.connection_switch = QtWidgets.QSlider(self.centralwidget)
        self.connection_switch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_switch.sizePolicy().hasHeightForWidth())
        self.connection_switch.setSizePolicy(sizePolicy)
        self.connection_switch.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.connection_switch.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0  rgb(200,255,200), stop: 1 rgb(0,255,0));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #aaa;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background:  rgb(0,255,0);\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.connection_switch.setMaximum(1)
        self.connection_switch.setPageStep(1)
        self.connection_switch.setProperty("value", 0)
        self.connection_switch.setOrientation(QtCore.Qt.Horizontal)
        self.connection_switch.setObjectName("connection_switch")
        self.horizontalLayout_11.addWidget(self.connection_switch)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout_12.addWidget(self.connect_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.motor_pot_2, self.motor_pot_1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAQ20 Demo Suitcase"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">MAQ20 Process Simulator Demonstration System</span></p><p><span style=\" font-weight:600;\"/></p><p>The MAQ20 Process Simulator Demonstration System was developed by Dataforth in order to showcase the operation of the MAQ20 system. The demonstration consists of the minimum size MAQ20-BKPL4 backbone having 4 IO modules slots. Modules within the system cover the basic functionality of a data acquisition and control system, modules include: </p><p/><p>MAQ20-COM4 Communication Module Supporting RS485, Ethernet and USB connectivity </p><p>MAQ20-JTC 8 Channel J Type Thermocouple Input Module </p><p>MAQ20-VO 8 Channel Voltage Output Module </p><p>MAQ20-VDN 8 Channel Differential Voltage Input </p><p>MAQ20-DIOL 10 Channel (5 In 5 Out) Digital IO Module With Special Functions </p></body></html>"))
        self.label_23.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-weight:600; color:#cc7832;\">from </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6;\">maq20 </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#cc7832;\">import </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6;\">MAQ20</span><span style=\" font-family:\'Courier New\'; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6;\">MAQ20Module<br/></span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#cc7832;\">from </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6;\">maq20.modules </span><span style=\" font-family:\'Courier New\'; font-weight:600; color:#cc7832;\">import </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6;\">outputmodule</span><span style=\" font-family:\'Courier New\'; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; color:#a9b7c6; background-color:#344134;\">diol</span></pre></body></html>"))
        self.label_23.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">MAQ20 Process Simulator Demonstration System</span><span style=\" font-size:12pt;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\"/><span style=\" font-size:12pt; font-weight:400;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\">The MAQ20 Process Simulator Demonstration System was developed by Dataforth in order to showcase the operation of the MAQ20 system. The demonstration consists of the minimum size MAQ20-BKPL4 backbone having 4 IO modules slots. Modules within the system cover the basic functionality of a data acquisition and control system, modules include: </span></p><p><span style=\" font-size:12pt; font-weight:400;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-COM4 Communication Module Supporting RS485, Ethernet and USB connectivity </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-JTC 8 Channel J Type Thermocouple Input Module </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-VO 8 Channel Voltage Output Module </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-VDN 8 Channel Differential Voltage Input </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-DIOL 10 Channel (5 In 5 Out) Digital IO Module With Special Functions </span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "API imports"))
        self.led_bar_control_checkbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">if </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">p_bool:<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">10</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">else</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">:<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=-</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">10</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.led_bar_control_checkbox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">LED Bar 3, 4 &amp; LED Bar Control</span></p><p>LED Bars 3 &amp; 4 can be operated via two methods controlled by the LED Bard Control input, wired to VO CH 1. When LED Bar Control is set to its lowest value (-10V) LED Bars 3 &amp; 4 are controlled by VO CH 2 &amp; 3 respectively. When the LED Bar Control is set to its highest value (+10V) LED Bar 3 &amp; 4 are controlled by Motor Pot 1 &amp; 2 respectively. </p></body></html>"))
        self.led_bar_control_checkbox.setText(_translate("MainWindow", "LED BAR CONTROL"))
        self.label_10.setText(_translate("MainWindow", "INT. TC HEAT 1"))
        self.tc_heat_1_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=p_double)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">tc_heat_1 = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_channel_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.tc_heat_1_spinbox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Internal Heater Control 1 &amp; 2 and Internal TC</span></p><p>Two internal heating elements bonded to an internal thermocouple. When the heater controls are enabled using channels VO Channels 4 &amp; 5 the temperature of the internal thermocouple is raised, the voltage at the heating elements can be read back on channels VDN 5 &amp; 6. The internal thermocouple is wired to JTC Channel 6. </p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "INT. TC HEAT 2"))
        self.tc_heat_2_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=p_double)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">tc_heat_2 = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_channel_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.tc_heat_2_spinbox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Internal Heater Control 1 &amp; 2 and Internal TC</span></p><p>Two internal heating elements bonded to an internal thermocouple. When the heater controls are enabled using channels VO Channels 4 &amp; 5 the temperature of the internal thermocouple is raised, the voltage at the heating elements can be read back on channels VDN 5 &amp; 6. The internal thermocouple is wired to JTC Channel 6. </p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "INT_TC"))
        self.int_tc_spinbox_indicator.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.int_tc_spinbox_indicator.setValue(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.jtc.read_channel_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">6</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">))</span></pre></body></html>"))
        self.int_tc_spinbox_indicator.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Internal Heater Control 1 &amp; 2 and Internal TC</span></p><p>Two internal heating elements bonded to an internal thermocouple. When the heater controls are enabled using channels VO Channels 4 &amp; 5 the temperature of the internal thermocouple is raised, the voltage at the heating elements can be read back on channels VDN 5 &amp; 6. The internal thermocouple is wired to JTC Channel 6. </p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "EXT. TC TOUCH"))
        self.tc_touch_line_edit.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">module_channel = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">7<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">ext_temperature = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.jtc.read_channel_data(module_channel)</span></pre></body></html>"))
        self.tc_touch_line_edit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">External Touch TC</span></p><p>J type thermocouple with touch pad interfaced to JTC CH 7. </p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "+FS"))
        self.freq_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.write_special_function_5_frequency_generator(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">timer</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">frequency</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=p_int)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">frequency = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_register(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1105</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.freq_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Frequency Output Control &amp; LED Bar 1</span></p><p>Frequency output control uses the DIOL modules special function for generating a square waveform up to 10 kHz, the DIOL output is wired to the input of a frequency to voltage converter which is used as an input to LED Bar 1 (red), this value can read back within the system on VDN CH 4. Each DIOL modules features 2 timers that can be used to provide timed special functions such as PWM output, Pulse Counter, Event Timer and more. In this case of the frequency generator used here timer 0 is used to produce the special function behaviour and is output on CH OUT 0. </p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "FREQ"))
        self.freq_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">frequency = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_register(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1105</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.freq_spinbox.setValue(frequency/</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1000.0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.label_17.setText(_translate("MainWindow", "+FS"))
        self.vout1_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">voltages = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vout1_slider.setValue(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#8888c6;\">round</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(voltages[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">]))</span></pre></body></html>"))
        self.vout1_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">LED Bar 2</span></p><p>LED Bar 2 is controlled directly by VO CH 0. </p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "-FS"))
        self.label_4.setText(_translate("MainWindow", "VOUT1"))
        self.vout1_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">voltages = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vout1_spinbox.setValue(voltages[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">])</span></pre></body></html>"))
        self.sw1.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw1.setText(_translate("MainWindow", "SW1"))
        self.sw1_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw1_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p><p><br/></p></body></html>"))
        self.sw2.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw2.setText(_translate("MainWindow", "SW2"))
        self.sw2_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw2_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw3.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw3.setText(_translate("MainWindow", "SW3"))
        self.sw3_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw3_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw4.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw4.setText(_translate("MainWindow", "SW4"))
        self.sw4_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw4_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw5.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.sw5.setText(_translate("MainWindow", "SW5"))
        self.sw5_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">_update_switches</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">):<br/>    values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">5</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw1_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw2_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw3_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw4_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5.setChecked(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.sw5_slider.setValue(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">] ^ </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre></body></html>"))
        self.sw5_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SW1-5 Digital Inputs</span></p><p>Switch inputs use TTL logic levels and are active low, LEDs light when the input to the MAQ20 DIOL modules is low. Switches are interfaced to DIOL CH 0-4. </p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "+FS"))
        self.vout2_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">vout2_slider_val</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">p_int):<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">if not </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.led_bar_control_checkbox.isChecked():<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.led_bar_control_checkbox.toggle()<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">try</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">:<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=p_int)</span></pre></body></html>"))
        self.vout2_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">LED Bar 3, 4 &amp; LED Bar Control</span></p><p>LED Bars 3 &amp; 4 can be operated via two methods controlled by the LED Bard Control input, wired to VO CH 1. When LED Bar Control is set to its lowest value (-10V) LED Bars 3 &amp; 4 are controlled by VO CH 2 &amp; 3 respectively. When the LED Bar Control is set to its highest value (+10V) LED Bar 3 &amp; 4 are controlled by Motor Pot 1 &amp; 2 respectively. </p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "-FS"))
        self.label_5.setText(_translate("MainWindow", "VOUT2"))
        self.vout2_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">voltages = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vout2_spinbox.setValue(voltages[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">])</span></pre></body></html>"))
        self.label_19.setText(_translate("MainWindow", "+FS"))
        self.vout3_slider.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">def </span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#a9b7c6;\">vout3_slider_val</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">p_int):<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">if not </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.led_bar_control_checkbox.isChecked():<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.led_bar_control_checkbox.toggle()<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:600; color:#cc7832;\">try</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">:<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.write_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">data</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=p_int)</span></pre></body></html>"))
        self.vout3_slider.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">LED Bar 3, 4 &amp; LED Bar Control</span></p><p>LED Bars 3 &amp; 4 can be operated via two methods controlled by the LED Bard Control input, wired to VO CH 1. When LED Bar Control is set to its lowest value (-10V) LED Bars 3 &amp; 4 are controlled by VO CH 2 &amp; 3 respectively. When the LED Bar Control is set to its highest value (+10V) LED Bar 3 &amp; 4 are controlled by Motor Pot 1 &amp; 2 respectively. </p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "-FS"))
        self.label_6.setText(_translate("MainWindow", "VOUT3"))
        self.vout3_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">voltages = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">4</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">).</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vout3_spinbox.setValue(voltages[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">])</span></pre></body></html>"))
        self.motor_pot_1.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#2b2b2b;\">values = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vdn.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">start_channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">number_of_channels</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#344134;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.motor_pot_1.setValue(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#8888c6;\">round</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">]*(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">20.0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">/</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3.3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)))</span></pre></body></html>"))
        self.motor_pot_1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Motor Pots 1 &amp; 2</span></p><p>Rotation of Motor Pots 1 &amp; 2 is controlled by CH 1-4 of the DIOL module outputs. Each pot has a forward and reverse control and is interlocked in logic to provide the truth table show below: </p><p/><p align=\"center\"><br/></p><table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\"><tr><td width=\"57\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Action</span></p></td><td width=\"66\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">OUT 1</span></p></td><td width=\"68\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">OUT 2</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Stop</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Forward</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Reverse</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Stop</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td></tr><tr><td colspan=\"3\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-style:italic;\">Figure 3: Motor Pot Truth Table</span></p></td></tr></table><p/><p>When the LED Bar Control is set high (+10V) motor pot position are displayed on LED Bar 3 &amp; 4 on the process simulator panel. Each motor pot is wired to two inputs of the VDN module, the first inputs is full scale 0 to +10V, the second inputs level shifted to 0 to +3V. Finally the rotational speed of each motor pot can be modified using VO Channels 6 &amp; 7, setting the output to &lt;=0 means the motor pots will not rotate when the digital control signals are asserted. Setting the output to &gt;0 will increase the rotation speed the maximum value is +10V this will rotate the motor pots at their maximum rate. </p></body></html>"))
        self.label.setText(_translate("MainWindow", "MOTOR POT 1"))
        self.motor_pot_2.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#40332b;\">values</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\"> = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vdn.read_data(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">start_channel</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">number_of_channels</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">2</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6; background-color:#344134;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.motor_pot_2.setValue(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#8888c6;\">round</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">(values[</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">1</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">]*(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">20.0</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">/</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#6897bb;\">3.3</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)))</span></pre></body></html>"))
        self.motor_pot_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Motor Pots 1 &amp; 2</span></p><p>Rotation of Motor Pots 1 &amp; 2 is controlled by CH 1-4 of the DIOL module outputs. Each pot has a forward and reverse control and is interlocked in logic to provide the truth table show below: </p><p/><p align=\"center\"><br/></p><table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\"><tr><td width=\"57\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Action</span></p></td><td width=\"66\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">OUT 1</span></p></td><td width=\"68\" bgcolor=\"#d9d9d9\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">OUT 2</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Stop</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Forward</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Reverse</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">0</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p><span style=\" font-size:8pt; font-weight:600;\">Stop</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:8pt;\">1</span></p></td></tr><tr><td colspan=\"3\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-style:italic;\">Figure 3: Motor Pot Truth Table</span></p></td></tr></table><p/><p>When the LED Bar Control is set high (+10V) motor pot position are displayed on LED Bar 3 &amp; 4 on the process simulator panel. Each motor pot is wired to two inputs of the VDN module, the first inputs is full scale 0 to +10V, the second inputs level shifted to 0 to +3V. Finally the rotational speed of each motor pot can be modified using VO Channels 6 &amp; 7, setting the output to &lt;=0 means the motor pots will not rotate when the digital control signals are asserted. Setting the output to &gt;0 will increase the rotation speed the maximum value is +10V this will rotate the motor pots at their maximum rate. </p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "MOTOR POT 2"))
        self.label_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">MAQ20 Process Simulator Demonstration System</span><span style=\" font-size:12pt;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\"/><span style=\" font-size:12pt; font-weight:400;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\">The MAQ20 Process Simulator Demonstration System was developed by Dataforth in order to showcase the operation of the MAQ20 system. The demonstration consists of the minimum size MAQ20-BKPL4 backbone having 4 IO modules slots. Modules within the system cover the basic functionality of a data acquisition and control system, modules include: </span></p><p><span style=\" font-size:12pt; font-weight:400;\"/></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-COM4 Communication Module Supporting RS485, Ethernet and USB connectivity </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-JTC 8 Channel J Type Thermocouple Input Module </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-VO 8 Channel Voltage Output Module </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-VDN 8 Channel Differential Voltage Input </span></p><p><span style=\" font-size:12pt; font-weight:400;\">MAQ20-DIOL 10 Channel (5 In 5 Out) Digital IO Module With Special Functions </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "PROCESS SIMULATOR"))
        self.label_12.setText(_translate("MainWindow", "IP Address:"))
        self.ip_address_line.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20 = MAQ20(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">ip_address</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.ip_address_line.displayText()</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">port</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.port_spinbox.value())</span></pre></body></html>"))
        self.ip_address_line.setText(_translate("MainWindow", "192.168.128.100"))
        self.label_13.setText(_translate("MainWindow", "Port"))
        self.port_spinbox.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20 = MAQ20(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">ip_address</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.ip_address_line.displayText()</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">port</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.port_spinbox.value())</span></pre></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Status:"))
        self.status_line.setText(_translate("MainWindow", "No Connection"))
        self.connect_button.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20 = MAQ20(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">ip_address</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.ip_address_line.displayText()</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#cc7832;\">, </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#aa4926;\">port</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">=</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.port_spinbox.value())<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.jtc = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20.find(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#008080;\">&quot;JTC&quot;</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vdn = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20.find(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#008080;\">&quot;VDN&quot;</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/>vo = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20.find(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#008080;\">&quot;VO&quot;</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/>dio = </span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.maq20.find(</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#008080;\">&quot;DIOL&quot;</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.vo = outputmodule.OutputModule(vo)<br/></span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#94558d;\">self</span><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#a9b7c6;\">.diol = diol.DIOL(dio)</span></pre></body></html>"))
        self.connect_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">MAQ20 Process Simulator Demonstration System</span></p><p><span style=\" font-weight:600;\"/></p><p>The MAQ20 Process Simulator Demonstration System was developed by Dataforth in order to showcase the operation of the MAQ20 system. The demonstration consists of the minimum size MAQ20-BKPL4 backbone having 4 IO modules slots. Modules within the system cover the basic functionality of a data acquisition and control system, modules include: </p><p/><p>MAQ20-COM4 Communication Module Supporting RS485, Ethernet and USB connectivity </p><p>MAQ20-JTC 8 Channel J Type Thermocouple Input Module </p><p>MAQ20-VO 8 Channel Voltage Output Module </p><p>MAQ20-VDN 8 Channel Differential Voltage Input </p><p>MAQ20-DIOL 10 Channel (5 In 5 Out) Digital IO Module With Special Functions </p></body></html>"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

