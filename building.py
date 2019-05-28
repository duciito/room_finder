import copy


class Building:
    """Клас, описващ сградата, съдържаща стаите и връзките помежду им."""

    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """Добавяне на нова стая към сградата."""

        if not room or room.name in self.rooms:
            print("Вече има такава!")
            return

        self.rooms[room.name] = room

    def add_connection(self, room_name, connection):
        """Добавяне на връзка м/у две стаи."""

        if room_name in self.rooms and connection.to in self.rooms:
            self.rooms[room_name].connections.append(connection)

            if connection.bidirectional:
                opposite_conn = copy.deepcopy(connection)
                opposite_conn.to = room_name
                self.rooms[connection.to].connections.append(opposite_conn)

    def get_room(self, name):
        """Връщане на стая."""

        return self.rooms[name]

    def contains_room(self, name):
        """Проверяване за съществуваща стая."""

        return name in self.rooms

    def clear_visited(self):
        """Изчистване на проверени стаи от търсенията."""

        for name in self.rooms.keys():
            self.rooms[name].visited = False
