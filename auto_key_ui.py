import sys
from ctypes import windll

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QCheckBox, QButtonGroup, QMessageBox, QTextEdit, QMainWindow
from ui_qsrcroll import Ui_Form

from pynput.keyboard import Listener

import json
import threading
from markdown import markdown

import auto_key


class Qsr(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 钩子线程
        self.listener_thread = None
        # 快捷键钩子
        self.listener = None

        self.time_out = False  # 暂停
        # 循环快捷键
        self.is_switch = False

        # 点击线程
        self.press_thread = None

        # 拖动窗口
        self.__is_dragging = None
        # 配置文件
        self.app_data_path = "E:\Py\catwu\\autokey.json"
        self.config = self.read_config()

        # 按键类
        self.dd = auto_key.DDkey()

        # 设置窗口无边框、工具窗口和置顶窗口标志
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 增加键位
        self.lineEdit_add_input.textChanged.connect(self.on_lineEdit_add_input)
        # 添加按钮
        self.Button_add.clicked.connect(self.on_Button_add)
        # 删除键位按钮
        self.Button_delete_key.clicked.connect(self.on_Button_delete_key)

        # 连发模式
        self.lineEdit_coiled_key.textChanged.connect(self.on_lineEdit_coiled_key)
        self.lineEdit_coiled_key.setText(self.config['Set_key']['coiled_press_key'])  # 设置默认键位

        self.radioButton_coiled.toggled.connect(self.on_radioButton_isChecked)
        self.radioButton_coiled.setChecked(self.config['Set_key']['coiled_key'])  # 设置默认选中

        # 循环模式
        self.lineEdit_circulate_key.textChanged.connect(self.on_lineEdit_circulate_key)
        self.lineEdit_circulate_key.setText(self.config['Set_key']['circulate_press_key'])

        self.radioButton_circulate.toggled.connect(self.on_radioButton_isChecked)
        self.radioButton_circulate.setChecked(self.config['Set_key']['circulate_key'])

        # 间隔时间
        self.lineEdit_Interval_time_mini.textChanged.connect(self.on_lineEdit_Interval_time_mini)
        self.lineEdit_Interval_time_mini.setText(self.config['Velocity']['Interval_time_mini'])

        self.lineEdit_Interval_time_max.textChanged.connect(self.on_lineEdit_Interval_time_max)
        self.lineEdit_Interval_time_max.setText(self.config['Velocity']['Interval_time_max'])

        # 控制开关
        self.Button_start.clicked.connect(self.on_Button_start)
        self.Button_start.setProperty("stop_text", "已启动")
        self.Button_stop.clicked.connect(self.on_Button_stop)

        # 界面开关
        self.Button_close.clicked.connect(self.on_Button_close)
        self.Button_minimize.clicked.connect(self.on_Button_minimize)
        self.Button_help.clicked.connect(self.on_Button_help)

        self.button_group = QButtonGroup()  # 创建按钮组
        self.button_group.addButton(self.radioButton_circulate)
        self.button_group.addButton(self.radioButton_coiled)

        self.add_qsr()  # 初始化按键列表
        self.listener_thread_start()  # 初始化快捷件

        self.setWindowTitle('[喵唔按键]本软件完全免费')
        self.icon = QPixmap('1.ico')
        self.setWindowIcon(self.icon)

        # 文档
        self.text_edit_documentation = QTextEdit()
        self.text_edit_documentation.setWindowIcon(self.icon)

    # 窗口操作---------------------------------------------------------------------

    def prompts(self, texts):
        """创建一个提示窗口"""
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("提示")
        self.msg_box.setText(texts)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.setDefaultButton(QMessageBox.Ok)
        # 设置确定按钮的文本为中文
        ok_button = self.msg_box.button(QMessageBox.Ok)
        ok_button.setText("确定")
        # 显示提示窗口
        self.msg_box.show()

    def mousePressEvent(self, event):
        # 按下鼠标时，记录窗口的初始位置和鼠标位置
        if event.button() == Qt.LeftButton:
            self.__is_dragging = True
            self.__mouse_press_pos = event.globalPos()
            self.__window_pos = self.pos()

    def mouseMoveEvent(self, event):
        # 拖动窗口
        if self.__is_dragging:
            delta = QPoint(event.globalPos() - self.__mouse_press_pos)
            self.move(self.__window_pos + delta)

    def mouseReleaseEvent(self, event):
        # 松开鼠标
        if event.button() == Qt.LeftButton:
            self.__is_dragging = False

    def closeEvent(self, event):
        self.listener_stop()  # 停止快捷键钩子
        sys.exit()

    def on_Button_help(self):
        """文档窗口"""
        with open("README.md", "r", encoding="utf-8") as file:
            markdown_text = file.read()

        # 将 Markdown 转换为 HTML
        html_text = markdown(markdown_text)

        self.text_edit_documentation.setFixedSize(500, 500)
        self.text_edit_documentation.setWindowTitle("喵唔按键文档,本软件完全免费,QQ群:222059950")
        self.text_edit_documentation.setText(html_text)

        self.text_edit_documentation.setReadOnly(True)

        self.text_edit_documentation.show()

    def on_Button_minimize(self):
        """窗口最小化"""
        self.showMinimized()
        print('窗口最小化')

    def on_Button_close(self):
        """关闭界面"""
        print('关闭窗口')
        self.close()

    # 按键脚本配置---------------------------------------------------------------------
    def read_config(self):
        """读取配置"""
        with open(self.app_data_path) as js:
            config = json.load(js)
        return config

    def undate_config(self):
        """更新配置"""
        with open(self.app_data_path, 'w') as js:
            json.dump(self.config, js, indent='\t', ensure_ascii=False)

    def on_lineEdit_Interval_time_mini(self):
        """延时mini"""
        r = self.lineEdit_Interval_time_mini.text()
        for i in r:
            if i not in '1234567890':
                self.lineEdit_Interval_time_mini.clear()
                self.prompts('输入数字')
                return

        self.config['Velocity']['Interval_time_mini'] = r
        self.undate_config()

    def on_lineEdit_Interval_time_max(self):
        """连发速度max"""
        r = self.lineEdit_Interval_time_max.text()
        for i in r:
            if i not in '1234567890':
                self.lineEdit_Interval_time_max.clear()
                self.prompts('输入数字')
                return

        self.config['Velocity']['__这是一个备注__'] = '控制按键速度'
        self.config['Velocity']['Interval_time_max'] = r
        self.undate_config()

    def on_radioButton_isChecked(self):
        """选择循环模式"""
        if self.radioButton_circulate.isChecked():
            self.config['Set_key']['coiled_key'] = False
            self.config['Set_key']['circulate_key'] = True

            self.dd.listener_stop()  # 关闭连发模式

            print("选择循环模式")

        elif self.radioButton_coiled.isChecked():
            self.config['Set_key']['coiled_key'] = True
            self.config['Set_key']['circulate_key'] = False

            self.dd.dd_click_stop()  # 关闭循环模式
            print('选择连发模式')

        self.undate_config()  # 更新数据

        #  更新脚本状态
        self.on_Button_stop()

    def on_lineEdit_circulate_key(self):
        """循环触发键"""
        r = self.lineEdit_circulate_key.text()
        if r not in self.dd.vk:
            self.lineEdit_circulate_key.clear()
            self.prompts('非法字符')
            return


        self.config['Set_key']['circulate_press_key'] = r
        self.undate_config()

    def on_lineEdit_coiled_key(self):
        """连发模式触发键"""
        r = self.lineEdit_coiled_key.text()
        if r not in self.config['Keys']:
            self.lineEdit_coiled_key.clear()
            self.prompts('非法字符')
            return

        self.config['Set_key']['__这是一个备注__'] = {
            'coiled_key': '连发模式',
            'coiled_press_key': '连发模式触发键位',

            'circulate_key': '循环模式',
            'circulate_press_key': '循环模式触发键位'
        }
        self.config['Set_key']['coiled_press_key'] = r
        self.undate_config()

    def on_Button_add(self):
        """添加按键"""
        if self.res not in self.dd.vk:
            self.lineEdit_add_input.clear()
            self.prompts('非法字符')
            return

        if self.res in self.config['PressKey']:
            self.config['PressKey'].remove(self.res)

        self.config['PressKey'].append(self.res)
        self.lineEdit_add_input.clear()
        self.undate_config()
        self.add_qsr()

    def on_lineEdit_add_input(self):
        """添加键位"""
        self.res = self.lineEdit_add_input.text()
        if self.res:
            return self.res

    def on_Button_delete_key(self):
        """删除键位"""
        for i in self.config['Selected']:
            if i in self.config['PressKey']:
                self.config['PressKey'].remove(i)

        self.config['Selected'].clear()
        self.undate_config()
        self.add_qsr()

    def add_qsr(self):
        """键位列表"""
        self.clear_layout()  # 清除控件避免重复显示
        self.verticalLayout.setAlignment(Qt.AlignTop)

        for i in reversed(self.config['PressKey']):
            checkbox = QCheckBox(i)
            checkbox.setStyleSheet("QCheckBox { border: 1px solid black; padding: 5px; }")

            checkbox.stateChanged.connect(self.on_checkbox_state_changed)  # 连接信号与槽函数
            self.verticalLayout.addWidget(checkbox)

            if i in self.config['Selected']:  # 判断是否被勾选
                checkbox.setChecked(True)

        self.update()

    def on_checkbox_state_changed(self, state):
        """复选框是否选中判断"""
        checkbox = self.sender()
        if checkbox.isChecked():
            if checkbox.text() not in self.config['Selected']:
                self.config['Selected'].append(checkbox.text())
        else:
            self.config['Selected'].remove(checkbox.text())

        self.undate_config()

    def clear_layout(self):
        """清除布局中的控件"""
        while self.verticalLayout.count() > 0:
            item = self.verticalLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # 按键脚本操作---------------------------------------------------------------------
    def on_Button_stop(self):
        """停止"""
        if self.config['Set_key']['coiled_key']:  # 连发
            self.dd.listener_stop()
            self.dd.stop_clicking()

        if self.config['Set_key']['circulate_key']:  # 循环
            self.dd.dd_click_stop()

        if self.press_thread:
            self.press_thread.join()

        self.is_switch = False
        self.time_out = True  # 暂停

        self.Button_start.setEnabled(True)
        self.Button_start.setText('启动/11')
        print('停止脚本')


    def on_Button_start(self):
        """开始按钮"""
        if self.Button_start.isEnabled():
            self.is_switch = True
            self.time_out = False  # 暂停

            self.coiled_thread_start()  # 开启连发模式
            self.Button_start.setEnabled(False)
            # 启动后更新按钮文本
            self.Button_start.setText(self.Button_start.property("stop_text"))




    def disable_button(self):
        """更新启动按钮的文字"""
        if self.Button_start.isEnabled():
            print('禁用按钮')
            self.Button_start.setText(self.Button_start.property("start_text"))
        else:
            self.Button_start.setText(self.Button_start.property("stop_text"))

    def start_circulate_key(self):
        """按键:循环模式"""
        self.dd.k = self.config['Set_key']['circulate_press_key']  # 触发键
        self.dd.d_k = self.config['Selected']  # 目标键

        self.dd.delay_mini = int(self.config['Velocity']['Interval_time_mini'])
        self.dd.delay_max = int(self.config['Velocity']['Interval_time_max'])

        self.dd.dd_click_start()

    def start_coiled_key(self):
        """按键:连发模式"""
        self.dd.k = self.config['Set_key']['coiled_press_key']  # 触发键
        self.dd.d_k = self.config['Selected']  # 目标键

        self.dd.delay_mini = int(self.config['Velocity']['Interval_time_mini'])
        self.dd.delay_max = int(self.config['Velocity']['Interval_time_max'])

        self.dd.start()

    # 快捷键---------------------------------------------------------------------

    def listener_thread_start(self):
        """钩子线程"""
        self.listener_thread = threading.Thread(target=self.is_listener)
        # self.press_thread.daemon = True
        self.listener_thread.start()

    def is_listener(self):
        """钩子函数"""
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

    def on_press(self, key):
        # print(f'按键 {key} 被按下')
        pass

    def on_release(self, key):
        """快捷键状态判断"""
        try:
            # 获取按下的键
            if key.char == self.config['Switch']:
                if self.is_switch:
                    self.is_switch = False
                    # print('快捷键关')
                else:
                    self.is_switch = True
                    # print('快捷键开')

            if key.char == self.config['Set_key']['circulate_press_key']:
                if self.time_out:
                    self.time_out = False
                else:
                    self.time_out = True

                if self.time_out:
                    self.circulate_thread_start()  # 启动循环

        except AttributeError:
            # 对于特殊键（如功能键、控制键等），获取其名称
            if key.name == self.config['Switch']['start']:
                self.on_Button_start()

            if key.name == self.config['Switch']['stop']:
                self.on_Button_stop()


            if key.name == self.config['Set_key']['circulate_press_key']:

                if self.time_out:
                    self.time_out = False
                else:
                    self.time_out = True

                print('time_out:', self.time_out)

                if self.time_out:
                    self.circulate_thread_start()  # 启动循环模式
                else:
                    self.dd.dd_click_stop()

    def coiled_thread_start(self):
        if self.config['Set_key']['coiled_key'] and self.is_switch:  # 连发
            self.press_thread = threading.Thread(target=self.start_coiled_key)
            self.press_thread.daemon = True
            print("执行连发模式")
            self.press_thread.start()

    def circulate_thread_start(self):
        if self.config['Set_key']['circulate_key'] and self.is_switch:  # 循环
            self.press_thread = threading.Thread(target=self.start_circulate_key)
            self.press_thread.daemon = True
            print('执行循环模式')
            self.press_thread.start()

    def listener_stop(self):
        # 停止钩子
        self.listener.stop()


def messagebox(text_1):
    app = QApplication()
    """创建一个提示窗口"""
    msg_box = QMessageBox()
    msg_box.setWindowTitle("提示")
    msg_box.setText(text_1)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    # 设置确定按钮的文本为中文
    ok_button = msg_box.button(QMessageBox.Ok)
    ok_button.setText("确定")
    # 显示提示窗口
    msg_box.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    if windll.shell32.IsUserAnAdmin():
        app = QApplication()
        qs = Qsr()
        qs.show()
        sys.exit(app.exec())
    else:
        messagebox('    请点击右键\n\n以管理员身份运行')
        sys.exit()
