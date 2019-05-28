import app
import sys
from PyQt5 import QtWidgets
from building import Building
from room import Room
from connection import Connection


def import_rooms(filename, building):
    """Импортиране на стаите от файл."""

    with open(filename) as rooms_file:

        for line in rooms_file:

            params = line.replace(' ', '').replace(';', '').rstrip().split(',')

            if 'yes' in params or 'no' in params:
                connection = Connection(params[1], params[2], params[3], True if params[4] == 'yes' else False)
                building.add_connection(params[0], connection)
            else:
                room = Room(params[0], params[1], params[2], params[3], params[4])
                building.add_room(room)


if __name__ == '__main__':
    building = Building()
    import_rooms('dexter+lab.txt', building)

    window_app = QtWidgets.QApplication(sys.argv)
    application = app.ApplicationWindow(building)
    application.show()
    sys.exit(window_app.exec_())
