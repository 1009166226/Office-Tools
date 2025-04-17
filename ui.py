# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(90, 310, 641, 81))
        self.Filling = QPushButton(self.centralwidget)
        self.Filling.setObjectName(u"Filling")
        self.Filling.setGeometry(QRect(170, 400, 140, 60))
        self.Filling.setCheckable(False)
        self.Filling.setChecked(False)
        self.Filling.setAutoRepeat(True)
        self.Filling.setAutoExclusive(False)
        self.fileList = QListWidget(self.centralwidget)
        self.fileList.setObjectName(u"fileList")
        self.fileList.setGeometry(QRect(90, 120, 641, 192))
        self.fileList.setAcceptDrops(False)
        self.fileList.setDragEnabled(False)
        self.fileList.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.fileList.setSelectionRectVisible(True)
        self.Remove = QPushButton(self.centralwidget)
        self.Remove.setObjectName(u"Remove")
        self.Remove.setGeometry(QRect(310, 400, 140, 60))
        self.Clear = QPushButton(self.centralwidget)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setGeometry(QRect(450, 400, 140, 60))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b87\u5b50\u5999\u5999\u5de5\u5177", None))
        self.Filling.setText(QCoreApplication.translate("MainWindow", u"Fill Form", None))
        self.Remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

