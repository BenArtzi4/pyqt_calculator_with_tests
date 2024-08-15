# gui.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from logic import CalculatorActions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 300, 300)

        # Initialize all attributes directly in __init__
        self.central_widget: QWidget = QWidget()
        self.layout: QVBoxLayout = QVBoxLayout(self.central_widget)
        self.input1: QLineEdit = QLineEdit(self)
        self.input2: QLineEdit = QLineEdit(self)
        self.result_label: QLabel = QLabel("Result: ", self)

        # Buttons for different operations
        self.add_button: QPushButton = QPushButton("Add", self)
        self.sub_button: QPushButton = QPushButton("Subtract", self)
        self.mul_button: QPushButton = QPushButton("Multiply", self)

        self.setCentralWidget(self.central_widget)

        # Set up the UI layout
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.sub_button)
        self.layout.addWidget(self.mul_button)
        self.layout.addWidget(self.result_label)

        # Connect buttons to corresponding methods
        self.add_button.clicked.connect(self.add)
        self.sub_button.clicked.connect(self.subtract)
        self.mul_button.clicked.connect(self.multiply)

    def add(self):
        self.perform_operation(CalculatorActions.add_numbers)

    def subtract(self):
        self.perform_operation(CalculatorActions.subtract_numbers)

    def multiply(self):
        self.perform_operation(CalculatorActions.multiply_numbers)

    def perform_operation(self, operation):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = operation(num1, num2)
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Invalid input!")
