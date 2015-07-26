# PyQt4 GUI / interface for MAX7219 LED Matrices
# www.scienceexposure.com

from PyQt4 import QtCore, QtGui
import sys
import numpy as np
try:
    from LEDController.functions import MatrixFunctions
    led_matrix = MatrixFunctions()
except ImportError:
    print('MAX7219 module or LEDController module missing. Program continuing...')

from datetime import date

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(296, 533)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 241, 251))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton_1 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_1.setText(_fromUtf8(""))
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setText(_fromUtf8(""))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_10 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_10.setText(_fromUtf8(""))
        self.radioButton_10.setAutoExclusive(False)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.gridLayout.addWidget(self.radioButton_10, 1, 1, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setText(_fromUtf8(""))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_9 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_9.setText(_fromUtf8(""))
        self.radioButton_9.setAutoExclusive(False)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.gridLayout.addWidget(self.radioButton_9, 1, 0, 1, 1)
        self.radioButton_8 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_8.setText(_fromUtf8(""))
        self.radioButton_8.setAutoExclusive(False)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.gridLayout.addWidget(self.radioButton_8, 0, 7, 1, 1)
        self.radioButton_12 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_12.setText(_fromUtf8(""))
        self.radioButton_12.setAutoExclusive(False)
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.gridLayout.addWidget(self.radioButton_12, 1, 3, 1, 1)
        self.radioButton_11 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_11.setText(_fromUtf8(""))
        self.radioButton_11.setAutoExclusive(False)
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.gridLayout.addWidget(self.radioButton_11, 1, 2, 1, 1)
        self.radioButton_13 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_13.setText(_fromUtf8(""))
        self.radioButton_13.setAutoExclusive(False)
        self.radioButton_13.setObjectName(_fromUtf8("radioButton_13"))
        self.gridLayout.addWidget(self.radioButton_13, 1, 4, 1, 1)
        self.radioButton_16 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_16.setText(_fromUtf8(""))
        self.radioButton_16.setAutoExclusive(False)
        self.radioButton_16.setObjectName(_fromUtf8("radioButton_16"))
        self.gridLayout.addWidget(self.radioButton_16, 1, 7, 1, 1)
        self.radioButton_14 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_14.setText(_fromUtf8(""))
        self.radioButton_14.setAutoExclusive(False)
        self.radioButton_14.setObjectName(_fromUtf8("radioButton_14"))
        self.gridLayout.addWidget(self.radioButton_14, 1, 5, 1, 1)
        self.radioButton_18 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_18.setText(_fromUtf8(""))
        self.radioButton_18.setAutoExclusive(False)
        self.radioButton_18.setObjectName(_fromUtf8("radioButton_18"))
        self.gridLayout.addWidget(self.radioButton_18, 2, 1, 1, 1)
        self.radioButton_21 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_21.setText(_fromUtf8(""))
        self.radioButton_21.setAutoExclusive(False)
        self.radioButton_21.setObjectName(_fromUtf8("radioButton_21"))
        self.gridLayout.addWidget(self.radioButton_21, 2, 4, 1, 1)
        self.radioButton_15 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_15.setText(_fromUtf8(""))
        self.radioButton_15.setAutoExclusive(False)
        self.radioButton_15.setObjectName(_fromUtf8("radioButton_15"))
        self.gridLayout.addWidget(self.radioButton_15, 1, 6, 1, 1)
        self.radioButton_17 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_17.setText(_fromUtf8(""))
        self.radioButton_17.setAutoExclusive(False)
        self.radioButton_17.setObjectName(_fromUtf8("radioButton_17"))
        self.gridLayout.addWidget(self.radioButton_17, 2, 0, 1, 1)
        self.radioButton_19 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_19.setText(_fromUtf8(""))
        self.radioButton_19.setAutoExclusive(False)
        self.radioButton_19.setObjectName(_fromUtf8("radioButton_19"))
        self.gridLayout.addWidget(self.radioButton_19, 2, 2, 1, 1)
        self.radioButton_20 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_20.setText(_fromUtf8(""))
        self.radioButton_20.setAutoExclusive(False)
        self.radioButton_20.setObjectName(_fromUtf8("radioButton_20"))
        self.gridLayout.addWidget(self.radioButton_20, 2, 3, 1, 1)
        self.radioButton_23 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_23.setText(_fromUtf8(""))
        self.radioButton_23.setAutoExclusive(False)
        self.radioButton_23.setObjectName(_fromUtf8("radioButton_23"))
        self.gridLayout.addWidget(self.radioButton_23, 2, 6, 1, 1)
        self.radioButton_28 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_28.setText(_fromUtf8(""))
        self.radioButton_28.setAutoExclusive(False)
        self.radioButton_28.setObjectName(_fromUtf8("radioButton_28"))
        self.gridLayout.addWidget(self.radioButton_28, 3, 3, 1, 1)
        self.radioButton_31 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_31.setText(_fromUtf8(""))
        self.radioButton_31.setAutoExclusive(False)
        self.radioButton_31.setObjectName(_fromUtf8("radioButton_31"))
        self.gridLayout.addWidget(self.radioButton_31, 3, 6, 1, 1)
        self.radioButton_26 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_26.setText(_fromUtf8(""))
        self.radioButton_26.setAutoExclusive(False)
        self.radioButton_26.setObjectName(_fromUtf8("radioButton_26"))
        self.gridLayout.addWidget(self.radioButton_26, 3, 1, 1, 1)
        self.radioButton_27 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_27.setText(_fromUtf8(""))
        self.radioButton_27.setAutoExclusive(False)
        self.radioButton_27.setObjectName(_fromUtf8("radioButton_27"))
        self.gridLayout.addWidget(self.radioButton_27, 3, 2, 1, 1)
        self.radioButton_22 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_22.setText(_fromUtf8(""))
        self.radioButton_22.setAutoExclusive(False)
        self.radioButton_22.setObjectName(_fromUtf8("radioButton_22"))
        self.gridLayout.addWidget(self.radioButton_22, 2, 5, 1, 1)
        self.radioButton_29 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_29.setText(_fromUtf8(""))
        self.radioButton_29.setAutoExclusive(False)
        self.radioButton_29.setObjectName(_fromUtf8("radioButton_29"))
        self.gridLayout.addWidget(self.radioButton_29, 3, 4, 1, 1)
        self.radioButton_30 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_30.setText(_fromUtf8(""))
        self.radioButton_30.setAutoExclusive(False)
        self.radioButton_30.setObjectName(_fromUtf8("radioButton_30"))
        self.gridLayout.addWidget(self.radioButton_30, 3, 5, 1, 1)
        self.radioButton_25 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_25.setText(_fromUtf8(""))
        self.radioButton_25.setAutoExclusive(False)
        self.radioButton_25.setObjectName(_fromUtf8("radioButton_25"))
        self.gridLayout.addWidget(self.radioButton_25, 3, 0, 1, 1)
        self.radioButton_24 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_24.setText(_fromUtf8(""))
        self.radioButton_24.setAutoExclusive(False)
        self.radioButton_24.setObjectName(_fromUtf8("radioButton_24"))
        self.gridLayout.addWidget(self.radioButton_24, 2, 7, 1, 1)
        self.radioButton_33 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_33.setText(_fromUtf8(""))
        self.radioButton_33.setAutoExclusive(False)
        self.radioButton_33.setObjectName(_fromUtf8("radioButton_33"))
        self.gridLayout.addWidget(self.radioButton_33, 4, 0, 1, 1)
        self.radioButton_5 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setText(_fromUtf8(""))
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.gridLayout.addWidget(self.radioButton_5, 0, 4, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setText(_fromUtf8(""))
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout.addWidget(self.radioButton_4, 0, 3, 1, 1)
        self.radioButton_32 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_32.setText(_fromUtf8(""))
        self.radioButton_32.setAutoExclusive(False)
        self.radioButton_32.setObjectName(_fromUtf8("radioButton_32"))
        self.gridLayout.addWidget(self.radioButton_32, 3, 7, 1, 1)
        self.radioButton_34 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_34.setText(_fromUtf8(""))
        self.radioButton_34.setAutoExclusive(False)
        self.radioButton_34.setObjectName(_fromUtf8("radioButton_34"))
        self.gridLayout.addWidget(self.radioButton_34, 4, 1, 1, 1)
        self.radioButton_7 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_7.setText(_fromUtf8(""))
        self.radioButton_7.setAutoExclusive(False)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.gridLayout.addWidget(self.radioButton_7, 0, 6, 1, 1)
        self.radioButton_6 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_6.setText(_fromUtf8(""))
        self.radioButton_6.setAutoExclusive(False)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.gridLayout.addWidget(self.radioButton_6, 0, 5, 1, 1)
        self.radioButton_36 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_36.setText(_fromUtf8(""))
        self.radioButton_36.setAutoExclusive(False)
        self.radioButton_36.setObjectName(_fromUtf8("radioButton_36"))
        self.gridLayout.addWidget(self.radioButton_36, 4, 3, 1, 1)
        self.radioButton_35 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_35.setText(_fromUtf8(""))
        self.radioButton_35.setAutoExclusive(False)
        self.radioButton_35.setObjectName(_fromUtf8("radioButton_35"))
        self.gridLayout.addWidget(self.radioButton_35, 4, 2, 1, 1)
        self.radioButton_39 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_39.setText(_fromUtf8(""))
        self.radioButton_39.setAutoExclusive(False)
        self.radioButton_39.setObjectName(_fromUtf8("radioButton_39"))
        self.gridLayout.addWidget(self.radioButton_39, 4, 6, 1, 1)
        self.radioButton_40 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_40.setText(_fromUtf8(""))
        self.radioButton_40.setAutoExclusive(False)
        self.radioButton_40.setObjectName(_fromUtf8("radioButton_40"))
        self.gridLayout.addWidget(self.radioButton_40, 4, 7, 1, 1)
        self.radioButton_37 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_37.setText(_fromUtf8(""))
        self.radioButton_37.setAutoExclusive(False)
        self.radioButton_37.setObjectName(_fromUtf8("radioButton_37"))
        self.gridLayout.addWidget(self.radioButton_37, 4, 4, 1, 1)
        self.radioButton_38 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_38.setText(_fromUtf8(""))
        self.radioButton_38.setAutoExclusive(False)
        self.radioButton_38.setObjectName(_fromUtf8("radioButton_38"))
        self.gridLayout.addWidget(self.radioButton_38, 4, 5, 1, 1)
        self.radioButton_44 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_44.setText(_fromUtf8(""))
        self.radioButton_44.setAutoExclusive(False)
        self.radioButton_44.setObjectName(_fromUtf8("radioButton_44"))
        self.gridLayout.addWidget(self.radioButton_44, 5, 3, 1, 1)
        self.radioButton_41 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_41.setText(_fromUtf8(""))
        self.radioButton_41.setAutoExclusive(False)
        self.radioButton_41.setObjectName(_fromUtf8("radioButton_41"))
        self.gridLayout.addWidget(self.radioButton_41, 5, 0, 1, 1)
        self.radioButton_43 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_43.setText(_fromUtf8(""))
        self.radioButton_43.setAutoExclusive(False)
        self.radioButton_43.setObjectName(_fromUtf8("radioButton_43"))
        self.gridLayout.addWidget(self.radioButton_43, 5, 2, 1, 1)
        self.radioButton_42 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_42.setText(_fromUtf8(""))
        self.radioButton_42.setAutoExclusive(False)
        self.radioButton_42.setObjectName(_fromUtf8("radioButton_42"))
        self.gridLayout.addWidget(self.radioButton_42, 5, 1, 1, 1)
        self.radioButton_45 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_45.setText(_fromUtf8(""))
        self.radioButton_45.setAutoExclusive(False)
        self.radioButton_45.setObjectName(_fromUtf8("radioButton_45"))
        self.gridLayout.addWidget(self.radioButton_45, 5, 4, 1, 1)
        self.radioButton_46 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_46.setText(_fromUtf8(""))
        self.radioButton_46.setAutoExclusive(False)
        self.radioButton_46.setObjectName(_fromUtf8("radioButton_46"))
        self.gridLayout.addWidget(self.radioButton_46, 5, 5, 1, 1)
        self.radioButton_49 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_49.setText(_fromUtf8(""))
        self.radioButton_49.setAutoExclusive(False)
        self.radioButton_49.setObjectName(_fromUtf8("radioButton_49"))
        self.gridLayout.addWidget(self.radioButton_49, 6, 0, 1, 1)
        self.radioButton_47 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_47.setText(_fromUtf8(""))
        self.radioButton_47.setAutoExclusive(False)
        self.radioButton_47.setObjectName(_fromUtf8("radioButton_47"))
        self.gridLayout.addWidget(self.radioButton_47, 5, 6, 1, 1)
        self.radioButton_48 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_48.setText(_fromUtf8(""))
        self.radioButton_48.setAutoExclusive(False)
        self.radioButton_48.setObjectName(_fromUtf8("radioButton_48"))
        self.gridLayout.addWidget(self.radioButton_48, 5, 7, 1, 1)
        self.radioButton_51 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_51.setText(_fromUtf8(""))
        self.radioButton_51.setAutoExclusive(False)
        self.radioButton_51.setObjectName(_fromUtf8("radioButton_51"))
        self.gridLayout.addWidget(self.radioButton_51, 6, 2, 1, 1)
        self.radioButton_50 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_50.setText(_fromUtf8(""))
        self.radioButton_50.setAutoExclusive(False)
        self.radioButton_50.setObjectName(_fromUtf8("radioButton_50"))
        self.gridLayout.addWidget(self.radioButton_50, 6, 1, 1, 1)
        self.radioButton_55 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_55.setText(_fromUtf8(""))
        self.radioButton_55.setAutoExclusive(False)
        self.radioButton_55.setObjectName(_fromUtf8("radioButton_55"))
        self.gridLayout.addWidget(self.radioButton_55, 6, 6, 1, 1)
        self.radioButton_52 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_52.setText(_fromUtf8(""))
        self.radioButton_52.setAutoExclusive(False)
        self.radioButton_52.setObjectName(_fromUtf8("radioButton_52"))
        self.gridLayout.addWidget(self.radioButton_52, 6, 3, 1, 1)
        self.radioButton_53 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_53.setText(_fromUtf8(""))
        self.radioButton_53.setAutoExclusive(False)
        self.radioButton_53.setObjectName(_fromUtf8("radioButton_53"))
        self.gridLayout.addWidget(self.radioButton_53, 6, 4, 1, 1)
        self.radioButton_54 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_54.setText(_fromUtf8(""))
        self.radioButton_54.setAutoExclusive(False)
        self.radioButton_54.setObjectName(_fromUtf8("radioButton_54"))
        self.gridLayout.addWidget(self.radioButton_54, 6, 5, 1, 1)
        self.radioButton_56 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_56.setText(_fromUtf8(""))
        self.radioButton_56.setAutoExclusive(False)
        self.radioButton_56.setObjectName(_fromUtf8("radioButton_56"))
        self.gridLayout.addWidget(self.radioButton_56, 6, 7, 1, 1)
        self.radioButton_57 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_57.setText(_fromUtf8(""))
        self.radioButton_57.setAutoExclusive(False)
        self.radioButton_57.setObjectName(_fromUtf8("radioButton_57"))
        self.gridLayout.addWidget(self.radioButton_57, 7, 0, 1, 1)
        self.radioButton_58 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_58.setText(_fromUtf8(""))
        self.radioButton_58.setAutoExclusive(False)
        self.radioButton_58.setObjectName(_fromUtf8("radioButton_58"))
        self.gridLayout.addWidget(self.radioButton_58, 7, 1, 1, 1)
        self.radioButton_59 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_59.setText(_fromUtf8(""))
        self.radioButton_59.setAutoExclusive(False)
        self.radioButton_59.setObjectName(_fromUtf8("radioButton_59"))
        self.gridLayout.addWidget(self.radioButton_59, 7, 2, 1, 1)
        self.radioButton_60 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_60.setText(_fromUtf8(""))
        self.radioButton_60.setAutoExclusive(False)
        self.radioButton_60.setObjectName(_fromUtf8("radioButton_60"))
        self.gridLayout.addWidget(self.radioButton_60, 7, 3, 1, 1)
        self.radioButton_61 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_61.setText(_fromUtf8(""))
        self.radioButton_61.setAutoExclusive(False)
        self.radioButton_61.setObjectName(_fromUtf8("radioButton_61"))
        self.gridLayout.addWidget(self.radioButton_61, 7, 4, 1, 1)
        self.radioButton_62 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_62.setText(_fromUtf8(""))
        self.radioButton_62.setAutoExclusive(False)
        self.radioButton_62.setObjectName(_fromUtf8("radioButton_62"))
        self.gridLayout.addWidget(self.radioButton_62, 7, 5, 1, 1)
        self.radioButton_63 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_63.setText(_fromUtf8(""))
        self.radioButton_63.setAutoExclusive(False)
        self.radioButton_63.setObjectName(_fromUtf8("radioButton_63"))
        self.gridLayout.addWidget(self.radioButton_63, 7, 6, 1, 1)
        self.radioButton_64 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_64.setText(_fromUtf8(""))
        self.radioButton_64.setAutoExclusive(False)
        self.radioButton_64.setObjectName(_fromUtf8("radioButton_64"))
        self.gridLayout.addWidget(self.radioButton_64, 7, 7, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 430, 241, 80))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)        
        self.pushButton.clicked.connect(self.updtMat)
        self.pushButton_2.clicked.connect(self.genMatrix)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MAX7219 LED Matrix - Raspberry Pi", None))
        self.pushButton.setText(_translate("Form", "Update matrix", None))
        self.pushButton_2.setText(_translate("Form", "Generate matrix", None))
        self.comboBox.setItemText(0, _translate("Form", "0", None))
        self.comboBox.setItemText(1, _translate("Form", "90", None))
        self.comboBox.setItemText(2, _translate("Form", "180", None))
        self.comboBox.setItemText(3, _translate("Form", "270", None))
        self.label.setText(_translate("Form", "Matrix orientation:", None))
        self.label_2.setText(_translate("Form", "Output style:", None))
        self.comboBox_2.setItemText(0, _translate("Form", "Numpy-style matrix", None))
        self.comboBox_2.setItemText(1, _translate("Form", "Binary", None))

    def updtMat(self):
        arr = np.array(np.zeros(64))
        orientation = int(self.comboBox.currentText())
        led_matrix.setOrientation(orientation)

        for i in range(1,65):
            method = getattr(self, "radioButton_%s" % i)
            a = method.isChecked()
            if a == True:
                arr[i-1] = 1
            else:
                pass
        matrix = arr.reshape(8,8)
        led_matrix.updateMatrix(matrix)


    def genMatrix(self):
        arr = np.array(np.zeros(64))

        for i in range(1,65):
            method = getattr(self, "radioButton_%s" % i)
            a = method.isChecked()
            if a == True:
                arr[i-1] = 1
            else:
                pass
        mx = arr.reshape(8,8)
        today = date.today()
        d = today.strftime('%d%m%Y')
        np.savetxt('%s_led_matrix.txt' % d,mx,fmt='%d',newline=',',delimiter=',')



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())