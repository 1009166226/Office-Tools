# pyside6-uic untitled.ui -o ui.py
import sys
from PySide6.QtWidgets import  QApplication, QMainWindow, QListWidgetItem

from ui import Ui_MainWindow
from ifta import statistics_ifta


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.files = []  # ==> 默认文本内容
        # 使用ui文件，导入定义的界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        # 文件列表
        self.fileList = self.ui.fileList

        # 文字输出
        self.textBrowser = self.ui.textBrowser

        # 填表按键
        self.bt_Filling = self.ui.Filling
        self.bt_Filling.clicked.connect(self.submit_iftas)

        # 移除选中文件
        self.bt_Remove = self.ui.Remove
        self.bt_Remove.clicked.connect(self.remove_files)

        # 清除所有
        self.bt_Clear = self.ui.Clear
        self.bt_Clear.clicked.connect(self.clearAll)

    def submit_iftas(self):
        if self.files:
            paths = [file.text() for file in self.files]
            statistics_ifta(paths,self.textBrowser)
        else:
            self.ui.textBrowser.setText("There is no files!!!!")

    def remove_files(self):
        for item in self.fileList.selectedItems():
            self.fileList.takeItem(self.fileList.row(item))
            self.files.remove(item)

    def clearAll(self):
        self.fileList.clear()
        self.files = []
        self.ui.textBrowser.clear()

    def dragEnterEvent(self, event):
        event.accept()

    # 鼠标拖入事件
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            file = url.toLocalFile()  # ==> 获取文件路径
            if file not in self.files:  # ==> 去重显示
                item = QListWidgetItem(file)
                self.fileList.addItem(item)
                self.files.append(item)
                # 鼠标放开函数事件
                event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())