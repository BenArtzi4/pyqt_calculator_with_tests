# gui.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from logic import CalculatorActions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")

        self.central_widget: QWidget = QWidget()
        self.layout: QVBoxLayout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(20)

        # Set up input fields
        self.input1: QLineEdit = QLineEdit(self)
        self.input1.setPlaceholderText("Enter first number")
        self.input1.setFont(QFont("Gisha", 14))
        self.input1.setStyleSheet("padding: 10px; border-radius: 5px; border: 2px solid #16a085;")

        self.input2: QLineEdit = QLineEdit(self)
        self.input2.setPlaceholderText("Enter second number")
        self.input2.setFont(QFont("Gisha", 14))
        self.input2.setStyleSheet("padding: 10px; border-radius: 5px; border: 2px solid #16a085;")

        # Set up the result label
        self.result_label: QLabel = QLabel("Result: ", self)
        self.result_label.setFont(QFont("Gisha", 16))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("padding: 10px; border-radius: 5px; background-color: #34495e;")

        # Buttons for different operations
        self.add_button: QPushButton = QPushButton("Add", self)
        self.sub_button: QPushButton = QPushButton("Subtract", self)
        self.mul_button: QPushButton = QPushButton("Multiply", self)

        button_style = (
            "padding: 10px; border-radius: 5px; border: none; background-color: #16a085;"
            "color: #ecf0f1; font-size: 18px;"
        )
        self.add_button.setStyleSheet(button_style)
        self.sub_button.setStyleSheet(button_style)
        self.mul_button.setStyleSheet(button_style)

        self.setCentralWidget(self.central_widget)

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
