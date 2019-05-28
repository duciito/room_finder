import sys
import searches
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    """Main UI window made using Qt5."""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 554)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.startRoom = QtWidgets.QLineEdit(self.centralWidget)
        self.startRoom.setGeometry(QtCore.QRect(190, 50, 101, 41))
        self.startRoom.setObjectName("startRoom")
        self.startRoom_label = QtWidgets.QLabel(self.centralWidget)
        self.startRoom_label.setGeometry(QtCore.QRect(190, 30, 91, 16))
        self.startRoom_label.setObjectName("startRoom_label")
        self.endRoom = QtWidgets.QLineEdit(self.centralWidget)
        self.endRoom.setGeometry(QtCore.QRect(190, 120, 101, 41))
        self.endRoom.setText("")
        self.endRoom.setObjectName("endRoom")
        self.endRoom_label = QtWidgets.QLabel(self.centralWidget)
        self.endRoom_label.setGeometry(QtCore.QRect(190, 100, 91, 16))
        self.endRoom_label.setObjectName("endRoom_label")
        self.obstacle = QtWidgets.QLineEdit(self.centralWidget)
        self.obstacle.setGeometry(QtCore.QRect(350, 50, 101, 41))
        self.obstacle.setObjectName("obstacle")
        self.obstacle_label = QtWidgets.QLabel(self.centralWidget)
        self.obstacle_label.setGeometry(QtCore.QRect(350, 30, 211, 16))
        self.obstacle_label.setObjectName("obstacle_label")
        self.obstacle_button = QtWidgets.QPushButton(self.centralWidget)
        self.obstacle_button.setGeometry(QtCore.QRect(640, 40, 141, 31))
        self.obstacle_button.setObjectName("obstacle_button")
        self.lift_button = QtWidgets.QPushButton(self.centralWidget)
        self.lift_button.setGeometry(QtCore.QRect(640, 140, 141, 31))
        self.lift_button.setObjectName("lift_button")
        self.shortest_button = QtWidgets.QPushButton(self.centralWidget)
        self.shortest_button.setGeometry(QtCore.QRect(640, 90, 141, 31))
        self.shortest_button.setObjectName("shortest_button")
        self.intermediate_data = QtWidgets.QTextBrowser(self.centralWidget)
        self.intermediate_data.setGeometry(QtCore.QRect(160, 260, 256, 192))
        self.intermediate_data.setObjectName("intermediate_data")
        self.path_data = QtWidgets.QTextBrowser(self.centralWidget)
        self.path_data.setGeometry(QtCore.QRect(560, 260, 256, 192))
        self.path_data.setObjectName("path_data")
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
        self.startRoom_label.setText(_translate("MainWindow", "Start room"))
        self.endRoom_label.setText(_translate("MainWindow", "End room"))
        self.obstacle_label.setText(_translate("MainWindow", "Obstacle (obstacle search)"))
        self.obstacle_button.setText(_translate("MainWindow", "Obstacle search"))
        self.lift_button.setText(_translate("MainWindow", "Lift search"))
        self.shortest_button.setText(_translate("MainWindow", "Shortest path search"))


class ApplicationWindow(QtWidgets.QMainWindow):
    """Use MainWindow to create the dialog and connect listeners to the buttons."""

    def __init__(self, building):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.building = building

        self.ui.obstacle_button.clicked.connect(self.obstacle_search)
        self.ui.shortest_button.clicked.connect(self.obstacle_search)
        self.ui.lift_button.clicked.connect(self.lift_search)

    def display_search(self, median_rooms, path, cost):
        self.building.clear_visited()
        self.ui.intermediate_data.clear()
        self.ui.path_data.clear()

        if not (median_rooms or path or cost):
            self.ui.intermediate_data.append("These rooms do not exist!")
            return

        for room in median_rooms:
            self.ui.intermediate_data.append(f"We went through {room}")

        if path and cost:
            self.ui.path_data.append("Path found!\n")

            for room in path:
                self.ui.path_data.append(room + '\n|')

            self.ui.path_data.append(f"Total cost: {cost}")
        else:
            self.ui.path_data.append("No path found!")

    def obstacle_search(self):
        sender = self.sender()
        start_room = self.ui.startRoom.text()
        end_room = self.ui.endRoom.text()
        obstacle = '' if sender == self.ui.shortest_button else self.ui.obstacle.text()

        median_rooms, path, cost = searches.obstacle_search(start_room, end_room, self.building, obstacle)

        self.display_search(median_rooms, path, cost)

    def lift_search(self):
        start_room = self.ui.startRoom.text()
        end_room = self.ui.endRoom.text()

        median_rooms, path, cost = searches.lift_search(start_room, end_room, self.building)

        self.display_search(median_rooms, path, cost)
