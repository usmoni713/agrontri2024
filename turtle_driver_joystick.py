import turtle

shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
window = turtle.Screen()
window.bgcolor("#0f67a2")


class driver:
    def __init__(
        self,
        shape: str = "classic",
        color: str | tuple = "green",
        pensize: float = 3,
        speed: int = -1,
    ):
        self.t = turtle.Turtle()
        self.t.shape(shape)
        self.t.color(color)
        self.t.pensize(pensize)
        self.t.speed(speed)

    def _forward(self, dist: float=5):
        self.t.forward(dist)

    def _backward(self, dist: float=5):
        self.t.backward(dist)

    def _left(self, angle: float=5):
        self.t.left(angle)

    def _right(self, angle: float=5):
        self.t.right(angle)

    def _goto(self, x: float, y: float, paint=False):
        if not paint:
            self.t.penup()
        self.t.goto(x, y)
        if not paint:
            self.t.pendown()

    def creat_star(self, number_sides: int=5, length: float = 100, paint=True):
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            angle = number_sides // 2 * 360 / number_sides
            self._left(angle)
        if paint:
            self.t.end_fill()

    def create_polygon(self, number_sides: int, length: float = 100, paint=True):
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            self._right(360 / number_sides)
        if paint:
            self.t.end_fill()



class joystick:
    instance = None
    def __init__(self, instance: driver|None):
        self.instance = instance
    def _regester_keys_for_new_function(self,function, key = 'space', ):
        window.onkeypress(function, key)
    def regester_keys_for_moving_through_space(self, key_forward = 'w', key_backward = 's', key_left = 'a', key_right = 'd'):
        self._regester_keys_for_new_function(function=self.instance._forward, key=key_forward)
        self._regester_keys_for_new_function(function=self.instance._backward, key=key_backward)
        self._regester_keys_for_new_function(function=self.instance._left, key=key_left)
        self._regester_keys_for_new_function(function=self.instance._right, key=key_right)
    def _listen(self):
        window.listen()


t = driver("turtle", "green", 3)
t.creat_star(5, 100)
t._goto(200, 100)
t.create_polygon(3, 100)

t_joystick = joystick(t)
t_joystick.regester_keys_for_moving_through_space()
t_joystick._regester_keys_for_new_function(t.creat_star, key='p')
t_joystick._listen()
window = turtle.Screen()
window.mainloop()