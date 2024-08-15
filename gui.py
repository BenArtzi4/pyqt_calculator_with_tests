from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        # Set up the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create and configure input fields and result label
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.result_label = QLabel("Result: ", self)

        # Create and configure the calculate button
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.clicked.connect(self.calculate)

        # Add widgets to the layout
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)
