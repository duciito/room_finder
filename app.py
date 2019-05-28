import sys
import searches
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 554)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.startRoom = QtWidgets.QLineEdit(self.centralWidget)
        self.startRoom.setGeometry(QtCore.QRect(190, 50, 101, 41))
        self.startRoom.setObjectName("startRoom")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 91, 16))
        self.label.setObjectName("label")
        self.endRoom = QtWidgets.QLineEdit(self.centralWidget)
        self.endRoom.setGeometry(QtCore.QRect(190, 120, 101, 41))
        self.endRoom.setText("")
        self.endRoom.setObjectName("endRoom")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(190, 100, 91, 16))
        self.label_2.setObjectName("label_2")
        self.obstacle = QtWidgets.QLineEdit(self.centralWidget)
        self.obstacle.setGeometry(QtCore.QRect(350, 50, 101, 41))
        self.obstacle.setObjectName("obstacle")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 211, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 40, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 140, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 90, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 260, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(560, 260, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 974, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Start room"))
        self.label_2.setText(_translate("MainWindow", "End room"))
        self.label_3.setText(_translate("MainWindow", "Obstacle (obstacle search)"))
        self.pushButton.setText(_translate("MainWindow", "Obstacle search"))
        self.pushButton_2.setText(_translate("MainWindow", "Lift search"))
        self.pushButton_3.setText(_translate("MainWindow", "Shortest path search"))


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, building):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.building = building

        self.ui.pushButton.clicked.connect(self.obstacle_search)
        self.ui.pushButton_3.clicked.connect(self.obstacle_search)
        self.ui.pushButton_2.clicked.connect(self.lift_search)

    def display_search(self, median_rooms, path, cost):
        self.building.clear_visited()
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()

        if not (median_rooms or path or cost):
            self.ui.textBrowser.append("These rooms do not exist!")
            return

        for room in median_rooms:
            self.ui.textBrowser.append(f"We went through {room}")

        if path and cost:
            self.ui.textBrowser_2.append("Path found!\n")

            for room in path:
                self.ui.textBrowser_2.append(room + '\n|')

            self.ui.textBrowser_2.append(f"Total cost: {cost}")
        else:
            self.ui.textBrowser_2.append("No path found!")

    def obstacle_search(self):
        sender = self.sender()
        start_room = self.ui.startRoom.text()
        end_room = self.ui.endRoom.text()
        obstacle = '' if sender == self.ui.pushButton_3 else self.ui.obstacle.text()

        median_rooms, path, cost = searches.obstacle_search(start_room, end_room, self.building, obstacle)

        self.display_search(median_rooms, path, cost)

    def lift_search(self):
        start_room = self.ui.startRoom.text()
        end_room = self.ui.endRoom.text()

        median_rooms, path, cost = searches.lift_search(start_room, end_room, self.building)

        self.display_search(median_rooms, path, cost)
