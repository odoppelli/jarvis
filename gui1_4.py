# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_1_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import weather
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 443)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(174, 174, 174);\n"
                                 "color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameWeather = QtWidgets.QFrame(self.centralwidget)
        self.frameWeather.setGeometry(QtCore.QRect(0, 200, 800, 230))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.frameWeather.setFont(font)
        self.frameWeather.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWeather.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWeather.setObjectName("frameWeather")
        self.uhrzeit1 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit1.setGeometry(QtCore.QRect(25, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit1.setFont(font)
        self.uhrzeit1.setStyleSheet("")
        self.uhrzeit1.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit1.setObjectName("uhrzeit1")
        self.image1 = QtWidgets.QLabel(self.frameWeather)
        self.image1.setGeometry(QtCore.QRect(25, 40, 80, 80))
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap("icons/01d.png"))
        self.image1.setScaledContents(True)
        self.image1.setAlignment(QtCore.Qt.AlignCenter)
        self.image1.setObjectName("image1")
        self.temperatur1 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur1.setGeometry(QtCore.QRect(25, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur1.setFont(font)
        self.temperatur1.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur1.setObjectName("temperatur1")
        self.wind1 = QtWidgets.QLabel(self.frameWeather)
        self.wind1.setGeometry(QtCore.QRect(25, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind1.setFont(font)
        self.wind1.setAlignment(QtCore.Qt.AlignCenter)
        self.wind1.setObjectName("wind1")
        self.regen1 = QtWidgets.QLabel(self.frameWeather)
        self.regen1.setGeometry(QtCore.QRect(25, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen1.setFont(font)
        self.regen1.setAlignment(QtCore.Qt.AlignCenter)
        self.regen1.setObjectName("regen1")
        self.regen2 = QtWidgets.QLabel(self.frameWeather)
        self.regen2.setGeometry(QtCore.QRect(155, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen2.setFont(font)
        self.regen2.setAlignment(QtCore.Qt.AlignCenter)
        self.regen2.setObjectName("regen2")
        self.uhrzeit2 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit2.setGeometry(QtCore.QRect(155, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit2.setFont(font)
        self.uhrzeit2.setStyleSheet("")
        self.uhrzeit2.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit2.setObjectName("uhrzeit2")
        self.temperatur2 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur2.setGeometry(QtCore.QRect(155, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur2.setFont(font)
        self.temperatur2.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur2.setObjectName("temperatur2")
        self.wind2 = QtWidgets.QLabel(self.frameWeather)
        self.wind2.setGeometry(QtCore.QRect(155, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind2.setFont(font)
        self.wind2.setAlignment(QtCore.Qt.AlignCenter)
        self.wind2.setObjectName("wind2")
        self.image2 = QtWidgets.QLabel(self.frameWeather)
        self.image2.setGeometry(QtCore.QRect(155, 40, 80, 80))
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap("icons/02d.png"))
        self.image2.setScaledContents(True)
        self.image2.setAlignment(QtCore.Qt.AlignCenter)
        self.image2.setObjectName("image2")
        self.regen3 = QtWidgets.QLabel(self.frameWeather)
        self.regen3.setGeometry(QtCore.QRect(285, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen3.setFont(font)
        self.regen3.setAlignment(QtCore.Qt.AlignCenter)
        self.regen3.setObjectName("regen3")
        self.uhrzeit3 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit3.setGeometry(QtCore.QRect(285, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit3.setFont(font)
        self.uhrzeit3.setStyleSheet("")
        self.uhrzeit3.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit3.setObjectName("uhrzeit3")
        self.temperatur3 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur3.setGeometry(QtCore.QRect(285, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur3.setFont(font)
        self.temperatur3.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur3.setObjectName("temperatur3")
        self.wind3 = QtWidgets.QLabel(self.frameWeather)
        self.wind3.setGeometry(QtCore.QRect(285, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind3.setFont(font)
        self.wind3.setAlignment(QtCore.Qt.AlignCenter)
        self.wind3.setObjectName("wind3")
        self.image3 = QtWidgets.QLabel(self.frameWeather)
        self.image3.setGeometry(QtCore.QRect(285, 40, 80, 80))
        self.image3.setText("")
        self.image3.setPixmap(QtGui.QPixmap("icons/03d.png"))
        self.image3.setScaledContents(True)
        self.image3.setAlignment(QtCore.Qt.AlignCenter)
        self.image3.setObjectName("image3")
        self.regen4 = QtWidgets.QLabel(self.frameWeather)
        self.regen4.setGeometry(QtCore.QRect(415, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen4.setFont(font)
        self.regen4.setAlignment(QtCore.Qt.AlignCenter)
        self.regen4.setObjectName("regen4")
        self.uhrzeit4 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit4.setGeometry(QtCore.QRect(415, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit4.setFont(font)
        self.uhrzeit4.setStyleSheet("")
        self.uhrzeit4.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit4.setObjectName("uhrzeit4")
        self.temperatur4 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur4.setGeometry(QtCore.QRect(415, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur4.setFont(font)
        self.temperatur4.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur4.setObjectName("temperatur4")
        self.wind4 = QtWidgets.QLabel(self.frameWeather)
        self.wind4.setGeometry(QtCore.QRect(415, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind4.setFont(font)
        self.wind4.setAlignment(QtCore.Qt.AlignCenter)
        self.wind4.setObjectName("wind4")
        self.image4 = QtWidgets.QLabel(self.frameWeather)
        self.image4.setGeometry(QtCore.QRect(415, 40, 80, 80))
        self.image4.setText("")
        self.image4.setPixmap(QtGui.QPixmap("icons/04d.png"))
        self.image4.setScaledContents(True)
        self.image4.setAlignment(QtCore.Qt.AlignCenter)
        self.image4.setObjectName("image4")
        self.regen5 = QtWidgets.QLabel(self.frameWeather)
        self.regen5.setGeometry(QtCore.QRect(545, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen5.setFont(font)
        self.regen5.setAlignment(QtCore.Qt.AlignCenter)
        self.regen5.setObjectName("regen5")
        self.uhrzeit5 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit5.setGeometry(QtCore.QRect(545, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit5.setFont(font)
        self.uhrzeit5.setStyleSheet("")
        self.uhrzeit5.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit5.setObjectName("uhrzeit5")
        self.temperatur5 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur5.setGeometry(QtCore.QRect(545, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur5.setFont(font)
        self.temperatur5.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur5.setObjectName("temperatur5")
        self.wind5 = QtWidgets.QLabel(self.frameWeather)
        self.wind5.setGeometry(QtCore.QRect(545, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind5.setFont(font)
        self.wind5.setAlignment(QtCore.Qt.AlignCenter)
        self.wind5.setObjectName("wind5")
        self.image5 = QtWidgets.QLabel(self.frameWeather)
        self.image5.setGeometry(QtCore.QRect(545, 40, 80, 80))
        self.image5.setAutoFillBackground(False)
        self.image5.setText("")
        self.image5.setPixmap(QtGui.QPixmap("icons/09d.png"))
        self.image5.setScaledContents(True)
        self.image5.setAlignment(QtCore.Qt.AlignCenter)
        self.image5.setObjectName("image5")
        self.regen6 = QtWidgets.QLabel(self.frameWeather)
        self.regen6.setGeometry(QtCore.QRect(675, 180, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.regen6.setFont(font)
        self.regen6.setAlignment(QtCore.Qt.AlignCenter)
        self.regen6.setObjectName("regen6")
        self.uhrzeit6 = QtWidgets.QLabel(self.frameWeather)
        self.uhrzeit6.setGeometry(QtCore.QRect(675, 10, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.uhrzeit6.setFont(font)
        self.uhrzeit6.setStyleSheet("")
        self.uhrzeit6.setAlignment(QtCore.Qt.AlignCenter)
        self.uhrzeit6.setObjectName("uhrzeit6")
        self.temperatur6 = QtWidgets.QLabel(self.frameWeather)
        self.temperatur6.setGeometry(QtCore.QRect(675, 120, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.temperatur6.setFont(font)
        self.temperatur6.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatur6.setObjectName("temperatur6")
        self.wind6 = QtWidgets.QLabel(self.frameWeather)
        self.wind6.setGeometry(QtCore.QRect(675, 150, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wind6.setFont(font)
        self.wind6.setAlignment(QtCore.Qt.AlignCenter)
        self.wind6.setObjectName("wind6")
        self.image6 = QtWidgets.QLabel(self.frameWeather)
        self.image6.setGeometry(QtCore.QRect(675, 40, 80, 80))
        self.image6.setText("")
        self.image6.setPixmap(QtGui.QPixmap("icons/13d.png"))
        self.image6.setScaledContents(True)
        self.image6.setAlignment(QtCore.Qt.AlignCenter)
        self.image6.setObjectName("image6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 201))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nextButton = QtWidgets.QPushButton(self.frame)
        self.nextButton.setGeometry(QtCore.QRect(700, 130, 50, 50))
        self.nextButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "border : none;")
        self.nextButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QtCore.QSize(50, 50))
        self.nextButton.setObjectName("nextButton")
        self.currentTrack = QtWidgets.QLabel(self.frame)
        self.currentTrack.setGeometry(QtCore.QRect(540, 80, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.currentTrack.setFont(font)
        self.currentTrack.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTrack.setObjectName("currentTrack")
        self.previousButton = QtWidgets.QPushButton(self.frame)
        self.previousButton.setGeometry(QtCore.QRect(530, 130, 50, 50))
        self.previousButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                          "border : none;")
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon1)
        self.previousButton.setIconSize(QtCore.QSize(50, 50))
        self.previousButton.setObjectName("previousButton")
        self.playpauseButton = QtWidgets.QPushButton(self.frame)
        self.playpauseButton.setGeometry(QtCore.QRect(610, 125, 60, 60))
        self.playpauseButton.setAutoFillBackground(False)
        self.playpauseButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "border : none;")
        self.playpauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playpauseButton.setIcon(icon2)
        self.playpauseButton.setIconSize(QtCore.QSize(60, 60))
        self.playpauseButton.setObjectName("playpauseButton")
        self.currentTime = QtWidgets.QLabel(self.frame)
        self.currentTime.setGeometry(QtCore.QRect(280, 10, 240, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(36)
        self.currentTime.setFont(font)
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.auswahlbox2 = QtWidgets.QComboBox(self.frame)
        self.auswahlbox2.setGeometry(QtCore.QRect(20, 55, 225, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.auswahlbox2.setFont(font)
        self.auswahlbox2.setStyleSheet("background-color: rgb(220, 217, 222);\n"
                                       "border-radius: 10px;\n"
                                       "color: black;")
        self.auswahlbox2.setObjectName("auswahlbox2")
        self.auswahlbox3 = QtWidgets.QComboBox(self.frame)
        self.auswahlbox3.setGeometry(QtCore.QRect(20, 100, 225, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.auswahlbox3.setFont(font)
        self.auswahlbox3.setStyleSheet("background-color: rgb(220, 217, 222);\n"
                                       "border-radius: 10px;\n"
                                       "color: black;")
        self.auswahlbox3.setObjectName("auswahlbox3")
        self.auswahlbox1 = QtWidgets.QComboBox(self.frame)
        self.auswahlbox1.setGeometry(QtCore.QRect(20, 10, 225, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.auswahlbox1.setFont(font)
        self.auswahlbox1.setAutoFillBackground(False)
        self.auswahlbox1.setStyleSheet("background-color: rgb(220, 217, 222);\n"
                                       "border-radius: 10px;\n"
                                       "color: black;")
        self.auswahlbox1.setObjectName("auswahlbox1")
        self.auswahlbox1.addItem("")
        self.auswahlbox1.addItem("")
        self.loadButton = QtWidgets.QPushButton(self.frame)
        self.loadButton.setGeometry(QtCore.QRect(70, 150, 120, 30))
        self.loadButton.setStyleSheet("border-radius : 10px;\n"
                                      "background-color: rgb(226, 224, 228);\n"
                                      "color: black;")
        self.loadButton.setObjectName("loadButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.uhrzeit1.setText(_translate("MainWindow", "uhrzeit1"))
        self.temperatur1.setText(_translate("MainWindow", "temperatur1"))
        self.wind1.setText(_translate("MainWindow", "wind1"))
        self.regen1.setText(_translate("MainWindow", "regen1"))
        self.regen2.setText(_translate("MainWindow", "regen2"))
        self.uhrzeit2.setText(_translate("MainWindow", "uhrzeit2"))
        self.temperatur2.setText(_translate("MainWindow", "temperatur2"))
        self.wind2.setText(_translate("MainWindow", "wind2"))
        self.regen3.setText(_translate("MainWindow", "regen3"))
        self.uhrzeit3.setText(_translate("MainWindow", "uhrzeit3"))
        self.temperatur3.setText(_translate("MainWindow", "temperatur3"))
        self.wind3.setText(_translate("MainWindow", "wind3"))
        self.regen4.setText(_translate("MainWindow", "regen4"))
        self.uhrzeit4.setText(_translate("MainWindow", "uhrzeit4"))
        self.temperatur4.setText(_translate("MainWindow", "temperatur4"))
        self.wind4.setText(_translate("MainWindow", "wind4"))
        self.regen5.setText(_translate("MainWindow", "regen5"))
        self.uhrzeit5.setText(_translate("MainWindow", "uhrzeit5"))
        self.temperatur5.setText(_translate("MainWindow", "temperatur5"))
        self.wind5.setText(_translate("MainWindow", "wind5"))
        self.regen6.setText(_translate("MainWindow", "regen6"))
        self.uhrzeit6.setText(_translate("MainWindow", "uhrzeit6"))
        self.temperatur6.setText(_translate("MainWindow", "temperatur6"))
        self.wind6.setText(_translate("MainWindow", "wind6"))
        self.currentTrack.setText(_translate("MainWindow", "currentTrack"))
        self.currentTime.setText(_translate("MainWindow", "currentTime"))
        self.auswahlbox1.setItemText(0, _translate("MainWindow", "Radio"))
        self.auswahlbox1.setItemText(1, _translate("MainWindow", "Audiobook"))
        self.loadButton.setText(_translate("MainWindow", "load"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.update_current_weather()
        self.update_other_weather()
        timerTime = QtCore.QTimer(self)
        timerTime.timeout.connect(self.update_current_time)
        timerTime.start(1000)
        timerWeather = QtCore.QTimer(self)
        timerWeather.timeout.connect(self.update_current_weather)
        timerWeather.timeout.connect(self.update_other_weather)
        timerWeather.start(60000)


    def update_current_weather(self):
        current_weather = weather.get_current_weather()
        time = current_weather.get('time')
        temperature = current_weather.get('temperature')
        wind_speed = current_weather.get('wind').get('speed')
        wind_direction = current_weather.get('wind').get('direction')
        icon = current_weather.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '1h' in current_weather.get('rain'):
            rain = current_weather.get('rain').get('1h')
            rain_time = '1h'
            norain = False
        elif '2h' in current_weather.get('rain'):
            rain = current_weather.get('rain').get('2h')
            rain_time = '2h'
            norain = False
        elif '3h' in current_weather.get('rain'):
            rain = current_weather.get('rain').get('3h')
            rain_time = '3h'
            norain = False
        else:
            rain = "---"
            norain = True
        self.uhrzeit1.setText("{}".format(time))
        self.temperatur1.setText("{}°C".format(temperature))
        self.wind1.setText("{}kn {}".format(wind_speed, wind_direction))
        if norain:
            self.regen1.setText("{}".format(rain))
        else:
            self.regen1.setText("{} in {}".format(rain, rain_time))
        self.image1.setPixmap(QtGui.QPixmap(icon))

        self.wind1.adjustSize()

    def update_other_weather(self):
        forecast = weather.x_hours_weather(15)

        # DREI STUNDEN
        forecast2 = forecast.get('1')
        time = forecast2.get('time')
        temperature = forecast2.get('temperature')
        wind_speed = forecast2.get('wind').get('speed')
        wind_direction = forecast2.get('wind').get('direction')
        icon = forecast2.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '3h' in forecast2.get('rain'):
            rain = forecast2.get('rain').get('3h')
            rain_time = '3h'
            self.regen2.setText("{} in {}".format(rain, rain_time))
        else:
            rain = "---"
            self.regen2.setText("{}".format(rain))

        self.uhrzeit2.setText("{}".format(time))
        self.temperatur2.setText("{}°C".format(temperature))
        self.wind2.setText("{}kn {}".format(wind_speed, wind_direction))
        self.image2.setPixmap(QtGui.QPixmap(icon))

        # SECHS STUNDEN
        forecast3 = forecast.get('2')
        time = forecast3.get('time')
        temperature = forecast3.get('temperature')
        wind_speed = forecast3.get('wind').get('speed')
        wind_direction = forecast3.get('wind').get('direction')
        icon = forecast3.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '3h' in forecast3.get('rain'):
            rain = forecast3.get('rain').get('3h')
            rain_time = '3h'
            self.regen3.setText("{} in {}".format(rain, rain_time))
        else:
            rain = "---"
            self.regen3.setText("{}".format(rain))

        self.uhrzeit3.setText("{}".format(time))
        self.temperatur3.setText("{}°C".format(temperature))
        self.wind3.setText("{}kn {}".format(wind_speed, wind_direction))
        self.image3.setPixmap(QtGui.QPixmap(icon))

        # NEUN STUNDEN
        forecast4 = forecast.get('3')
        time = forecast4.get('time')
        temperature = forecast4.get('temperature')
        wind_speed = forecast4.get('wind').get('speed')
        wind_direction = forecast4.get('wind').get('direction')
        icon = forecast4.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '3h' in forecast4.get('rain'):
            rain = forecast4.get('rain').get('3h')
            rain_time = '3h'
            self.regen4.setText("{} in {}".format(rain, rain_time))
        else:
            rain = "---"
            self.regen4.setText("{}".format(rain))

        self.uhrzeit4.setText("{}".format(time))
        self.temperatur4.setText("{}°C".format(temperature))
        self.wind4.setText("{}kn {}".format(wind_speed, wind_direction))
        self.image4.setPixmap(QtGui.QPixmap(icon))

        # ZWÖLF STUNDEN
        forecast5 = forecast.get('4')
        time = forecast5.get('time')
        temperature = forecast5.get('temperature')
        wind_speed = forecast5.get('wind').get('speed')
        wind_direction = forecast5.get('wind').get('direction')
        icon = forecast5.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '3h' in forecast5.get('rain'):
            rain = forecast5.get('rain').get('3h')
            rain_time = '3h'
            self.regen5.setText("{} in {}".format(rain, rain_time))
        else:
            rain = "---"
            self.regen5.setText("{}".format(rain))

        self.uhrzeit5.setText("{}".format(time))
        self.temperatur5.setText("{}°C".format(temperature))
        self.wind5.setText("{}kn {}".format(wind_speed, wind_direction))
        self.image5.setPixmap(QtGui.QPixmap(icon))

        # 15 STUNDEN
        forecast6 = forecast.get('5')
        time = forecast6.get('time')
        temperature = forecast6.get('temperature')
        wind_speed = forecast6.get('wind').get('speed')
        wind_direction = forecast6.get('wind').get('direction')
        icon = forecast6.get('icon')
        icon = "icons/" + icon + ".png"
        # rain
        if '3h' in forecast6.get('rain'):
            rain = forecast6.get('rain').get('3h')
            rain_time = '3h'
            self.regen6.setText("{} in {}".format(rain, rain_time))
        else:
            rain = "---"
            self.regen6.setText("{}".format(rain))

        self.uhrzeit6.setText("{}".format(time))
        self.temperatur6.setText("{}°C".format(temperature))
        self.wind6.setText("{}kn {}".format(wind_speed, wind_direction))
        self.image6.setPixmap(QtGui.QPixmap(icon))

        self.wind2.adjustSize()
        self.wind3.adjustSize()
        self.wind4.adjustSize()
        self.wind5.adjustSize()
        self.wind6.adjustSize()

    def update_current_time(self):
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M")
        self.currentTime.setText(current_time)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
