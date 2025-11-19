from sys import argv

from PyQt6.QtWidgets import QApplication, QMainWindow

from project.untitled import Ui_MainWindow


class Interactor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   # ← اینجا مشکل بود
        self.show()

def _run():
    app: QApplication = QApplication(argv)
    window = Interactor()
    app.exec()
    exit()

if __name__ == "__main__":
    _run()
