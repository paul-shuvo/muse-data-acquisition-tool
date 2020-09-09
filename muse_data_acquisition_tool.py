# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'muse_widget.ui'
#
# Created: Thu Mar 19 05:11:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
from __future__ import print_function
import subprocess, time, signal, sys, os
import lxml.etree
import lxml.builder
from datetime import date
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

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
        self.pushButton.setGeometry(QtCore.QRect(180, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
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
        self.pushButton.setText(_translate("Widget", "Start", None))
        self.radioButton_Male.setText(_translate("Widget", "Male", None))
        self.radioButton_Female.setText(_translate("Widget", "Female", None))

        self.pushButton.clicked.connect(self.Start_Muse)
        list1 = [
            self.tr('Experiment One'),
            self.tr('Experiment Two'),
            self.tr('Experiment Three'),
            self.tr('Experiment Four'),
            self.tr('Experiment Five'),
            self.tr('Experiment Six'),
            ]
        self.comboBox.clear()
        self.comboBox.addItems(list1)
        # self.comboBox.addItem(self, "Video1")
        # self.comboBox.addItem(self, "Video2")
        # self.comboBox.addItem(self, "Video4")


    def Start_Muse(self):
        E = lxml.builder.ElementMaker()
        CVCR = E.cvcr
        today = date.today()
        today=today.strftime('%d%m%Y')
        fileName=today+"_"+self.lineEdit_serial.text()
        #fileName=self.lineEdit_serial.text()+'_'+self.lineEdit_name.text()+'_'+self.lineEdit_age.text()
        if self.radioButton_Male.isChecked():
            str=self.radioButton_Male.text()
        else:
            str=self.radioButton_Female.text()
        print(str)
        #fileName=fileName+'_'+str+'_'+self.comboBox.currentText()
        vid_dir=''
        if self.comboBox.currentText() == 'Experiment One':
            vid_dir='Exp1.mp4'
            # fileName=fileName+'_'+str+'_'+'Experiment1'
            fileName=fileName+'_'+'Experiment1'
        elif self.comboBox.currentText() == 'Experiment Two':
            vid_dir='Exp2.mp4'
            fileName=fileName+'_'+'Experiment2'
        elif self.comboBox.currentText() == 'Experiment Three':
            vid_dir='Exp3.mp4'
            fileName=fileName+'_'+'Experiment3'
        else :
            vid_dir='Exp4.mp4'
            fileName=fileName+'_'+str+'_'+'Experiment4'
        print (fileName)
        #fileName=str(fileName)
        save_xml(E, today, self.lineEdit_name.text(), self.lineEdit_age.text(), self.lineEdit_serial.text(), str)
        vid_player(vid_dir, fileName)

def save_xml(E, date, name, age, serial, gender):
    #CVCR=E.cvcr
    SUBJECT = E.subject
    DATE = E.date
    SERIAL = E.serial
    NAME = E.name
    AGE = E.age
    GENDER = E.gender
    val='1'
    #the_doc =()
    the_doc=(SUBJECT(DATE(date),SERIAL(str(serial)),NAME(str(name)),AGE(str(age)),GENDER(str(gender)), ID=str(serial)))
    # the_doc.append(SUBJECT(DATE('date'),SERIAL('serial'),NAME('name'),AGE('age'),GENDER('gender'), ID=s))


    # the_doc.append(DOC(FIELD1('another value again', name='hithere'), name='hithere'))
    # the_doc.append(DOC())

    DOC = lxml.etree.tostring(the_doc, pretty_print=True)
    output_file = open( 'cvcr.xml', 'a' )
    output_file.seek(20)
    #output_file.write( '<?xml version="1.0"?>' )
    output_file.write(DOC)
    output_file.close()
    
def signal_handler(signal, frame):
    time.sleep(1)
    print('Ctrl+C received in wrapper.py') 

def save_data(sleep_time, muse_command):
    command=muse_command

    #command = "muse-player -l udp:5001 -M output.mat"
    

    signal.signal(signal.SIGINT, signal_handler)
    print 'command Starting'
    subprocess.Popen(command)
    print 'command started'
    time.sleep(sleep_time)
    print 'Timeout Completed'
    os.kill(signal.CTRL_C_EVENT, 0)

def vid_player(vid_dir, fileName):
    vid_dir = "F:\\"+vid_dir
    print(vid_dir)
    command= "\"F:\Program Files (x86)\VideoLAN\VLC"+"\\""vlc.exe\" --fullscreen "+vid_dir#\"F:\Exp1.mp4\""
    muse_command="muse-player -l udp:5001 -M " +fileName+".mat"
    muse_command=str(muse_command)
    print(command)
    print(muse_command)
    #subprocess.Popen(muse_command)
    subprocess.Popen(command)
    time.sleep(1)
    save_data(5, muse_command)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('CVCR')
    window = Ui_Widget()
    window.show()
    sys.exit(app.exec_())
