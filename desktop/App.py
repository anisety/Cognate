# Cognate Desktop App (PyQt6)
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cognate Desktop")
        self.setCentralWidget(QLabel("Welcome to Cognate Desktop!"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
