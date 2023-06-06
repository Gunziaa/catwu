# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catwu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, PushButton, RadioButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(350, 284)
        Form.setWindowOpacity(0.900000000000000)
        Form.setStyleSheet(u"background-color: rgba(231, 255, 251, 90)\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 2, 348, 281))
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(500, 350))
        self.widget.setStyleSheet(u"")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 150, 231))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 151, 231))
        font = QFont()
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(u"border-style:none;\n"
"background-color: rgba(197, 236, 233, 50);\n"
"border-radius: 5px\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 151, 231))
        self.verticalLayout_g = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_g.setSpacing(3)
        self.verticalLayout_g.setObjectName(u"verticalLayout_g")
        self.verticalLayout_g.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_input = LineEdit(self.widget)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setGeometry(QRect(0, 2, 150, 30))
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(150, 32, 191, 241))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 40, 181, 31))
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 181, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_delay_mini = LineEdit(self.layoutWidget)
        self.lineEdit_delay_mini.setObjectName(u"lineEdit_delay_mini")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_delay_mini.sizePolicy().hasHeightForWidth())
        self.lineEdit_delay_mini.setSizePolicy(sizePolicy2)
        self.lineEdit_delay_mini.setMinimumSize(QSize(35, 30))
        self.lineEdit_delay_mini.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_delay_mini)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(15, 0))
        self.label_2.setMaximumSize(QSize(15, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_delay_max = LineEdit(self.layoutWidget)
        self.lineEdit_delay_max.setObjectName(u"lineEdit_delay_max")
        sizePolicy2.setHeightForWidth(self.lineEdit_delay_max.sizePolicy().hasHeightForWidth())
        self.lineEdit_delay_max.setSizePolicy(sizePolicy2)
        self.lineEdit_delay_max.setMinimumSize(QSize(35, 30))
        self.lineEdit_delay_max.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_delay_max)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 115, 181, 41))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 81, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.lineEdit_coiled_key = LineEdit(self.page)
        self.lineEdit_coiled_key.setObjectName(u"lineEdit_coiled_key")
        self.lineEdit_coiled_key.setGeometry(QRect(85, 5, 95, 30))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit_circulate_key = LineEdit(self.page_2)
        self.lineEdit_circulate_key.setObjectName(u"lineEdit_circulate_key")
        self.lineEdit_circulate_key.setGeometry(QRect(85, 5, 95, 30))
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 81, 21))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.page_2)
        self.Button_delete = PushButton(self.frame_2)
        self.Button_delete.setObjectName(u"Button_delete")
        self.Button_delete.setGeometry(QRect(100, 0, 91, 32))
        self.Button_delete.setMinimumSize(QSize(80, 30))
        self.Button_add = PushButton(self.frame_2)
        self.Button_add.setObjectName(u"Button_add")
        self.Button_add.setGeometry(QRect(8, 0, 90, 32))
        self.Button_add.setMinimumSize(QSize(80, 30))
        self.Button_stop = PushButton(self.frame_2)
        self.Button_stop.setObjectName(u"Button_stop")
        self.Button_stop.setGeometry(QRect(10, 200, 181, 41))
        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 80, 181, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.radioButton_coiled_mode = RadioButton(self.layoutWidget1)
        self.radioButton_coiled_mode.setObjectName(u"radioButton_coiled_mode")
        self.radioButton_coiled_mode.setMinimumSize(QSize(0, 30))
        self.radioButton_coiled_mode.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_coiled_mode)

        self.radioButton_circulate_mode = RadioButton(self.layoutWidget1)
        self.radioButton_circulate_mode.setObjectName(u"radioButton_circulate_mode")
        self.radioButton_circulate_mode.setMinimumSize(QSize(0, 30))
        self.radioButton_circulate_mode.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_circulate_mode)

        self.Button_start = PushButton(self.frame_2)
        self.Button_start.setObjectName(u"Button_start")
        self.Button_start.setEnabled(True)
        self.Button_start.setGeometry(QRect(10, 155, 181, 41))
        self.Button_start.setStyleSheet(u"\n"
"QPushButton:disabled {\n"
"	border-radius: 3px;\n"
"    background-color: #009faa;\n"
"	border: none;\n"
"	color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"        background-color:rgba(255, 255, 255, 90);  \n"
"    }\n"
"\n"
"")
        self.Button_close = PushButton(self.widget)
        self.Button_close.setObjectName(u"Button_close")
        self.Button_close.setGeometry(QRect(310, 2, 30, 30))
        self.Button_close.setStyleSheet(u" QPushButton:hover {\n"
"        background-color:rgb(255, 158, 129); \n"
"		border-radius: 5px;\n"
"    }")
        self.Button_minimize = PushButton(self.widget)
        self.Button_minimize.setObjectName(u"Button_minimize")
        self.Button_minimize.setGeometry(QRect(280, 2, 30, 30))
        self.Button_text = PushButton(self.widget)
        self.Button_text.setObjectName(u"Button_text")
        self.Button_text.setGeometry(QRect(195, 2, 85, 30))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 348, 281))
        self.label_6.setMinimumSize(QSize(348, 281))
        self.label_6.setPixmap(QPixmap(u"12.jpg"))
        self.label_6.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)
        self.radioButton_coiled_mode.toggled.connect(self.stackedWidget.show)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit_input.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u5ef6\u65f6/\u6beb\u79d2\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_delay_mini.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u" ~", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8fde\u53d1\u5feb\u6377\u952e:", None))
        self.lineEdit_circulate_key.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u5feb\u6377\u952e:", None))
#if QT_CONFIG(tooltip)
        self.Button_delete.setToolTip(QCoreApplication.translate("Form", u"\u5220\u9664\u6309\u94ae", None))
#endif // QT_CONFIG(tooltip)
        self.Button_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.Button_add.setToolTip(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6309\u94ae", None))
#endif // QT_CONFIG(tooltip)
        self.Button_add.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(tooltip)
        self.Button_stop.setToolTip(QCoreApplication.translate("Form", u"\u505c\u6b62\u811a\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.Button_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62/F12", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f\uff1a", None))
        self.radioButton_coiled_mode.setText(QCoreApplication.translate("Form", u"\u8fde\u53d1", None))
        self.radioButton_circulate_mode.setText(QCoreApplication.translate("Form", u"\u5faa\u73af", None))
#if QT_CONFIG(tooltip)
        self.Button_start.setToolTip(QCoreApplication.translate("Form", u"\u6fc0\u6d3b\u811a\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.Button_start.setText(QCoreApplication.translate("Form", u"\u542f\u52a8/F11", None))
#if QT_CONFIG(tooltip)
        self.Button_close.setToolTip(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.Button_close.setText(QCoreApplication.translate("Form", u"X", None))
#if QT_CONFIG(tooltip)
        self.Button_minimize.setToolTip(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.Button_minimize.setText(QCoreApplication.translate("Form", u"-----", None))
#if QT_CONFIG(tooltip)
        self.Button_text.setToolTip(QCoreApplication.translate("Form", u"\u55b5\u5514\u8f6f\u4ef6\u6587\u6863/\u672c\u8f6f\u4ef6\u5b8c\u5168\u514d\u8d39/\u7fa4:222059950", None))
#endif // QT_CONFIG(tooltip)
        self.Button_text.setText(QCoreApplication.translate("Form", u"\u55b5\u5514\u6587\u6863", None))
        self.label_6.setText("")
    # retranslateUi

