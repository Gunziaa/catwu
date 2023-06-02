# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qsrcroll.ui'
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
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(326, 226)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 325, 221))
        self.widget.setStyleSheet(u"QPushButton:hover {\n"
"		border-radius: 3px;\n"
"        background-color: #99d6ff;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"		border-radius: 3px;\n"
"        background-color: #73a0bf;  /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QRadioButton:hover {\n"
"		border-radius: 3px;\n"
"        background-color: #99d6ff;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"		border-radius: 3px;\n"
"        background-color: #73a0bf;  /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"\n"
"")
        self.Button_close = QPushButton(self.widget)
        self.Button_close.setObjectName(u"Button_close")
        self.Button_close.setGeometry(QRect(300, 0, 25, 25))
        self.Button_close.setFocusPolicy(Qt.NoFocus)
        self.Button_close.setStyleSheet(u" QPushButton:hover {\n"
"        background-color: #ff4639;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #2c3e50;  /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.Button_minimize = QPushButton(self.widget)
        self.Button_minimize.setObjectName(u"Button_minimize")
        self.Button_minimize.setGeometry(QRect(275, 0, 25, 25))
        self.Button_minimize.setFocusPolicy(Qt.NoFocus)
        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(110, 0, 101, 221))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 102, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(115, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 11, 110, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_coiled_key = QLineEdit(self.layoutWidget)
        self.lineEdit_coiled_key.setObjectName(u"lineEdit_coiled_key")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_coiled_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_coiled_key.setSizePolicy(sizePolicy1)
        self.lineEdit_coiled_key.setMinimumSize(QSize(50, 0))
        self.lineEdit_coiled_key.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_coiled_key)

        self.radioButton_coiled = QRadioButton(self.frame_2)
        self.radioButton_coiled.setObjectName(u"radioButton_coiled")
        self.radioButton_coiled.setGeometry(QRect(1, 40, 71, 19))
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radioButton_coiled.sizePolicy().hasHeightForWidth())
        self.radioButton_coiled.setSizePolicy(sizePolicy2)
        self.radioButton_coiled.setMaximumSize(QSize(80, 20))
        self.layoutWidget1 = QWidget(self.frame_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 70, 102, 51))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_circulate_key = QLineEdit(self.layoutWidget1)
        self.lineEdit_circulate_key.setObjectName(u"lineEdit_circulate_key")
        self.lineEdit_circulate_key.setMinimumSize(QSize(50, 0))
        self.lineEdit_circulate_key.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_circulate_key)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.radioButton_circulate = QRadioButton(self.layoutWidget1)
        self.radioButton_circulate.setObjectName(u"radioButton_circulate")
        self.radioButton_circulate.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_2.addWidget(self.radioButton_circulate)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 130, 101, 91))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Button_delete_key = QPushButton(self.frame_4)
        self.Button_delete_key.setObjectName(u"Button_delete_key")
        self.Button_delete_key.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_6.addWidget(self.Button_delete_key)

        self.Button_start = QPushButton(self.frame_4)
        self.Button_start.setObjectName(u"Button_start")
        self.Button_start.setEnabled(True)
        self.Button_start.setMinimumSize(QSize(0, 23))
        self.Button_start.setFocusPolicy(Qt.NoFocus)
        self.Button_start.setStyleSheet(u"QPushButton:disabled {\n"
"        background-color: #73a0bf; /* \u7981\u7528\u65f6\u7684\u80cc\u666f\u8272 */\n"
"		border: none;\n"
"		border-radius: 5px;\n"
"		text:\u7981\u7528\n"
"    }\n"
"")

        self.verticalLayout_6.addWidget(self.Button_start)

        self.Button_stop = QPushButton(self.frame_4)
        self.Button_stop.setObjectName(u"Button_stop")
        self.Button_stop.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_6.addWidget(self.Button_stop)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 130, 100, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 70, 100, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(105, 1, 3, 221))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget2 = QWidget(self.widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 102, 221))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.layoutWidget2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 30))
        self.frame.setMaximumSize(QSize(100, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget3 = QWidget(self.frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 102, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_add_input = QLineEdit(self.layoutWidget3)
        self.lineEdit_add_input.setObjectName(u"lineEdit_add_input")
        self.lineEdit_add_input.setMinimumSize(QSize(50, 30))
        self.lineEdit_add_input.setMaximumSize(QSize(50, 30))
        self.lineEdit_add_input.setFrame(True)
        self.lineEdit_add_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_add_input.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_add_input)

        self.Button_add = QPushButton(self.layoutWidget3)
        self.Button_add.setObjectName(u"Button_add")
        self.Button_add.setMinimumSize(QSize(50, 30))
        self.Button_add.setFocusPolicy(Qt.NoFocus)
        self.Button_add.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.Button_add)


        self.verticalLayout_5.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.layoutWidget2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(120, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 181))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 3, 0, 10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(215, 3, 3, 220))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.Button_help = QPushButton(self.widget)
        self.Button_help.setObjectName(u"Button_help")
        self.Button_help.setGeometry(QRect(228, 0, 45, 25))
        self.Button_help.setFocusPolicy(Qt.NoFocus)
        self.layoutWidget4 = QWidget(self.widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(220, 30, 122, 67))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_Interval_time_mini = QLineEdit(self.layoutWidget4)
        self.lineEdit_Interval_time_mini.setObjectName(u"lineEdit_Interval_time_mini")

        self.horizontalLayout_4.addWidget(self.lineEdit_Interval_time_mini)

        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_Interval_time_max = QLineEdit(self.layoutWidget4)
        self.lineEdit_Interval_time_max.setObjectName(u"lineEdit_Interval_time_max")

        self.horizontalLayout_4.addWidget(self.lineEdit_Interval_time_max)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.Button_close.setToolTip(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.Button_close.setText(QCoreApplication.translate("Form", u"X", None))
#if QT_CONFIG(tooltip)
        self.Button_minimize.setToolTip(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.Button_minimize.setText(QCoreApplication.translate("Form", u"--", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5feb\u6377\u952e\uff1a", None))
        self.lineEdit_coiled_key.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5b57\u7b26\u4e32", None))
        self.radioButton_coiled.setText(QCoreApplication.translate("Form", u"\u8fde\u53d1\u6a21\u5f0f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5feb\u6377\u952e\uff1a", None))
        self.lineEdit_circulate_key.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5b57\u7b26\u4e32", None))
        self.radioButton_circulate.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u6a21\u5f0f", None))
        self.Button_delete_key.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u52fe\u9009\u952e\u4f4d", None))
        self.Button_start.setText(QCoreApplication.translate("Form", u"\u542f\u52a8/f11", None))
        self.Button_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62/f12", None))
        self.lineEdit_add_input.setText("")
        self.lineEdit_add_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5b57\u7b26\u4e32", None))
        self.Button_add.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.Button_help.setText(QCoreApplication.translate("Form", u"\u6587\u6863", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5ef6\u65f6(\u6beb\u79d2)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"--", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"1\u79d2 = 1000\u6beb\u79d2", None))
    # retranslateUi

