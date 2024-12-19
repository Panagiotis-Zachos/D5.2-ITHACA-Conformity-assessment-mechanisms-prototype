import os
import sys

import numpy as np
import tensorflow as tf
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QListWidgetItem

from models import create_dp_model
from VisualBackendFunctions import returnTweets


class UI_Moderator_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Set up the user interface for the main window.
        This method initializes and configures the main window and its widgets, including layouts, labels, buttons,
        scroll areas, and other UI elements. It also sets up the styles, sizes, and connections for various widgets.
        Parameters:
        MainWindow (QMainWindow): The main window object to set up the UI for.
        Widgets and Layouts:
        - MainWindow: The main window object.
        - centralwidget: The central widget of the main window.
        - horizontalLayout_3: The main horizontal layout.
        - verticalGroupBox_2: A vertical group box containing buttons and a label.
        - label_5: A label displaying an image.
        - pushButton_3: A button to load tweets.
        - pushButton_2: A button to clear selection.
        - pushButton: A button to close the application.
        - verticalLayout_5: A vertical layout for additional widgets.
        - verticalLayout_4: A vertical layout containing labels and lines.
        - line_11, line_8, line_7: Horizontal lines for separation.
        - scrollArea: A scroll area containing a group box with buttons.
        - verticalGroupBox_new: A vertical group box inside the scroll area.
        - verticalLayout_2: A vertical layout inside the new group box.
        - label_2: A label inside the new group box.
        - pushButtons: A list of buttons added dynamically.
        - horizontalLayout_Fairness: A horizontal layout for text and images.
        - textBrowser: A plain text edit widget.
        - fairness_image, fairness_image_2: Labels displaying images.
        - plainTextEdit: A plain text edit widget.
        - pushButton_5: A button to highlight plain text.
        - widget, widget2: Widgets for additional layouts and labels.
        - verticalLayout_ppml, verticalLayout_cybersecurity: Vertical layouts for PPML and cybersecurity sections.
        - label_ppml, label_cybersecurity: Labels for PPML and cybersecurity sections.
        - pushButton_ppml_stats, pushButton_ppml_refresh: Buttons for PPML stats and refresh.
        - pushButton_info_cyber: A button for cybersecurity info.
        - tableWidget: A table widget displaying tool status.
        - pushButton_info_tool_status: A button for tool status info.
        Styles and Configurations:
        - Sets fonts, sizes, and styles for various widgets.
        - Configures minimum and maximum sizes for widgets.
        - Sets up connections for button click events.
        - Configures scroll area properties.
        Returns:
        None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1851, 1173)
        font = QtGui.QFont()
        font.setPointSize(14)
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
        font.setPointSize(14)
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
        font.setPointSize(14)
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
        font.setPointSize(14)
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
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 45, 136, 50);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

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
        font.setPointSize(18)
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
        # ******
        self.horizontalLayout_Fairness = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_Fairness.setObjectName("horizontalLayout_Fairness")
        # ******
        self.textBrowser = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.textBrowser.setObjectName("textBrowser")
        font_textBrowser = QtGui.QFont()
        font_textBrowser.setPointSize(14)
        self.textBrowser.setFont(font_textBrowser)
        # *******
        # self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_Fairness)
        self.horizontalLayout_Fairness.addWidget(self.textBrowser)
        self.fairness_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.fairness_image.setSizePolicy(sizePolicy)
        self.fairness_image.setMinimumSize(QtCore.QSize(90, 0))
        self.fairness_image.setMaximumSize(QtCore.QSize(90, 100))
        self.fairness_image.setSizeIncrement(QtCore.QSize(90, 90))
        self.fairness_image.setBaseSize(QtCore.QSize(60, 60))
        self.fairness_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fairness_image.setText("")
        self.fairness_image.setStyleSheet(
            "background-color: rgba(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.fairness_image.setPixmap(
            QtGui.QPixmap("figures/Eo_circle_green_checkmark.svg.png")
        )
        self.fairness_image.setScaledContents(True)
        self.fairness_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.fairness_image.setObjectName("fairness_image")
        self.horizontalLayout_Fairness.addWidget(self.fairness_image)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        # ******
        # self.verticalLayout.addWidget(self.plainTextEdit)
        # self.horizontalLayout_Fairness2.addWidget(self.plainTextEdit)
        self.fairness_image_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.fairness_image_2.setSizePolicy(sizePolicy)
        self.fairness_image_2.setMinimumSize(QtCore.QSize(90, 0))
        self.fairness_image_2.setMaximumSize(QtCore.QSize(90, 100))
        self.fairness_image_2.setSizeIncrement(QtCore.QSize(90, 90))
        self.fairness_image_2.setBaseSize(QtCore.QSize(60, 60))
        self.fairness_image_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fairness_image_2.setText("")
        self.fairness_image_2.setStyleSheet(
            "background-color: rgba(255, 255, 255, 150);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.fairness_image_2.setPixmap(
            QtGui.QPixmap("figures/x_mark-removebg-preview.png")
        )
        self.fairness_image_2.setScaledContents(True)
        self.fairness_image_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.fairness_image_2.setObjectName("fairness_image_2")
        # self.horizontalLayout_Fairness2.addWidget(self.fairness_image_2)
        self.horizontalLayout_Fairness.addWidget(self.plainTextEdit)
        self.horizontalLayout_Fairness.addWidget(self.fairness_image_2)

        # ********
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
        font.setPointSize(14)
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
        # ********

        #         self.label_4 = QtWidgets.QLabel(self.centralwidget)
        #         font = QtGui.QFont()
        #         font.setPointSize(16)
        #         self.label_4.setFont(font)
        #         self.label_4.setStyleSheet("background-color: rgba(0, 45, 136, 50);\n"
        # "border: 5px; \n"
        # "border-radius: 10px;")
        # self.label_4.setObjectName("label_4")
        # self.verticalLayout.addWidget(self.label_4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(650, 0))
        self.widget.setMaximumSize(QtCore.QSize(400, 400))
        self.widget.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget.setBaseSize(QtCore.QSize(40, 40))
        self.widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget.setObjectName("widget")
        # ********
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy)
        self.widget2.setMinimumSize(QtCore.QSize(650, 0))
        self.widget2.setMaximumSize(QtCore.QSize(400, 400))
        self.widget2.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget2.setBaseSize(QtCore.QSize(40, 40))
        self.widget2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget2.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget2.setObjectName("widget2")
        # **********
        # self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        # self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # Differential Privacy Stats
        # self.dp_image = QtWidgets.QLabel(self.widget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(10)
        # sizePolicy.setVerticalStretch(10)
        # sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        # ********************* PPML ********************* #
        self.verticalLayout_ppml = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_ppml.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint
        )
        self.verticalLayout_ppml.setObjectName("verticalLayout_ppml")
        spacerItem_ppml = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        # self.horizontalLayout_4.addItem(self.verticalLayout_cybersecurity)
        self.label_ppml = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_ppml.setFont(font)
        self.label_ppml.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_ppml.setObjectName("label_ppml")
        self.verticalLayout_ppml.addWidget(self.label_ppml)
        self.line_ppml = QtWidgets.QFrame(self.widget2)
        self.line_ppml.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ppml.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ppml.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.line_ppml.setObjectName("line_ppml")
        self.verticalLayout_ppml.addWidget(self.line_ppml)
        self.ppml_stars = QtWidgets.QLabel(self.widget2)
        self.ppml_stars.setStyleSheet(
            "background-color: rgb(255, 255, 255, 100);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.ppml_stars.setObjectName("ppml_stars")
        font_textBrowser = QtGui.QFont()
        font_textBrowser.setPointSize(16)
        font_textBrowser.setWeight(QFont.Bold)
        self.ppml_stars.setFont(font_textBrowser)
        self.ppml_stars.setText("\n" + "Metrics after 50 epochs\n")
        self.ppml_stars.setAlignment(QtCore.Qt.AlignCenter)
        self.ppml_stars2 = QtWidgets.QTextBrowser(self.widget2)
        self.ppml_stars2.setStyleSheet(
            "background-color: rgb(255, 255, 255, 200);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.ppml_stars2.setObjectName("ppml_stars2")
        font_textBrowser = QtGui.QFont()
        font_textBrowser.setPointSize(14)
        self.ppml_stars2.setFont(font_textBrowser)
        self.ppml_stars2.setText(
            "\n"
            + "\n"
            + " Area Under Curve (AUC) : 0.498 \n"
            + " Attacker Advantage       : 0.059 \n"
            + " Positive Predictive Value : 0.800 \n"
        )
        self.ppml_stars2.selectAll()
        self.ppml_stars2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_ppml.addWidget(self.ppml_stars)
        self.verticalLayout_ppml.addWidget(self.ppml_stars2)
        self.pushButton_ppml_stats = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.pushButton_ppml_stats.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_ppml_stats.setSizePolicy(sizePolicy)
        self.pushButton_ppml_stats.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(QFont.Bold)
        self.pushButton_ppml_stats.setFont(font)
        self.pushButton_ppml_stats.setAutoFillBackground(False)
        self.pushButton_ppml_stats.setStyleSheet(
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
        # self.pushButton_info_cyber.setGeometry(200, 150, 100, 30)
        self.pushButton_ppml_stats.setObjectName("pushButton_ppml_stats")
        # self.pushButton_info_cyber.setIcon(QIcon('info-information-icon.png'))
        self.pushButton_ppml_stats.clicked.connect(self.show_ppml_stats)
        self.pushButton_ppml_stats.show()
        self.verticalLayout_ppml.addWidget(
            self.pushButton_ppml_stats, 0, QtCore.Qt.AlignRight
        )

        self.pushButton_ppml_refresh = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.pushButton_ppml_refresh.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_ppml_refresh.setSizePolicy(sizePolicy)
        self.pushButton_ppml_refresh.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(QFont.Bold)
        self.pushButton_ppml_refresh.setFont(font)
        self.pushButton_ppml_refresh.setAutoFillBackground(False)
        self.pushButton_ppml_refresh.setStyleSheet(
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
        # self.pushButton_info_cyber.setGeometry(200, 150, 100, 30)
        self.pushButton_ppml_refresh.setObjectName("pushButton_ppml_stats")
        # self.pushButton_info_cyber.setIcon(QIcon('info-information-icon.png'))
        self.verticalLayout_ppml.addWidget(
            self.pushButton_ppml_refresh, 0, QtCore.Qt.AlignRight
        )

        # ********************* CYBERSECURITY ********************* #
        self.verticalLayout_cybersecurity = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_cybersecurity.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint
        )
        self.verticalLayout_cybersecurity.setObjectName("verticalLayout_cybersecurity")
        spacerItem_cyber = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        # self.horizontalLayout_4.addItem(self.verticalLayout_cybersecurity)
        self.label_cybersecurity = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_cybersecurity.setFont(font)
        self.label_cybersecurity.setStyleSheet(
            "background-color: rgba(0, 45, 136, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity.setObjectName("label_cybersecurity")
        self.verticalLayout_cybersecurity.addWidget(self.label_cybersecurity)
        self.line_cyber = QtWidgets.QFrame(self.widget)
        self.line_cyber.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_cyber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_cyber.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.line_cyber.setObjectName("line_cyber")
        self.verticalLayout_cybersecurity.addWidget(self.line_cyber)
        # self.verticalLayout_cybersecurity.addItem(spacerItem_cyber)
        # **************************** LOW ****************************#
        self.widget3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())
        self.widget3.setSizePolicy(sizePolicy)
        self.widget3.setMinimumSize(QtCore.QSize(640, 0))
        self.widget3.setMaximumSize(QtCore.QSize(400, 400))
        self.widget3.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget3.setBaseSize(QtCore.QSize(40, 40))
        self.widget3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget3.setStyleSheet(
            "background-color: rgba(0, 45, 136, 10);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget3.setObjectName("widget3")
        self.label_cybersecurity_stats = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats.setFont(font)
        self.label_cybersecurity_stats.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats.setObjectName("label_cybersecurity_stats")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.verticalLayout_cybersecurity.addWidget(self.widget3)
        self.horizontalLayout_4.addWidget(self.label_cybersecurity_stats)

        self.label_cybersecurity_stats2 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats2.setFont(font)
        self.label_cybersecurity_stats2.setStyleSheet(
            "background-color: rgba(147, 250, 165, 100);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats2.setObjectName("label_cybersecurity_stats2")
        self.horizontalLayout_4.addWidget(self.label_cybersecurity_stats2)

        # ****************************************************************#
        # **************************** MEDIUM ****************************#
        self.widget4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget4.sizePolicy().hasHeightForWidth())
        self.widget4.setSizePolicy(sizePolicy)
        self.widget4.setMinimumSize(QtCore.QSize(640, 0))
        self.widget4.setMaximumSize(QtCore.QSize(400, 400))
        self.widget4.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget4.setBaseSize(QtCore.QSize(40, 40))
        self.widget4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget4.setStyleSheet(
            "background-color: rgba(0, 45, 136, 10);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget4.setObjectName("widget4")
        self.label_cybersecurity_stats3 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats3.setFont(font)
        self.label_cybersecurity_stats3.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats3.setObjectName("label_cybersecurity_stats3")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.verticalLayout_cybersecurity.addWidget(self.widget4)
        self.horizontalLayout_42.addWidget(self.label_cybersecurity_stats3)

        self.label_cybersecurity_stats4 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats4.setFont(font)
        self.label_cybersecurity_stats4.setStyleSheet(
            "background-color: rgba(255, 252, 127, 100);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats4.setObjectName("label_cybersecurity_stats4")
        self.horizontalLayout_42.addWidget(self.label_cybersecurity_stats4)
        # **************************************************************#
        # **************************** HIGH ****************************#
        self.widget5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget5.sizePolicy().hasHeightForWidth())
        self.widget5.setSizePolicy(sizePolicy)
        self.widget5.setMinimumSize(QtCore.QSize(640, 0))
        self.widget5.setMaximumSize(QtCore.QSize(400, 400))
        self.widget5.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget5.setBaseSize(QtCore.QSize(40, 40))
        self.widget5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget5.setStyleSheet(
            "background-color: rgba(0, 45, 136, 10);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget5.setObjectName("widget5")
        self.label_cybersecurity_stats5 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats5.setFont(font)
        self.label_cybersecurity_stats5.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats5.setObjectName("label_cybersecurity_stats5")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.verticalLayout_cybersecurity.addWidget(self.widget5)
        self.horizontalLayout_43.addWidget(self.label_cybersecurity_stats5)

        self.label_cybersecurity_stats6 = QtWidgets.QLabel(self.widget5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats6.setFont(font)
        self.label_cybersecurity_stats6.setStyleSheet(
            "background-color: rgba(255, 148, 112, 100);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats6.setObjectName("label_cybersecurity_stats6")
        self.horizontalLayout_43.addWidget(self.label_cybersecurity_stats6)
        # ******************************************************************#
        # **************************** CRITICAL ****************************#
        self.widget6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget6.sizePolicy().hasHeightForWidth())
        self.widget6.setSizePolicy(sizePolicy)
        self.widget6.setMinimumSize(QtCore.QSize(640, 0))
        self.widget6.setMaximumSize(QtCore.QSize(400, 400))
        self.widget6.setSizeIncrement(QtCore.QSize(40, 40))
        self.widget6.setBaseSize(QtCore.QSize(40, 40))
        self.widget6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget6.setStyleSheet(
            "background-color: rgba(0, 45, 136, 10);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.widget6.setObjectName("widget6")
        self.label_cybersecurity_stats7 = QtWidgets.QLabel(self.widget6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cybersecurity_stats7.setFont(font)
        self.label_cybersecurity_stats7.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats7.setObjectName("label_cybersecurity_stats7")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.verticalLayout_cybersecurity.addWidget(self.widget6)
        self.horizontalLayout_44.addWidget(self.label_cybersecurity_stats7)

        self.label_cybersecurity_stats8 = QtWidgets.QLabel(self.widget6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_cybersecurity_stats8.setFont(font)
        self.label_cybersecurity_stats8.setStyleSheet(
            "background-color: rgba(254, 121, 104, 100);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        self.label_cybersecurity_stats8.setObjectName("label_cybersecurity_stats8")
        self.horizontalLayout_44.addWidget(self.label_cybersecurity_stats8)
        # ***************** INFO BUTTON ***************** #
        self.pushButton_info_cyber = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.pushButton_info_cyber.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_info_cyber.setSizePolicy(sizePolicy)
        self.pushButton_info_cyber.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(QFont.Bold)
        self.pushButton_info_cyber.setFont(font)
        self.pushButton_info_cyber.setAutoFillBackground(False)
        self.pushButton_info_cyber.setStyleSheet(
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
        # self.pushButton_info_cyber.setGeometry(200, 150, 100, 30)
        self.pushButton_info_cyber.setObjectName("pushButton_info_cyber")
        # self.pushButton_info_cyber.setIcon(QIcon('info-information-icon.png'))
        self.pushButton_info_cyber.clicked.connect(self.info_cybersecurity)
        self.verticalLayout_cybersecurity.addWidget(
            self.pushButton_info_cyber, 0, QtCore.Qt.AlignRight
        )

        # # *********************
        # IMAGE PPML
        # self.dp_image = QtWidgets.QLabel(self.widget)
        # self.dp_image.setSizePolicy(sizePolicy)
        # self.dp_image.setMinimumSize(QtCore.QSize(650, 0))
        # self.dp_image.setMaximumSize(QtCore.QSize(350, 350))
        # self.dp_image.setSizeIncrement(QtCore.QSize(40, 40))
        # self.dp_image.setBaseSize(QtCore.QSize(40, 40))
        # self.dp_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.dp_image.setText("")
        # self.dp_image.setPixmap(QtGui.QPixmap("figures/models_vpe.png"))
        # self.dp_image.setScaledContents(True)
        # self.dp_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        # self.dp_image.setObjectName("dp_image")
        # # HOW IT WAS
        # # self.horizontalLayout_4.addWidget(self.dp_image)
        # self.verticalLayout_cybersecurity.addWidget(self.dp_image)
        # self.dial = QtWidgets.QDial(self.widget)
        # self.dial.setObjectName("dial")
        # self.horizontalLayout_4.addWidget(self.dial)
        # self.dial_2 = QtWidgets.QDial(self.widget)
        # self.dial_2.setObjectName("dial_2")
        # self.horizontalLayout_4.addWidget(self.dial_2)
        # self.dial_3 = QtWidgets.QDial(self.widget)
        # self.dial_3.setObjectName("dial_3")
        # self.horizontalLayout_4.addWidget(self.dial_3)
        # ******
        self.horizontalLayout_Cybersecurity = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_Cybersecurity.setObjectName(
            "horizontalLayout_Cybersecurity"
        )
        self.verticalLayout.addLayout(self.horizontalLayout_Cybersecurity)
        self.horizontalLayout_Cybersecurity.addWidget(self.widget)
        self.horizontalLayout_Cybersecurity.addWidget(self.widget2)
        # *****
        # self.verticalLayout.addWidget(self.widget)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem11)

        spacerItem8 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
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
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.verticalLayout.addItem(spacerItem10)
        # ******************* TOOL STATUS ******************* #
        self.verticalLayout_tool_status = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_tool_status.setObjectName("verticalLayout_tool_status")
        self.tableWidget = QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50);\n"
            "border: 5px; \n"
            "border-radius: 10px;"
        )
        # Row count
        self.tableWidget.setRowCount(3)

        # Column count
        self.tableWidget.setColumnCount(5)
        delegate = AlignDelegate(self.tableWidget)
        # If you want to do it for all columns:
        self.tableWidget.setItemDelegate(delegate)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView { font-size: 16pt; }"
        )
        green_light = ImageWidget(
            "figures/green_light-removebg-preview", self.tableWidget
        )
        green_light2 = ImageWidget(
            "figures/green_light-removebg-preview", self.tableWidget
        )
        green_light3 = ImageWidget(
            "figures/green_light-removebg-preview", self.tableWidget
        )
        orange_light = ImageWidget(
            "figures/orange_light-removebg-preview", self.tableWidget
        )
        orange_light2 = ImageWidget(
            "figures/orange_light-removebg-preview", self.tableWidget
        )
        red_light = ImageWidget("figures/red_light-removebg-preview", self.tableWidget)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("AI Fairness"))
        self.tableWidget.setItem(
            1, 0, QTableWidgetItem("Privacy Preserving Machine Learning")
        )
        self.tableWidget.setItem(2, 0, QTableWidgetItem("AI Cybersecurity"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("7-12-2024"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("5-12-2024"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("12-12-2024"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Yes"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Yes"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Yes"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("GREEN"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("GREEN"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem("ORANGE"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("RED"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("GREEN"))
        self.tableWidget.setItem(2, 4, QTableWidgetItem("ORANGE"))

        self.tableWidget.setCellWidget(0, 3, green_light)
        self.tableWidget.setCellWidget(1, 3, green_light2)
        self.tableWidget.setCellWidget(2, 3, orange_light)
        self.tableWidget.setCellWidget(0, 4, red_light)
        self.tableWidget.setCellWidget(1, 4, green_light3)
        self.tableWidget.setCellWidget(2, 4, orange_light2)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Name", "Last Update", "Operational", "Security", "Privacy"]
        )
        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalLayout_tool_status.addWidget(self.tableWidget)

        # ***************** INFO BUTTON TOOL STATUS ***************** #
        self.pushButton_info_tool_status = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.pushButton_info_tool_status.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_info_tool_status.setSizePolicy(sizePolicy)
        self.pushButton_info_tool_status.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(QFont.Bold)
        self.pushButton_info_tool_status.setFont(font)
        self.pushButton_info_tool_status.setAutoFillBackground(False)
        self.pushButton_info_tool_status.setStyleSheet(
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
        # self.pushButton_info_cyber.setGeometry(200, 150, 100, 30)
        self.pushButton_info_tool_status.setObjectName("pushButton_info_cyber")
        # self.pushButton_info_cyber.setIcon(QIcon('info-information-icon.png'))
        self.pushButton_info_tool_status.clicked.connect(self.info_tool_status)
        self.verticalLayout_tool_status.addWidget(
            self.pushButton_info_tool_status, 0, QtCore.Qt.AlignRight
        )
        # *************************************************** #
        # *************************************************** #
        self.verticalLayout.addLayout(self.verticalLayout_tool_status)
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
        """
        Sets the text for various widgets in the MainWindow.

        Parameters:
        MainWindow (QMainWindow): The main window of the application.

        This function uses the QtCore.QCoreApplication.translate method to set the text
        for various buttons, labels, and other widgets in the MainWindow. The text is
        set in HTML format to allow for styling, such as text alignment and color.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Load Posts"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        # self.pushButton_21.setText(_translate("MainWindow", "Button 555"))
        # print(self.pushButton_21.text())
        self.label_6.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Moderator Visual Component</span></p></body></html>',
            )
        )
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">List of Toxic Posts</span></p></body></html>',
            )
        )
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Edit a post from the list / Create your own post</span></p></body></html>',
            )
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Tools\' Status</span></p></body></html>',
            )
        )
        self.pushButton_5.setText(_translate("MainWindow", "Check Toxicity"))
        self.pushButton_info_cyber.setText(_translate("MainWindow", "(?)"))
        self.pushButton_ppml_stats.setText(_translate("MainWindow", "PPML Metrics"))
        self.pushButton_ppml_refresh.setText(
            _translate("MainWindow", "Refresh Metrics")
        )
        self.pushButton_info_tool_status.setText(_translate("MainWindow", "(?)"))
        # self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Statistics</span></p></body></html>"))
        # ***************************
        self.label_cybersecurity.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Cybersecurity</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Security in Fairness Model</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Security in Chatbot</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Security in Translator</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats7.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Security in XYZ AI Model</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">LOW</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">MEDIUM</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats6.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">HIGH</span></p></body></html>',
            )
        )
        self.label_cybersecurity_stats8.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">CRITICAL</span></p></body></html>',
            )
        )
        self.label_ppml.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" color:#ffffff;">Privacy</span></p></body></html>',
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

        tox_eval = fairness_model.predict(np.array([pressed_button.text()]))[0][0]
        print(f"Toxic Eval:{tox_eval}")

        if tox_eval > 0.5:
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
        else:
            html_text = []
            for word in words:
                html_text.append(word)

        highlighted_text = " ".join(html_text)
        self.textBrowser.clear()
        self.textBrowser.appendHtml(highlighted_text)

    def add_button(self, text):
        """
        Adds a button with specified text to the UI.
        This method creates a button with text retrieved from the tweets list based on the provided index.
        The button's appearance and size are adjusted, and it is added to the vertical group box.
        The button is also connected to the clickme method for handling click events.
        Args:
            text (str): The index of the tweet to be displayed on the button.
        Returns:
            QPushButton: The created button with the specified text.
        """

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
        font = QtGui.QFont("Arial", 14)
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
        Highlights plain text in the QTextEdit widget based on toxicity evaluation.
        This method retrieves the plain text from the QTextEdit widget, evaluates its toxicity using a fairness model,
        and highlights the text based on the evaluation. If the toxicity evaluation score is greater than 0.5, it highlights
        each word with a background color that varies depending on the word's index in a list of unique words. If the score
        is 0.5 or less, the text remains unhighlighted.
        The unique words are loaded from a NumPy file located at "./data/unique_words.npy".
        The highlighted text is then set back to the QTextEdit widget.
        Returns:
            None
        """
        plain_text = self.plainTextEdit.toPlainText()
        if plain_text:
            words = plain_text.split()
            unique_words = np.load("./data/unique_words.npy")

            tox_eval = fairness_model.predict(np.array([plain_text]))[0][0]
            print(f"Toxic Eval:{tox_eval}")

            if tox_eval > 0.5:
                html_text = []
                for word in words:
                    word_idx = np.argwhere(unique_words == word)
                    if word in unique_words:
                        html_text.append(
                            "<span style='background-color: rgb({}, 165, 73);'>{}</span>".format(
                                255 - 255 * word_idx[0][0] / len(unique_words), word
                            )
                        )
                    else:
                        html_text.append(word)
            else:
                html_text = []
                for word in words:
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
            font = QtGui.QFont("Arial", 12)
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
        """
        Displays a message box asking the user if they would like to exit the application.

        If the user selects 'Yes', the application will quit. If the user selects 'No', the application will continue running.
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Exit")
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

    def info_cybersecurity(self):
        """
        Displays a message box with cybersecurity tool indications.

        The message box contains information about the security status of the model,
        categorized into four levels:
        - LOW: The Model is Secure
        - MEDIUM: The Model is Vulnerable
        - HIGH: Significant Security Risk
        - CRITICAL: The Model is Unsafe

        The message box has a title "Cybersecurity Tool Indications" and uses Arial font with size 14.
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Cybersecurity Tool Indications")
        font = QtGui.QFont("Arial", 14)
        msg.setFont(font)
        msg.setText(
            "LOW : The Model is Secure \nMEDIUM : The Model is Vulnerable \nHIGH : Significant Security Risk \nCRITICAL : The Model is Unsafe "
        )
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def info_tool_status(self):
        """
        Displays a message box with the status indications of the cybersecurity tool.

        The message box contains the following status indications:
        - GREEN: Fully Secure/Private
        - ORANGE: Some Security/Privacy Criteria Are Not Fulfilled
        - RED: Not Secure/Private

        The message box has the title "Cybersecurity Tool Indications" and uses the Arial font with size 14.
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Tools' Status Indications")
        font = QtGui.QFont("Arial", 14)
        msg.setFont(font)
        msg.setText(
            "GREEN : Fully Secure/Private \nORANGE : Some Security/Privacy Criteria Are \n                    Not Fulfilled" +
            " \nRED : Not Secure/Private "
        )
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def show_ppml_stats(self):
        """
        Displays a dialog with the Privacy Preserving Machine Learning Tool Metrics.

        This method creates a QDialog window that shows an image of the metrics
        for the Privacy Preserving Machine Learning Tool. The image is loaded
        from "figures/models_vpe.png" and displayed in a QLabel within the dialog.

        The dialog is resized to fit the dimensions of the image and is displayed
        modally, blocking interaction with other windows until it is closed.
        """
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Privacy Preserving Machine Learning Tool Metrics")
        lay = QtWidgets.QVBoxLayout(dialog)
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("figures/models_vpe.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        dialog.resize(pixmap.width(), pixmap.height())
        lay.addWidget(label)
        dialog.show()
        dialog.exec_()


class ImageWidget(QtWidgets.QWidget):

    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QtGui.QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


if __name__ == "__main__":

    checkpoint_path = (
        "./models/differentially_private/model.{epoch:02d}-{val_accuracy:.4f}.ckpt"
    )
    checkpoint_dir = os.path.dirname(checkpoint_path)
    best = tf.train.latest_checkpoint(checkpoint_dir)
    fairness_model = create_dp_model()
    fairness_model.load_weights(best)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Moderator_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
