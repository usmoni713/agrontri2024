import turtle

shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
class driver:
    def __init__(self, shape:str='classic', color:str|tuple='green', pensize:float=3, speed:int=-1):
        self.t = turtle.Turtle()
        self.t.shape(shape)
        self.t.color(color)
        self.t.pensize(pensize)
        self.t.speed(speed)
    def _forward(self, dist:float):
        self.t.forward(dist)
    def _backward(self, dist:float):
        self.t.backward(dist)
    def _left(self, angle:float):
        self.t.left(angle)
    def _right(self, angle:float):
        self.t.right(angle)
    def _goto(self, x:float, y:float, paint=False):
        if not paint:
            self.t.penup()
        self.t.goto(x, y)
        if not paint:
            self.t.pendown()
    def creat_star(self, number_sides:int, length:float=100, paint=True):
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            angle = number_sides//2 * 360/number_sides
            print(f'{(number_sides/2)=}')
            print(f'{(number_sides//2)=}')
            self._left(angle)
        if paint:
            self.t.end_fill()
    def create_polygon(self, number_sides:int, length:float=100, paint=True):
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            self._right(360/number_sides)
        if paint:
            self.t.end_fill()


t = driver('turtle', 'green', 3)
t.creat_star(5, 100)
t._goto(200, 100)
t.create_polygon(5, 100)
input()

