from abc import ABC, abstractmethod

class Game:
    def __init__(self):
        self.maze = None # Creates a maze

    def make2RoomsMaze(self):
        self.maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.add_room(room1)
        self.maze.add_room(room2)

        door = Door(room1, room2)
        room1.south = door
        room2.north = door
        return self.maze
    
    def make2RoomsMazeFM(self):
        self.maze = self.make_maze()
        room1 = self.make_room(1)
        room2 = self.make_room(2)
        self.maze.add_room(room1)
        self.maze.add_room(room2)
        door = self.make_door(room1, room2)
        room1.south = door
        room2.north = door
        self.maze.connect_rooms(room1, room2, door)
        return self.maze

    def make_wall(self):
        return Wall()
    
    def make_door(self, room1, room2):
        return Door(room1, room2)
    
    def make_room(self, id):
        room = Room(id)
        room.north = self.make_wall()
        room.south = self.make_wall()
        room.east = self.make_wall()
        room.west = self.make_wall()
        return room
    
    def make_maze(self):
        return Maze()

class BombedGame(Game):
    def make_wall(self):
        return BombedWall()


# Creator
class MapElement(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
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
        self.north = None
        self.south = None
        self.east = None
        self.west = None
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

class BombedWall(Wall):
    def __init__(self):
        self.active = False
    def entrar(self):
        if self.active:
            print("You are dead")
        else:
            return super().entrar()

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

class Enemy:
    def __init__(self):
        self.lives = None
        self.power = None
        self.mode = None
        self.position = None

    def isAlive(self):
        return self.lives > 0
    
    def getMode(self):
        return self.mode
    
    def setMode(self, mode):
        self.mode = mode

    def getPower(self):
        return self.power
    
    def setPower(self, power):
        self.power = power

    def getLives(self):
        return self.lives
    
    def setLives(self, lives):
        self.lives = lives

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position





game = Game()
game.make2RoomsMazeFM()
game.maze.entrar()
game.maze.rooms[0].north.entrar()
game.maze.doors[0].entrar()
game.maze.rooms[0].opened = True
game.maze.doors[0].entrar()

