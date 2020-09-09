from __future__ import print_function
from PyQt4 import QtCore, QtGui
from lxml import builder
from util import save_xml, save_data, vid_player, signal_handler
from datetime import date
from experiments import *

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

class Ui_Widget(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(444, 423)
        self.label = QtGui.QLabel(self)
        self.label_name.setGeometry(QtCore.QRect(50, 60, 81, 31))
        self.label_name.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setObjectName(_fromUtf8("label"))
        self.label_age = QtGui.QLabel(self)
        self.label_age.setGeometry(QtCore.QRect(50, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_age.setFont(font)
        self.label_age.setObjectName(_fromUtf8("label_2"))
        self.label_gender = QtGui.QLabel(self)
        self.label_gender.setGeometry(QtCore.QRect(50, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName(_fromUtf8("label_3"))
        self.label_serial = QtGui.QLabel(self)
        self.label_serial.setGeometry(QtCore.QRect(50, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_serial.setFont(font)
        self.label_serial.setObjectName(_fromUtf8("label_4"))
        self.label_experiment = QtGui.QLabel(self)
        self.label_experiment.setGeometry(QtCore.QRect(50, 260, 111, 31))
        self.label_experiment.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_experiment.setFont(font)
        self.label_experiment.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton_startsetGeometry(QtCore.QRect(180, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.pushButton_startsetFont(font)
        self.pushButton_startsetObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(170, 260, 181, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit_name.setGeometry(QtCore.QRect(170, 59, 181, 31))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_age = QtGui.QLineEdit(self)
        self.lineEdit_age.setGeometry(QtCore.QRect(170, 109, 181, 31))
        self.lineEdit_age.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_serial = QtGui.QLineEdit(self)
        self.lineEdit_serial.setGeometry(QtCore.QRect(170, 209, 181, 31))
        self.lineEdit_serial.setObjectName(_fromUtf8("lineEdit_3"))
        self.radioButton = QtGui.QRadioButton(self)
        self.radioButton_Male.setGeometry(QtCore.QRect(170, 170, 82, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.radioButton_Male.setFont(font)
        self.radioButton_Male.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_Female = QtGui.QRadioButton(self)
        self.radioButton_Female.setGeometry(QtCore.QRect(280, 170, 82, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.radioButton_Female.setFont(font)
        self.radioButton_Female.setObjectName(_fromUtf8("radioButton_2"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("CVCR", "CVCR", None))
        self.label_name.setText(_translate("Widget", "Name", None))
        self.label_age.setText(_translate("Widget", "Age", None))
        self.label_gender.setText(_translate("Widget", "Gender", None))
        self.label_serial.setText(_translate("Widget", "Serial No.", None))
        self.label_experiment.setText(_translate("Widget", "Exp. No.", None))
        self.pushButton_startsetText(_translate("Widget", "Start", None))
        self.radioButton_Male.setText(_translate("Widget", "Male", None))
        self.radioButton_Female.setText(_translate("Widget", "Female", None))

        self.pushButton_startclicked.connect(self.start_muse)
        self.experiment_list = [self.tr(f'Experiment {experiment_num}') for experiment_num in range(1,7)]
        
        self.comboBox.clear()
        self.comboBox.addItems(self.experiment_list)



    def start_muse(self):
        Elm = builder.ElementMaker()
        # CVCR = Elm.cvcr
        today = date.today().strftime('%d%m%Y')
        #fileName=self.lineEdit_serial.text()+'_'+self.lineEdit_name.text()+'_'+self.lineEdit_age.text()
        if self.radioButton_Male.isChecked():
            str = self.radioButton_Male.text()
        else:
            str = self.radioButton_Female.text()
        print(str)
        #fileName=fileName+'_'+str+'_'+self.comboBox.currentText()
        save_xml(Elm, today, self.lineEdit_name.text(), self.lineEdit_age.text(), self.lineEdit_serial.text(), str)

        experiments = Experiments(experiment_args)
        fileName = today +  "_" + self.lineEdit_serial.text() + '_' + self.comboBox.currentText
        experiments.start_experiment(self.comboBox.currentText, fileName)




if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('CVCR')
    window = Ui_Widget()
    window.show()
    sys.exit(app.exec_())
