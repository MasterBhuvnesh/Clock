import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

current_directory =os.getcwd()
# print("Current Directory:",current_directory)
path=current_directory.replace( "\\", "/")
# print("new",path)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("clock")
        self.setFixedSize(800,600)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f"{path}/index.html"))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon('icon.png'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
