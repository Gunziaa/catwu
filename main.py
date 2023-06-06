import json
import sys
from ctypes import windll

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QTextEdit
from markdown import markdown
import threading

from pynput.keyboard import Listener

from ui_catwu import Ui_Form

import auto_key
from qfluentwidgets import ToggleButton


class CatWu(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # 数据初始化
        self.c = Config("autokey.json")
        self.config = self.c.read_config()

        self.dd = auto_key.DDkey()  # 按键类

        self.listener = None  # 钩子
        self.listener_thread = None  # 钩子线程
        self.delay_mini = None
        self.delay_max = None
        self.res = None  # 添加按钮

        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.is_coiled_mode = True  # 连发开关 防止重复启动

        self.is_switch = False  # F11 总开关
        # 添加按钮 删除按钮
        self.lineEdit_input.textChanged.connect(self.on_lineEdit_add_input)
        self.lineEdit_input.setPlaceholderText('设置快捷键')
        self.Button_add.clicked.connect(self.on_Button_add)
        self.Button_delete.clicked.connect(self.on_Button_delete)

        # 延时
        self.lineEdit_delay_mini.textChanged.connect(self.on_delay_mini)
        self.lineEdit_delay_mini.setText(self.config["Velocity"]["Interval_time_mini"])

        self.lineEdit_delay_max.textChanged.connect(self.on_delay_max)
        self.lineEdit_delay_max.setText(self.config["Velocity"]["Interval_time_max"])

        # 模式选择
        self.radioButton_coiled_mode.toggled.connect(self.on_coiled_mode)  # 连发选择
        self.radioButton_coiled_mode.setChecked(self.config['Set_key']['coiled_mode'])

        self.radioButton_circulate_mode.toggled.connect(self.on_circulate_mode)  # 循环选择
        self.radioButton_circulate_mode.setChecked(self.config['Set_key']['circulate_mode'])  # 设置默认选中状态

        # 模式快捷键
        self.lineEdit_coiled_key.textChanged.connect(self.on_coiled_key)  # 连发快捷键
        self.lineEdit_coiled_key.setText(self.config["Set_key"]["coiled_key"])

        self.lineEdit_circulate_key.textChanged.connect(self.on_circulate_key)  # 循环快捷键
        self.lineEdit_circulate_key.setText(self.config["Set_key"]["circulate_key"])

        self.Button_stop.clicked.connect(self.on_Button_stop)
        self.Button_start.clicked.connect(self.on_Button_start)

        # 关于窗口
        self.Button_close.clicked.connect(self.on_window_close)
        self.Button_minimize.clicked.connect(self.on_window_minimize)
        self.Button_text.clicked.connect(self.on_Button_help)

        self.key_list()  # 按键列表

        # 图标
        self.setWindowTitle('[喵唔按键]本软件完全免费')
        self.icon = QPixmap('1.ico')
        self.setWindowIcon(self.icon)

        # 文档
        self.text_edit_documentation = QTextEdit()
        self.text_edit_documentation.setWindowIcon(self.icon)

        self.listener_thread_start()  # 启动钩子

    # _________________________________________________________________
    # 信号关联

    def on_Button_stop(self):
        self.Button_start.setEnabled(True)
        self.Button_start.setText('启动/F11')

        self.is_switch = False
        self.dd.is_circulate = False

    def on_Button_start(self):
        if self.Button_start.isEnabled():
            self.dd.delay_max = self.config["Velocity"]["Interval_time_max"]
            self.dd.delay_mini = self.config["Velocity"]["Interval_time_mini"]
            self.Button_start.setEnabled(False)
            # 启动后更新按钮文本
            self.Button_start.setProperty("stop_text", "已启动/按F12停止")
            self.Button_start.setText(self.Button_start.property("stop_text"))

            self.is_switch = True

            print('启动')

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

    def on_window_minimize(self):
        """窗口最小化"""
        self.showMinimized()

    def on_window_close(self):
        """关闭窗口"""
        self.close()

    def on_coiled_key(self):
        # 连发快捷键
        coi = self.lineEdit_coiled_key.text()
        if coi in self.config["PressKey"]:
            self.lineEdit_coiled_key.clear()
            self.lineEdit_coiled_key.setPlaceholderText('重复键')
            return

        if coi in self.dd.vk:
            self.config['Set_key']["coiled_key"] = coi
        else:
            self.lineEdit_coiled_key.clear()
            self.lineEdit_coiled_key.setPlaceholderText('非法字符')

        self.c.undate_config(self.config)  # 更新数据

    def on_circulate_key(self):
        # 循环快捷键
        cir = self.lineEdit_circulate_key.text()
        if cir in self.config["PressKey"]:
            self.lineEdit_circulate_key.clear()
            self.lineEdit_circulate_key.setPlaceholderText('重复键')
            return

        if cir in self.dd.vk:
            self.config['Set_key']['circulate_key'] = cir
        else:
            self.lineEdit_circulate_key.clear()
            self.lineEdit_circulate_key.setPlaceholderText('非法字符')

        self.c.undate_config(self.config)  # 更新数据

    def on_delay_mini(self):
        delay_mini = self.lineEdit_delay_mini.text()
        for i in delay_mini:
            if i in '1234567890':
                self.config['Velocity']["Interval_time_mini"] = delay_mini
            else:
                self.lineEdit_delay_mini.clear()

        self.c.undate_config(self.config)  # 更新数据

    def on_delay_max(self):
        delay_max = self.lineEdit_delay_max.text()
        for i in delay_max:
            if i in '1234567890':
                self.config['Velocity']["Interval_time_max"] = delay_max
            else:
                self.lineEdit_delay_max.clear()
        self.c.undate_config(self.config)  # 更新数据

    def on_Button_delete(self):
        """删除键位"""
        for i in self.config["Selected"]:
            self.config["PressKey"].remove(i)
        self.config["Selected"].clear()
        self.key_list()

    def on_Button_add(self):
        """添加按键"""
        if self.res is None:
            self.lineEdit_input.setPlaceholderText('不可以是空的')
        else:
            if self.res not in self.config["PressKey"]:
                self.config["PressKey"].append(self.res)
            else:
                self.config["PressKey"].remove(self.res)
                self.config["PressKey"].append(self.res)

            self.key_list()  # 更新列表
        self.lineEdit_input.clear()
        self.c.undate_config(self.config)  # 更新数据

    def on_lineEdit_add_input(self):
        """添加键位输入框"""
        self.res = self.lineEdit_input.text()
        if self.res == self.config["Set_key"]["coiled_key"] or self.res == self.config["Set_key"]["circulate_key"]:
            self.lineEdit_input.clear()
            self.lineEdit_input.setPlaceholderText('快捷键重复')

        elif self.res not in self.dd.vk:
            self.lineEdit_input.clear()
            self.lineEdit_input.setPlaceholderText('输入单个小写字母')

    def key_list(self):
        """滚动区域"""
        self.clear_layout()  # 清除控件避免重复显示
        self.verticalLayout_g.setAlignment(Qt.AlignTop)

        for btn in reversed(self.config["PressKey"]):
            self.btn = ToggleButton(btn, self)
            self.btn.clicked.connect(self.on_Button_key)
            self.verticalLayout_g.addWidget(self.btn)

            if btn in self.config["Selected"]:  # 判断有没有被选中
                self.btn.setChecked(True)

        self.update()

    def on_Button_key(self):
        """左边选中的按钮"""
        sender = self.sender()
        btn_text = sender.text()
        if self.sender().isChecked():
            self.config["Selected"].append(btn_text)
        else:
            self.config["Selected"].remove(btn_text)

    def clear_layout(self):
        """清除布局中的控件"""
        while self.verticalLayout_g.count() > 0:
            item = self.verticalLayout_g.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def on_coiled_mode(self):
        """stackedWidget 页面"""
        if self.radioButton_coiled_mode.isChecked():
            self.stackedWidget.setCurrentIndex(0)  # 页面切换

            self.config["Set_key"]["coiled_mode"] = True
            self.config["Set_key"]["circulate_mode"] = False

    def on_circulate_mode(self):
        """stackedWidget 页面"""
        self.stackedWidget.setCurrentIndex(1)
        if self.radioButton_circulate_mode.isChecked():
            self.config["Set_key"]["coiled_mode"] = False
            self.config["Set_key"]["circulate_mode"] = True

            # print('连发', self.radioButton_coiled_mode.isChecked())
            # print('循环', self.radioButton_circulate_mode.isChecked())

    # _________________________________________________________________
    # 窗口事件

    def closeEvent(self, event):
        self.listener.stop()  # 停止钩子
        self.c.undate_config(self.config)  # 更新数据
        sys.exit()

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

    def focusInEvent(self, event):
        self.lineEdit_input.setPlaceholderText('')
        super().focusInEvent(event)

    # ________________________________________________________
    # 快捷键钩子

    def is_listener(self):
        """钩子函数"""
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

    def on_press(self, key):
        try:
            if key.char == self.config['Set_key']['coiled_key'] and self.config['Set_key'][
                'coiled_mode'] and self.is_switch and self.is_coiled_mode:
                self.key_star()
                self.is_coiled_mode = False
                print('开始连发1')
            # print(f'按键 {key} 被按下')

        except AttributeError:
            if key.name == self.config['Set_key']['coiled_key'] and self.config['Set_key'][
                'coiled_mode'] and self.is_switch and self.is_coiled_mode:
                self.key_star()
                self.is_coiled_mode = False
                print('开始连发2')

    def on_release(self, key):
        print(key, '松开')
        try:
            if key.char == self.config['Set_key']['coiled_key'] and self.config['Set_key'][
                'coiled_mode'] and self.is_switch:
                self.key_stop()
                self.is_coiled_mode = True
                print('停止连发')

            elif key.char == self.config['Set_key']['circulate_key'] and self.config['Set_key'][
                'circulate_mode'] and self.is_switch:
                if self.dd.is_circulate:
                    self.dd.is_circulate = False
                else:
                    self.dd.is_circulate = True
                self.dd.dd_click()
                print('开始循环模式')

        except AttributeError:
            if key.name == self.config['Switch']['start']:
                self.on_Button_start()
                print('激活脚本')
            elif key.name == self.config['Switch']['stop']:
                self.on_Button_stop()
                print('停止脚本')

            if key.name == self.config['Set_key']['coiled_key'] and self.config['Set_key'][
                'coiled_mode'] and self.is_switch:
                self.key_stop()
                self.is_coiled_mode = True
                print('停止连发')

            elif key.name == self.config['Set_key']['circulate_key'] and self.config['Set_key'][
                'circulate_mode'] and self.is_switch:

                if self.dd.is_circulate:
                    self.dd.is_circulate = False
                else:
                    self.dd.is_circulate = True
                if self.dd.is_circulate:
                    self.key_star()
                    print('开始循环模式')

            if key.name == self.config['Set_key']['coiled_key'] and self.config['Set_key'][
                'coiled_mode'] and self.is_switch:
                self.key_stop()
                self.is_coiled_mode = True
                print('停止连发')

    def listener_thread_start(self):
        """钩子线程"""
        self.listener_thread = threading.Thread(target=self.is_listener)
        self.listener_thread.daemon = True
        self.listener_thread.start()

    # -----------------------------------------------------------------
    # 功能
    def key_star(self):
        self.dd.d_k = self.config['Selected']
        self.dd.dd_click_start()

    def key_stop(self):
        self.dd.dd_click_stop()


class Config:
    """配置类:用于读取,更新配置"""

    def __init__(self, file):
        self.file_path = file

    def read_config(self):
        """读取配置"""
        with open(self.file_path) as js:
            config = json.load(js)
        return config

    def undate_config(self, config):
        """更新配置"""
        with open(self.file_path, 'w') as js:
            json.dump(config, js, indent='\t', ensure_ascii=False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = CatWu()
    c.show()
    sys.exit(app.exec())
