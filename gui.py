# gui.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from logic import CalculatorActions  # Import the new class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.result_label = QLabel("Result: ", self)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.clicked.connect(self.calculate)

        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = CalculatorActions.add_numbers(num1, num2)  # Use the new class
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Invalid input!")
