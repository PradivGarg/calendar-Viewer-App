import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout
from PyQt5 import QtCore as core
import calendar

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #set the title of the window
        self.setWindowTitle("Calendar Viewer")
        self.setGeometry(100, 100, 650, 850)

        self.setStyleSheet("background-color: lightgray;")

        #create a central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #create the layout for the main window
        self.layout = QGridLayout(self.centralWidget)

        #create title label
        self.titleLabel = QLabel("Calendar")
        self.titleLabel.setStyleSheet("font: bold 28px 'Times'; background-color: lightgray; text-align: center; border: 2px solid lightgray;")
        self.titleLabel.setAlignment(core.Qt.AlignCenter)
        self.layout.addWidget(self.titleLabel, 0, 0, 1, 2)

        #create labe for input of year
        self.yearLabel = QLabel("Enter Year:")
        self.yearLabel.setStyleSheet("font: 20px 'Times'; background-color: lightgray;")
        self.layout.addWidget(self.yearLabel, 1, 0)

        self.yearInput = QLineEdit()
        self.layout.addWidget(self.yearInput, 1, 1)
        self.yearInput.setPlaceholderText("Enter Year (e.g. 2023)")
        self.yearInput.setStyleSheet("font: 20px 'Times'; background-color: lightgray;")

        #Create buttons
        self.showButton = QPushButton("Show Calendar")
        self.showButton.setStyleSheet("font: 20px 'Times'; background-color: lightgray; color:black")
        self.showButton.clicked.connect(self.show_calendar)
        self.layout.addWidget(self.showButton, 2, 1)


        self.exitButton = QPushButton("Exit")
        self.exitButton.setStyleSheet("font: 20px 'Times'; background-color: lightgray; color:black")
        self.exitButton.clicked.connect(self.close) 
        self.layout.addWidget(self.exitButton, 2, 0)

        #Create text area to display the calendar
        self.displayCalendar = QTextEdit()
        self.displayCalendar.setReadOnly(True)
        self.layout.addWidget(self.displayCalendar, 3, 0, 1, 2)
        

        self.setLayout(self.layout)

    def show_calendar(self):
        #get the year from the input field
        year = int(self.yearInput.text())
        #generate the calendar for the year
        calContent = calendar.calendar(year)
        #display the calendar in the text area
        self.displayCalendar.setText(calContent)
        #set the font and color of the text area
        self.displayCalendar.setStyleSheet("font: 14px 'Courier New'; color: black; background-color: lightgray;")

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())


