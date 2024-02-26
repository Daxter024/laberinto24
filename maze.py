class Game:
    def __init__(self):
        self.maze = None

    def make2RoomsMaze(self):
        self.maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.add_room(room1)
        self.maze.add_room(room2)

        door=Door(room1,room2)
        room1.south = door
        room2.north = door
        return self.maze

    def make2RoomsMazeFM(self):
        self.maze = self.make_maze()
        room1 = self.make_room(1)
        room2 = self.make_room(2)
        self.maze.add_room(room1)
        self.maze.add_room(room2)

        door=self.make_door(room1,room2)
        room1.south = door
        room2.north = door
        self.maze.connect_rooms(room1,room2,door)
        return self.maze
    
    def make_wall(self):
        return Wall()
    
    def make_door(self, room1, room2):
        return Door(room1, room2)
    
    def make_room(self, id):
        return Room(id)
    
    def make_maze(self):
        return Maze()
    
class BombedGame(Game):
    def make_wall(self):
        return BombedWall()

class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Hoja(MapElement):
    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorator(Hoja):
    def __init__(self, component):
        self.component = component

# clase hoja  subclase de MapElement y clase contenedor  subclase de MapElement
class Contenedor(MapElement):
    def __init__ (self):
        self.hijos=[]

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
    
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

class Maze(Contenedor):
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

class Room(Contenedor):
    def __init__(self, id):
        self.id = id
        self.north = Wall()
        # esto se podria hacer inicializando a None y luego en el make_room que haga self.north = self.make_wall()
        self.south = Wall()
        self.east = Wall()
        self.west = Wall()
        self.doors = []
        
    def connect(self, door):
        self.doors.append(door)

    def entrar(self):
        print("You enter room ",self.id)
        
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


class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need any special attributes

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
    

# game=Game()
# game.make2RoomsMazeFM()
# game.maze.entrar()
# game.maze.doors[0].entrar()
        
game = Game()
game.make2RoomsMaze()
game.maze.entrar()

game = Game()
game.make2RoomsMazeFM()
import unittest

class TestMaze(unittest.TestCase):

    def test_move(self):
        # Set up maze and player
        maze = Maze() 
        player = Player()
        
        # Test moving player
        player.move("right")
        self.assertEqual(player.x, 1)
        self.assertEqual(player.y, 0)
        
        player.move("down")
        self.assertEqual(player.x, 1)
        self.assertEqual(player.y, 1)
        
        player.move("left")
        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 1)
        
        player.move("up")
        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 0)
        
if __name__ == '__main__':
    unittest.main()

    #FM, decoractor, strategy y composite design patterns the project must have


game2=BombedGame()
game2.make2RoomsMazeFM()
game2.maze.entrar()




