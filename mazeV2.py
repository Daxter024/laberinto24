class Game:
    def __init__(self):
        self.maze = None # Creates a maze


class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Maze(MapElement):
    def __init__(self):
        self.rooms = []
        self.doors = []
    def add_room(self, room):
        self.rooms.append(room)
    def entrar(self):
        self.rooms[0].entrar()
    def connect_rooms(self, room1, room2, door):
        self.doors.append(door)
        room1.connect(door)
        room2.connect(door)

class Room(MapElement):
    def __init__(self, id):
        self.id = id
        self.north = Wall()
        self.south = Wall()
        self.east = Wall()
        self.west = Wall()
        self.doors = []
    def connect(self, door):
        self.doors.append(door)
    def entrar(self):
        print("You enter room ",self.id)

class Wall(MapElement):
    def __init__(self):
        pass
    def entrar(self):
        print("You can't go through walls")

class Door(MapElement):
    def __init__(self, room1, room2):
        #self.rooms = [room1, room2]
        self.room1 = room1
        self.room2 = room2
        self.opened = False
    def entrar(self):
        if self.opened:
            self.room2.entrar()
        else:
            #self.opened = True
            print("The door is closed")