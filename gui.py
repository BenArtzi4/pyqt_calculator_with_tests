# gui.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from logic import CalculatorActions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 200)

        # Initialize all attributes directly in __init__
        self.central_widget: QWidget = QWidget()
        self.layout: QVBoxLayout = QVBoxLayout(self.central_widget)
        self.input1: QLineEdit = QLineEdit(self)
        self.input2: QLineEdit = QLineEdit(self)
        self.calculate_button: QPushButton = QPushButton("Calculate", self)
        self.result_label: QLabel = QLabel("Result: ", self)

        self.setCentralWidget(self.central_widget)

        # Set up the UI layout
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        # Connect the button click to the calculate method
        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = CalculatorActions.add_numbers(num1, num2)
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Invalid input!")
