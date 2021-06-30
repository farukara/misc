import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButto:

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("This is My first Qt Application window")
window.setGeometry(100, 100, 280, 380)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello World!!</h1>", parent=window)
helloMsg.move(60, 15)

layout = QHBoxLayout()
layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))
layout.addWidget(QPushButton("Button 3"))
layout.addWidget(QPushButton("Button 3"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
