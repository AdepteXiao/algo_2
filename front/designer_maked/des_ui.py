# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\front\designer_maked\pain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistsLayout = QtWidgets.QHBoxLayout()
        self.playlistsLayout.setObjectName("playlistsLayout")
        self.allPlaylistsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.allPlaylistsGroupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.allPlaylistsGroupBox.setObjectName("allPlaylistsGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.allPlaylistsGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.allPlaylistsScrollArea = QtWidgets.QScrollArea(self.allPlaylistsGroupBox)
        self.allPlaylistsScrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.allPlaylistsScrollArea.setWidgetResizable(True)
        self.allPlaylistsScrollArea.setObjectName("allPlaylistsScrollArea")
        self.allPlaylistScrollAreaWidget = QtWidgets.QWidget()
        self.allPlaylistScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 350, 344))
        self.allPlaylistScrollAreaWidget.setObjectName("allPlaylistScrollAreaWidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.allPlaylistScrollAreaWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.playlistHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.playlistHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.playlistHorizontalLayout.setObjectName("playlistHorizontalLayout")
        self.playlistLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.playlistLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.playlistLabel.setObjectName("playlistLabel")
        self.playlistHorizontalLayout.addWidget(self.playlistLabel)
        self.allPlaylistsScrollArea.setWidget(self.allPlaylistScrollAreaWidget)
        self.verticalLayout_2.addWidget(self.allPlaylistsScrollArea)
        self.playlistsLayout.addWidget(self.allPlaylistsGroupBox)
        self.curPlaylistGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.curPlaylistGroupBox.setObjectName("curPlaylistGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.curPlaylistGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.playlistMeta = QtWidgets.QLabel(self.curPlaylistGroupBox)
        self.playlistMeta.setObjectName("playlistMeta")
        self.verticalLayout_5.addWidget(self.playlistMeta)
        self.curPlaylistScrollArea = QtWidgets.QScrollArea(self.curPlaylistGroupBox)
        self.curPlaylistScrollArea.setMinimumSize(QtCore.QSize(300, 0))
        self.curPlaylistScrollArea.setWidgetResizable(True)
        self.curPlaylistScrollArea.setObjectName("curPlaylistScrollArea")
        self.curPlaylistScrollAreaWidget = QtWidgets.QWidget()
        self.curPlaylistScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 349, 322))
        self.curPlaylistScrollAreaWidget.setObjectName("curPlaylistScrollAreaWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.curPlaylistScrollAreaWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.trackHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.trackHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.trackHorizontalLayout.setObjectName("trackHorizontalLayout")
        self.trackLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.trackLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.trackLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.trackLabel.setObjectName("trackLabel")
        self.trackHorizontalLayout.addWidget(self.trackLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.trackHorizontalLayout.addItem(spacerItem)
        self.durationLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.durationLabel.setObjectName("durationLabel")
        self.trackHorizontalLayout.addWidget(self.durationLabel)
        self.curPlaylistScrollArea.setWidget(self.curPlaylistScrollAreaWidget)
        self.verticalLayout_5.addWidget(self.curPlaylistScrollArea)
        self.playlistsLayout.addWidget(self.curPlaylistGroupBox)
        self.verticalLayout.addLayout(self.playlistsLayout)
        self.playLineGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.playLineGroupBox.setObjectName("playLineGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.playLineGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.metaLayout = QtWidgets.QHBoxLayout()
        self.metaLayout.setObjectName("metaLayout")
        self.trackPicLabel = QtWidgets.QLabel(self.playLineGroupBox)
        self.trackPicLabel.setObjectName("trackPicLabel")
        self.metaLayout.addWidget(self.trackPicLabel)
        self.trackNameLabel = QtWidgets.QLabel(self.playLineGroupBox)
        self.trackNameLabel.setObjectName("trackNameLabel")
        self.metaLayout.addWidget(self.trackNameLabel)
        self.verticalLayout_3.addLayout(self.metaLayout)
        self.trackProgressLayout = QtWidgets.QHBoxLayout()
        self.trackProgressLayout.setObjectName("trackProgressLayout")
        self.curDurationLabel = QtWidgets.QLabel(self.playLineGroupBox)
        self.curDurationLabel.setObjectName("curDurationLabel")
        self.trackProgressLayout.addWidget(self.curDurationLabel)
        self.trackProgressHorizontalSlider = QtWidgets.QSlider(self.playLineGroupBox)
        self.trackProgressHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.trackProgressHorizontalSlider.setObjectName("trackProgressHorizontalSlider")
        self.trackProgressLayout.addWidget(self.trackProgressHorizontalSlider)
        self.trackDurationLabel = QtWidgets.QLabel(self.playLineGroupBox)
        self.trackDurationLabel.setObjectName("trackDurationLabel")
        self.trackProgressLayout.addWidget(self.trackDurationLabel)
        self.verticalLayout_3.addLayout(self.trackProgressLayout)
        self.controlsLayout = QtWidgets.QHBoxLayout()
        self.controlsLayout.setObjectName("controlsLayout")
        self.prevPushButton = QtWidgets.QPushButton(self.playLineGroupBox)
        self.prevPushButton.setObjectName("prevPushButton")
        self.controlsLayout.addWidget(self.prevPushButton)
        self.playPushButton = QtWidgets.QPushButton(self.playLineGroupBox)
        self.playPushButton.setFlat(False)
        self.playPushButton.setObjectName("playPushButton")
        self.controlsLayout.addWidget(self.playPushButton)
        self.pausePushButton = QtWidgets.QPushButton(self.playLineGroupBox)
        self.pausePushButton.setObjectName("pausePushButton")
        self.controlsLayout.addWidget(self.pausePushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.playLineGroupBox)
        self.nextPushButton.setObjectName("nextPushButton")
        self.controlsLayout.addWidget(self.nextPushButton)
        self.verticalLayout_3.addLayout(self.controlsLayout)
        self.verticalLayout.addWidget(self.playLineGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 26))
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
        self.allPlaylistsGroupBox.setTitle(_translate("MainWindow", "Плейлисты"))
        self.playlistLabel.setText(_translate("MainWindow", "мета плейлиста"))
        self.curPlaylistGroupBox.setTitle(_translate("MainWindow", "Название активного плейлиста"))
        self.playlistMeta.setText(_translate("MainWindow", "Мета плелиста"))
        self.trackLabel.setText(_translate("MainWindow", "мета трека"))
        self.durationLabel.setText(_translate("MainWindow", "Duration"))
        self.playLineGroupBox.setTitle(_translate("MainWindow", "Строка воспросизведения"))
        self.trackPicLabel.setText(_translate("MainWindow", "ПИкча трека"))
        self.trackNameLabel.setText(_translate("MainWindow", "Мета трека"))
        self.curDurationLabel.setText(_translate("MainWindow", "00:00"))
        self.trackDurationLabel.setText(_translate("MainWindow", "02:05"))
        self.prevPushButton.setText(_translate("MainWindow", "prev"))
        self.playPushButton.setText(_translate("MainWindow", "Play"))
        self.pausePushButton.setText(_translate("MainWindow", "Pause"))
        self.nextPushButton.setText(_translate("MainWindow", "Next"))