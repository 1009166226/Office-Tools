# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'callHistory.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.HistoryTable = QTableWidget(self.centralwidget)
        if (self.HistoryTable.columnCount() < 3):
            self.HistoryTable.setColumnCount(3)
        font = QFont()
        font.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.HistoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.HistoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.HistoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.HistoryTable.setObjectName(u"HistoryTable")
        self.HistoryTable.setGeometry(QRect(10, 10, 771, 271))
        self.HistoryTable.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HistoryTable.setAutoFillBackground(False)
        self.HistoryTable.horizontalHeader().setCascadingSectionResizes(False)
        self.HistoryTable.horizontalHeader().setDefaultSectionSize(255)
        self.PolicyTable = QTableWidget(self.centralwidget)
        if (self.PolicyTable.columnCount() < 3):
            self.PolicyTable.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.PolicyTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.PolicyTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.PolicyTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.PolicyTable.setObjectName(u"PolicyTable")
        self.PolicyTable.setGeometry(QRect(10, 290, 771, 251))
        self.PolicyTable.horizontalHeader().setDefaultSectionSize(250)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b87\u5b50\u5f39\u7a97", None))
        ___qtablewidgetitem = self.HistoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"From", None));
        ___qtablewidgetitem1 = self.HistoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"To", None));
        ___qtablewidgetitem2 = self.HistoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date/Time", None));
        ___qtablewidgetitem3 = self.PolicyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Account#", None));
        ___qtablewidgetitem4 = self.PolicyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem5 = self.PolicyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Policy", None));
    # retranslateUi

