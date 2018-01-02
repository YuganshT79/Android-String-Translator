# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
#
# Edited by Yugansh Tyagi on 02/01/2018

from PyQt4 import QtCore, QtGui
from xml.dom import minidom
from googletrans import Translator
import threading

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

# Globals
filename = "/"
progressValue = 0
totalStrings = 0


class Ui_mainWindows(object):

    def start_thread(self):
        self.showTransStrings.clear()   
        t1 = threading.Thread(target=self.start_translation)
        t1.start()

    def open_strings_file(self):
        print("Opening File")
        global filename
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open Android Strings File")
        file = open(filename, "r")
        print(str(filename))

        with file:
            text = file.read()
            self.showReadStrings.setText(text)

    def do_translation(self, fromLang, toLang):
        global progressValue
        progressValue = progressValue + 1
        print((totalStrings/100)*progressValue)
        translator = Translator()
        return translator.translate(fromLang, dest=toLang).text

    def start_translation(self):
        # translatedStringFile.delete('1.0', END)
        global filename
        print(str(self.langComboBox.currentText()))

        if str(self.langComboBox.currentText()) == "English, (en_US)":
            translate_to = "en"
        elif str(self.langComboBox.currentText()) == "German, Germany (de_DE)":
            translate_to = "de"
        elif str(self.langComboBox.currentText()) == "Chinese, PRC (zh_CN)":
            translate_to = "zh"
        elif str(self.langComboBox.currentText()) == "Czech, Czech Republic (cs_CZ)":
            translate_to = "cs"
        elif str(self.langComboBox.currentText()) == "Dutch, Belgium (nl_BE)":
            translate_to = "nl"
        elif str(self.langComboBox.currentText()) == "French, France (fr_FR)":
            translate_to = "fr"
        elif str(self.langComboBox.currentText()) == "Italian, Italy (it_IT)":
            translate_to = "it"
        elif str(self.langComboBox.currentText()) == "Japanese (ja_JP)":
            translate_to = "ja"
        elif str(self.langComboBox.currentText()) == "Korean (ko_KR)":
            translate_to = "ko"
        elif str(self.langComboBox.currentText()) == "Polish (pl_PL)":
            translate_to = "pl"
        elif str(self.langComboBox.currentText()) == "Russian (ru_RU)":
            translate_to = "ru"
        elif str(self.langComboBox.currentText()) == "Spanish (es_ES)":
            translate_to = "es"
        elif str(self.langComboBox.currentText()) == "Bulgarian, Bulgaria (bg_BG)":
            translate_to = "bg"
        elif str(self.langComboBox.currentText()) == "Catalan, Spain (ca_ES)":
            translate_to = "ca"
        elif str(self.langComboBox.currentText()) == "Danish, Denmark(da_DK)":
            translate_to = "da"
        elif str(self.langComboBox.currentText()) == "Greek, Greece (el_GR)":
            translate_to = "el"
        elif str(self.langComboBox.currentText()) == "Hindi, India (hi_IN)":
            translate_to = "hi"
        elif str(self.langComboBox.currentText()) == "Hungarian, Hungary (hu_HU)":
            translate_to = "hu"
        elif str(self.langComboBox.currentText()) == "Portuguese, Brazil (pt_BR)":
            translate_to = "pt"
        elif str(self.langComboBox.currentText()) == "Romanian, Romania (ro_RO)":
            translate_to = "ro"
        elif str(self.langComboBox.currentText()) == "Serbian (sr_RS)":
            translate_to = "sr"
        elif str(self.langComboBox.currentText()) == "Slovak, Slovakia (sk_SK)":
            translate_to = "sk"
        elif str(self.langComboBox.currentText()) == "Slovenian, Slovenia (sl_SI)":
            translate_to = "sl"
        elif str(self.langComboBox.currentText()) == "Spanish, US (es_US)":
            translate_to = "es"
        elif str(self.langComboBox.currentText()) == "Swedish, Sweden (sv_SE)":
            translate_to = "sv"
        elif str(self.langComboBox.currentText()) == "Thai, Thailand (th_TH)":
            translate_to = "th"
        elif str(self.langComboBox.currentText()) == "Turkish, Turkey (tr_TR)":
            translate_to = "hu"
        elif str(self.langComboBox.currentText()) == "Ukrainian, Ukraine (uk_UA)":
            translate_to = "uk"
        elif str(self.langComboBox.currentText()) == "Vietnamese, Vietnam (vi_VN)":
            translate_to = "vi"
        else:
            translate_to = ""

        print("Translating to : " + translate_to)
        if filename is not "/":
            global totalStrings
            print(filename)
            xmlDoc = minidom.parse(filename)
            stringList = xmlDoc.getElementsByTagName('string')

            totalStrings = int(len(stringList))
            print(totalStrings)
            self.progressBar.setProperty("maximum", totalStrings)

            for s in stringList:

                try:
                    try:
                        if s.attributes['translatable'].value == "false":
                            self.showTransStrings.insertPlainText("<string name=" + "\"" + s.attributes['name'].value
                                                                  + "\"" + " translatable=\"false\"" + ">"
                                                                  + s.firstChild.nodeValue + "</string>" + "\n")

                    except:
                            self.showTransStrings.insertPlainText("<string name=" + "\"" + s.attributes['name'].value + "\""
                                                              + ">"
                                                              + self.do_translation(s.firstChild.nodeValue, translate_to)
                                                              + "</string>" + "\n")

                except:
                    self.showTransStrings.insertPlainText("****Too many Tags in the String****  Name : "
                                                          + s.attributes['name'].value)
        else:
            print("Please select a File")

    def setupUi(self, mainWindows):
        mainWindows.setObjectName(_fromUtf8("mainWindows"))
        mainWindows.resize(1080, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("YT.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindows.setWindowIcon(icon)
        mainWindows.setAutoFillBackground(False)
        mainWindows.setStyleSheet(_fromUtf8(""))
        self.progName = QtGui.QLabel(mainWindows)
        self.progName.setGeometry(QtCore.QRect(160, 0, 821, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 240, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.progName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.progName.setFont(font)
        self.progName.setAutoFillBackground(False)
        self.progName.setStyleSheet(_fromUtf8(""))
        self.progName.setObjectName(_fromUtf8("progName"))
        self.langComboBox = QtGui.QComboBox(mainWindows)
        self.langComboBox.setGeometry(QtCore.QRect(30, 640, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.langComboBox.setFont(font)
        self.langComboBox.setObjectName(_fromUtf8("langComboBox"))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))
        self.langComboBox.addItem(_fromUtf8(""))

        self.openStringBtn = QtGui.QPushButton(mainWindows)
        self.openStringBtn.setGeometry(QtCore.QRect(30, 560, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.openStringBtn.setFont(font)
        self.openStringBtn.clicked.connect(self.open_strings_file)
        self.openStringBtn.setObjectName(_fromUtf8("openStringBtn"))

        self.beginTransBtn = QtGui.QPushButton(mainWindows)
        self.beginTransBtn.setGeometry(QtCore.QRect(550, 560, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.beginTransBtn.setFont(font)
        self.beginTransBtn.clicked.connect(self.start_thread)
        self.beginTransBtn.setObjectName(_fromUtf8("beginTransBtn"))

        self.progressBar = QtGui.QProgressBar(mainWindows)
        self.progressBar.setGeometry(QtCore.QRect(557, 642, 501, 51))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.showReadStrings = QtGui.QTextEdit(mainWindows)
        self.showReadStrings.setEnabled(True)
        self.showReadStrings.setReadOnly(True)
        self.showReadStrings.setGeometry(QtCore.QRect(30, 120, 501, 431))
        self.showReadStrings.setObjectName(_fromUtf8("showReadStrings"))

        self.showTransStrings = QtGui.QTextEdit(mainWindows)
        self.showTransStrings.setReadOnly(True)
        self.showTransStrings.setGeometry(QtCore.QRect(550, 120, 501, 431))
        self.showTransStrings.setObjectName(_fromUtf8("showTransStrings"))

        self.retranslateUi(mainWindows)
        QtCore.QMetaObject.connectSlotsByName(mainWindows)

    def retranslateUi(self, mainWindows):
        mainWindows.setWindowTitle(_translate("mainWindows", "Android String Translator", None))
        self.progName.setText(_translate("mainWindows", "<html><head/><body><p><span style=\" color:#ffffff;\">Android String Translator</span></p></body></html>", None))
        self.langComboBox.setItemText(0, _translate("mainWindows", "Select Translation Language ", None))
        self.langComboBox.setItemText(1, _translate("mainWindows", "English, (en_US)", None))
        self.langComboBox.setItemText(2, _translate("mainWindows", "German, Germany (de_DE)", None))
        self.langComboBox.setItemText(3, _translate("mainWindows", "Chinese, PRC (zh_CN)", None))
        self.langComboBox.setItemText(4, _translate("mainWindows", "Czech, Czech Republic (cs_CZ)", None))
        self.langComboBox.setItemText(5, _translate("mainWindows", "Dutch, Belgium (nl_BE)", None))
        self.langComboBox.setItemText(6, _translate("mainWindows", "French, France (fr_FR)", None))
        self.langComboBox.setItemText(7, _translate("mainWindows", "Italian, Italy (it_IT)", None))
        self.langComboBox.setItemText(8, _translate("mainWindows", "Japanese (ja_JP)", None))
        self.langComboBox.setItemText(9, _translate("mainWindows", "Korean (ko_KR)", None))
        self.langComboBox.setItemText(10, _translate("mainWindows", "Polish (pl_PL)", None))
        self.langComboBox.setItemText(11, _translate("mainWindows", "Russian (ru_RU)", None))
        self.langComboBox.setItemText(12, _translate("mainWindows", "Spanish (es_ES)", None))
        self.langComboBox.setItemText(13, _translate("mainWindows", "Bulgarian, Bulgaria (bg_BG)", None))
        self.langComboBox.setItemText(14, _translate("mainWindows", "Catalan, Spain (ca_ES)", None))
        self.langComboBox.setItemText(15, _translate("mainWindows", "Danish, Denmark(da_DK)", None))
        self.langComboBox.setItemText(16, _translate("mainWindows", "Greek, Greece (el_GR)", None))
        self.langComboBox.setItemText(17, _translate("mainWindows", "Hindi, India (hi_IN)", None))
        self.langComboBox.setItemText(18, _translate("mainWindows", "Hungarian, Hungary (hu_HU)", None))
        self.langComboBox.setItemText(19, _translate("mainWindows", "Portuguese, Brazil (pt_BR)", None))
        self.langComboBox.setItemText(20, _translate("mainWindows", "Romanian, Romania (ro_RO)", None))
        self.langComboBox.setItemText(21, _translate("mainWindows", "Serbian (sr_RS)", None))
        self.langComboBox.setItemText(22, _translate("mainWindows", "Slovak, Slovakia (sk_SK)", None))
        self.langComboBox.setItemText(23, _translate("mainWindows", "Slovenian, Slovenia (sl_SI)", None))
        self.langComboBox.setItemText(24, _translate("mainWindows", "Swedish, Sweden (sv_SE)", None))
        self.langComboBox.setItemText(25, _translate("mainWindows", "Thai, Thailand (th_TH)", None))
        self.langComboBox.setItemText(26, _translate("mainWindows", "Turkish, Turkey (tr_TR)", None))
        self.langComboBox.setItemText(27, _translate("mainWindows", "Ukrainian, Ukraine (uk_UA)", None))
        self.langComboBox.setItemText(28, _translate("mainWindows", "Vietnamese, Vietnam (vi_VN)", None))
        self.openStringBtn.setText(_translate("mainWindows", "Open Android String File", None))
        self.beginTransBtn.setText(_translate("mainWindows", "Begin String Translation", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindows = QtGui.QDialog()
    ui = Ui_mainWindows()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())

