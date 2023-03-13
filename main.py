import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from interface import Ui_MainWindow
from PySide6.QtCore import QEvent, Qt




class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # btn connects
        self.ui.btn_start.clicked.connect(self.is_triangle)

        # install event filter on line edit
        self.ui.le_main.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.ui.le_main and event.type() == QEvent.KeyPress:
            self.ui.success.setMaximumHeight(0)
            self.ui.error.setMaximumHeight(0)

            if event.text().isdigit() or event.key() == Qt.Key_Backspace or event.text() == " ":
                return False
            else:
                return True
        return False

    def is_triangle(self):
        value = self.ui.le_main.text().split(" ")
        side1 = int(value[0])
        side2 = int(value[1])
        side3 = int(value[2])


        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            self.ui.error.setMaximumHeight(150)
        else:
            self.ui.success.setMaximumHeight(150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
