class Room:
    """Клас, описващ стаята в сградата."""

    def __init__(self, name, x, y, floor_num, room_type):
        self.name = name
        self.x = x
        self.y = y
        self.floor_num = floor_num
        self.room_type = room_type
        self.connections = []
        self.visited = False
