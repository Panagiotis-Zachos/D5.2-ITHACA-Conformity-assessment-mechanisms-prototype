"""
This Python script is a part of a PyQt5 application. PyQt5 is a set of Python bindings for Qt libraries which can be used to create cross-platform applications with a graphical user interface (GUI).

The script defines a class Ui_MainWindow which is used to set up the user interface for the main window of the application. The setupUi method is where the UI elements are created and configured.

Here's a brief overview of what the setupUi method does:

It sets up the main window, including its size, font, and background color.
It creates a central widget and a horizontal layout for the main window.
It creates a group box (verticalGroupBox_2) with a vertical layout (verticalLayout_3), which will contain other widgets.
It adds a label (label_5) to the group box, which displays an image (Ithaca_logo.jpg).
It adds three buttons (pushButton_3, pushButton_2, pushButton) to the group box. Each button is connected to a different function (load_tweets, clear_selection, close respectively) that will be executed when the button is clicked.
It adds the group box to the horizontal layout of the central widget.
It creates another vertical layout (verticalLayout_5) in the central widget, which contains a label (label_6) and two horizontal lines (line_11, line_8).
"""


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QListWidgetItem
from VisualBackendFunctions import returnTweets
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1851, 1173)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "background-color: rgba(0, 45, 136, 255);\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 45, 136, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox_2.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalGroupBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.verticalGroupBox_2.setSizeIncrement(QtCore.QSize(400, 400))
        self.verticalGroupBox_2.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(40, 50))
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_5.setSizeIncrement(QtCore.QSize(20, 20))
        self.label_5.setBaseSize(QtCore.QSize(20, 20))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("figures/Ithaca_logo.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(
            """QPushButton
                                                    {
                                                    background-color: rgb(255, 255, 255, 150); color: black;
                                                    border-color: rgb(172, 172, 172);
                                                    alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
                                                    border-color: rgb(255, 255, 255);
                                                    }
                                                    QPushButton:pressed
                                                    {
                                                    background-color : rgb(255, 255, 255, 255); color: rgb(255,255,255);
                                                    }"""
        )
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.load_tweets)
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            """QPushButton
                                                    {
                                                    background-color: rgb(255, 255, 255, 150); color: black;
                                                    border-color: rgb(172, 172, 172);
                                                    alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
                                                    border-color: rgb(255, 255, 255);
                                                    }
                                                    QPushButton:pressed
                                                    {
                                                    background-color : rgb(255, 255, 255, 255); color: rgb(255,255,255);
                                                    }"""
        )
        self.pushButton_2.setObjectName("pushButton_2")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_2.clicked.connect(self.clear_selection)
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            """QPushButton
                                                    {
                                                    background-color: rgb(255, 255, 255, 150); color: black;
                                                    border-color: rgb(172, 172, 172);
                                                    alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
                                                    border-color: rgb(255, 255, 255);
                                                    }
                                                    QPushButton:pressed
                                                    {
                                                    background-color : rgb(255, 255, 255, 255); color: rgb(255,255,255);
                                                    }"""
        )
        self.pushButton.setObjectName("pushButton")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 20))

        self.pushButton.clicked.connect(self.close)

        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.horizontalLayout_3.addWidget(self.verticalGroupBox_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_4.addWidget(self.line_11)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(
            "background-color: rgba(0, 45, 136, 70);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_4.addWidget(self.line_8)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem4)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout.addWidget(self.line_7)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        # Give some padding to avoid using horizontal scrollbar
        self.scrollArea.setMinimumSize(QtCore.QSize(420, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(420, 16777215))
        self.scrollArea.setStyleSheet(
            "border-color: rgb(0, 43, 131, 50);\n"
            "gridline-color: rgb(0, 45, 136, 50);\n"
            "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 50), stop:1 rgba(255, 255, 255, 50));\n"
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # Close Horizontal Scroll Bar
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 956))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(400, 1200))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalGroupBox_new = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        # self.verticalGroupBox_new.adjustSize()
        self.verticalGroupBox_new.setMinimumSize(QtCore.QSize(400, 1200))
        self.verticalGroupBox_new.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalGroupBox_new.setSizeIncrement(QtCore.QSize(400, 1200))
        self.verticalGroupBox_new.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.verticalGroupBox_new.setObjectName("verticalGroupBox_new")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_new)
        # like this is working yet the alignment is wrong
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox_new)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 45, 136, 50);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        # Bgazw th lista kai bazw koumpia mono se vertical layout
        #         self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        #         self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255, 150);\n"
        # "target->window()->setAttribute(Qt::WA_TranslucentBackground);\n"
        # "")
        #         self.listWidget.setObjectName("listWidget")
        #
        #         self.listWidget.addItems(self.readTweets())
        #         # self.listWidget.addItem()
        #         self.verticalLayout_2.addWidget(self.listWidget)

        # Add buttons as clickable tweets
        self.pushButtons = []
        for i in range(0, 20):
            self.pushButtons.append(self.add_button(str(i)))
            self.verticalLayout_2.addWidget(self.pushButtons[i])

        # self.richy = self.RichTextButton("richi", self.verticalGroupBox_new)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem7)
        # self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # Changed QTextBrowser to QPlainTextEdit so as to edit the text that appears
        self.textBrowser = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.textBrowser.setObjectName("textBrowser")
        font_textBrowser = QtGui.QFont()
        font_textBrowser.setPointSize(12)
        self.textBrowser.setFont(font_textBrowser)
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")

        self.verticalLayout.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem9)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "border-color: rgb(172, 172, 172);\n"
            "alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-color: rgb(255, 255, 255);"
        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.highlight_plain_text)
        self.verticalLayout.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignRight)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem10)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(900, 0))
        self.widget.setMaximumSize(QtCore.QSize(2000, 1500))
        self.widget.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget.setBaseSize(QtCore.QSize(40, 40))
        self.widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # Differential Privacy Stats
        self.dp_image = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.dp_image.setSizePolicy(sizePolicy)
        self.dp_image.setMinimumSize(QtCore.QSize(900, 0))
        self.dp_image.setMaximumSize(QtCore.QSize(2000, 1500))
        self.dp_image.setSizeIncrement(QtCore.QSize(40, 40))
        self.dp_image.setBaseSize(QtCore.QSize(40, 40))
        self.dp_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dp_image.setText("")
        self.dp_image.setPixmap(QtGui.QPixmap("figures/models_vpe.png"))
        self.dp_image.setScaledContents(True)
        self.dp_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.dp_image.setObjectName("dp_image")
        self.horizontalLayout_4.addWidget(self.dp_image)
        # self.dial = QtWidgets.QDial(self.widget)
        # self.dial.setObjectName("dial")
        # self.horizontalLayout_4.addWidget(self.dial)
        # self.dial_2 = QtWidgets.QDial(self.widget)
        # self.dial_2.setObjectName("dial_2")
        # self.horizontalLayout_4.addWidget(self.dial_2)
        # self.dial_3 = QtWidgets.QDial(self.widget)
        # self.dial_3.setObjectName("dial_3")
        # self.horizontalLayout_4.addWidget(self.dial_3)
        self.verticalLayout.addWidget(self.widget)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1851, 26))
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
        self.pushButton_3.setText(_translate("MainWindow", "Load Tweets"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        # self.pushButton_21.setText(_translate("MainWindow", "Button 555"))
        # print(self.pushButton_21.text())
        self.label_6.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Visual Component Demo</span></p></body></html>',
            )
        )
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">List of Toxic Tweets</span></p></body></html>',
            )
        )
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Edit a tweet from the list</span></p></body></html>',
            )
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Edit plain text</span></p></body></html>',
            )
        )
        self.pushButton_5.setText(_translate("MainWindow", "Check Toxicity"))
        self.label_4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Plot view</span></p></body></html>',
            )
        )

    def readTweets(self):
        """
        Reads tweets using the returnTweets function and returns the result.

        Returns:
            X (list): A list of tweets.
        """
        X = returnTweets()
        return X

    def clickme(self):
        """
        Updates the text browser with highlighted text based on the button pressed.

        This method retrieves the text from the button that was pressed, splits it into words,
        and then checks if each word is present in the 'unique_words' array. If a word is found,
        it is highlighted with a background color based on its index in the 'unique_words' array.
        The highlighted text is then displayed in the text browser.

        Parameters:
            None

        Returns:
            None
        """
        # Find which button was pressed
        pressed_button = self.centralwidget.sender()
        self.textBrowser.setPlainText(pressed_button.text())
        words = pressed_button.text().split()

        # toxicity_freq = np.load("./data/toxicity_freq.npy")
        unique_words = np.load("./data/unique_words.npy")

        html_text = []
        for word in words:
            word_idx = np.argwhere(unique_words == word)
            if word in unique_words:
                #     print()
                html_text.append(
                    "<span style='background-color: rgb({}, 165, 73);'>{}</span>".format(
                        255 - 255 * word_idx[0][0] / len(unique_words), word
                    )
                )
            else:
                html_text.append(word)

        highlighted_text = " ".join(html_text)
        self.textBrowser.clear()
        self.textBrowser.appendHtml(highlighted_text)

    def add_button(self, text):
        tweets = self.readTweets()
        # The buttons should wrap text and their sizes should be adjusted accordingly
        pushButton_32 = self.RichTextButton(
            tweets[int(text)], self.verticalGroupBox_new
        )
        # pushButton_32 = QtWidgets.QPushButton("button_" + text, self.verticalGroupBox_new)
        print(pushButton_32.text())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(500)
        sizePolicy.setHeightForWidth(pushButton_32.sizePolicy().hasHeightForWidth())
        pushButton_32.setSizePolicy(sizePolicy)
        pushButton_32.setMinimumSize(QtCore.QSize(50, 50))
        pushButton_32.setMaximumSize(QtCore.QSize(500, 16777214))
        font = QtGui.QFont("Arial", 11)
        # font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        pushButton_32.setFont(font)
        pushButton_32.setAutoFillBackground(False)
        # text color was black -> changed to transparent -> low a (rgb(255, 255, 255, 10))
        pushButton_32.setStyleSheet(
            """QPushButton
                                                    {
                                                    background-color: rgb(255, 255, 255, 150); color: rgb(255, 255, 255, 10);
                                                    border-color: rgb(172, 172, 172);
                                                    alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
                                                    border-color: rgb(255, 255, 255);
                                                    }
                                                    QPushButton:pressed
                                                    {
                                                    background-color : rgb(255, 255, 255, 255); color: rgb(255,255,255);
                                                    }"""
        )
        pushButton_32.setObjectName("pushButton_" + text)
        # the button is pressed
        pushButton_32.setText(tweets[int(text)])
        pushButton_32.clicked.connect(self.clickme)
        # self.pushButton_32.setText("Over-write")
        text = pushButton_32.text()
        pushButton_32.adjustSize()

        print(text)
        return pushButton_32

    def highlight_plain_text(self):
        """
        Highlights specific words in the plain text using HTML formatting.

        This method takes the plain text from the `plainTextEdit` widget, splits it into words,
        and checks if each word is present in the `unique_words` array. If a word is found in the array,
        it is highlighted with a background color based on its index in the `unique_words` array.
        The highlighted text is then displayed in the `plainTextEdit` widget.

        Note: The `unique_words` array is loaded from the "./data/unique_words.npy" file.

        Returns:
            None
        """
        plain_text = self.plainTextEdit.toPlainText()
        if plain_text:
            words = plain_text.split()
            # toxicity_freq = np.load("./data/toxicity_freq.npy")
            unique_words = np.load("./data/unique_words.npy")

            html_text = []
            for word in words:
                word_idx = np.argwhere(unique_words == word)
                if word in unique_words:
                    #     print()
                    html_text.append(
                        "<span style='background-color: rgb({}, 165, 73);'>{}</span>".format(
                            255 - 255 * word_idx[0][0] / len(unique_words), word
                        )
                    )
                else:
                    html_text.append(word)

            highlighted_text = " ".join(html_text)
            self.plainTextEdit.clear()
            self.plainTextEdit.appendHtml(highlighted_text)

    class RichTextButton(QtWidgets.QPushButton):
        def __init__(self, text, parent=None):  # change signature to allow text
            QtWidgets.QPushButton.__init__(self, parent)
            self.UnitText = QtWidgets.QLabel(text, self)  # pass the text for the label
            self.UnitText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.UnitText.setWordWrap(True)  # set word wrap for label
            self.UnitText.setAlignment(QtCore.Qt.AlignCenter)
            self.UnitText.setMouseTracking(False)
            font = QtGui.QFont("Arial", 11)
            # font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.UnitText.setFont(font)
            self.setLayout(QtWidgets.QVBoxLayout())
            self.layout().setContentsMargins(0, 0, 0, 0)
            self.layout().addWidget(self.UnitText)

    def clear_selection(self):
        """
        Clears the content of the text browser and plain text edit.
        """
        self.textBrowser.clear()
        self.plainTextEdit.clear()

    def load_tweets(self):
            """
            Load tweets from a specified path.

            This method prompts the user to enter the path to their files and then uses the path to load the files.
            """
            path, ok = QtWidgets.QInputDialog().getText(
                None, "Load Tweets", "Enter the path to your files:"
            )
            # use path to load files
            print(path)

    def close(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Εxit")
        msg.setText("Would you like to exit the application?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # result = msg.question(self.centralwidget, 'Εxit', 'Would you like to exit the application?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # msg.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
        #                   "color: black")
        result = msg.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            app.quit()
        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
