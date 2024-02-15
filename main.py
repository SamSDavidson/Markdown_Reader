import sys
from PyQt6 import *
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QVBoxLayout,
    # TODO: QTabWidget,
    QMenuBar,
    QFileDialog,
    QTextEdit,
)
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Markdown Test")

        layout_main = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(layout_main)
        self.setCentralWidget(central_widget)

        ## Append markdown to text browser
        self.text_box = QTextEdit()
        self.text_box.setMarkdown
        self.text_box.setReadOnly(False)

        menu = QMenuBar(central_widget)
        file_select = menu.addAction("Open")
        file_select.triggered.connect(self.load_page)
        save_action = menu.addAction("Save")
        save_action.triggered.connect(self.save_edit)

        layout_main.addWidget(menu)
        layout_main.addWidget(self.text_box)

        web_view = QWebEngineView()
        test_url = "https://youtu.be/teet7SEwRdE"
        file_test_url = "file://///home/sam/Code/Python/mdReader/pages/index.html"
        web_view.setUrl(QUrl(file_test_url))

        layout_main.addWidget(web_view)

    def load_page(self):
        file_path, _ = QFileDialog.getOpenFileName()
        with open(file_path, "r") as fp:
            self.text_box.setMarkdown(fp.read())

    def save_edit(self):
        file_path, _ = QFileDialog.getSaveFileName()
        with open(file_path, "w") as fp:
            fp.write(self.text_box.toHtml())
        self.load_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1080, 720)
    apply_stylesheet(app, "dark_cyan.xml")
    window.show()
    sys.exit(app.exec())
