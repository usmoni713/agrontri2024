import turtle

shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
window = turtle.Screen()
window.bgcolor("#0f67a2")


class driver:
    """Класс для управления тюльками turtle"""

    def __init__(
        self,
        shape: str = "classic",
        color: str | tuple = "green",
        pensize: float = 3,
        speed: int = -1,
    ):
        """Инициализирует тюльку

        :param shape: форма тюльки из списка shapes
        :param color: цвет тюльки, может быть строкой или кортежем с RGB
        :param pensize: толщина линии, в пикселях
        :param speed: скорость тюльки, от 0 до 10
        """
        self.t = turtle.Turtle()
        self.t.shape(shape)
        self.t.color(color)
        self.t.pensize(pensize)
        self.t.speed(speed)

    def _forward(self, dist: float = 5):
        """Перемещает тюльку вперед

        :param dist: расстояние в пикселях
        """
        self.t.forward(dist)

    def _backward(self, dist: float = 5):
        """Перемещает тюльку назад

        :param dist: расстояние в пикселях
        """
        self.t.backward(dist)

    def _left(self, angle: float = 5):
        """Поворачивает тюльку на угол

        :param angle: угол в градусах
        """
        self.t.left(angle)

    def _right(self, angle: float = 5):
        """Поворачивает тюльку на угол

        :param angle: угол в градусах
        """
        self.t.right(angle)

    def _goto(self, x: float, y: float, paint=False):
        """Перемещает тюльку на координаты

        :param x: координата по оси x
        :param y: координата по оси y
        :param paint: рисовать ли линию при перемещении
        """
        if not paint:
            self.t.penup()
        self.t.goto(x, y)
        if not paint:
            self.t.pendown()

    def creat_star(self, number_sides: int = 5, length: float = 100, paint=True):
        """Рисует звезду

        :param number_sides: количество сторон
        :param length: длина сторон
        :param paint: рисовать ли заливку
        """
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            angle = number_sides // 2 * 360 / number_sides
            self._left(angle)
        if paint:
            self.t.end_fill()

    def create_polygon(self, number_sides: int, length: float = 100, paint=True):
        """Рисует многоугольник

        :param number_sides: количество сторон
        :param length: длина сторон
        :param paint: рисовать ли заливку
        """
        if paint:
            self.t.begin_fill()
        for i in range(number_sides):
            self._forward(length)
            self._right(360 / number_sides)
        if paint:
            self.t.end_fill()


class joystick:
    """Класс для управления тюлькой с помощью клавиатуры"""

    instance = None

    def __init__(self, instance: driver | None):
        """Инициализирует класс

        :param instance: объект класса driver, который нужно управлять
        """
        self.instance = instance

    def _regester_keys_for_new_function(
        self,
        function,
        key="space",
    ):
        """Регистрирует новую функцию для нажатия клавиши

        :param function: функция, которую нужно зарегистрировать
        :param key: символ клавиши
        """
        window.onkeypress(function, key)

    def regester_keys_for_moving_through_space(
        self, key_forward="w", key_backward="s", key_left="a", key_right="d"
    ):
        """Регистрирует клавиши для перемещения тюльки в пространстве

        :param key_forward: клавиша для перемещения вперед
        :param key_backward: клавиша для перемещения назад
        :param key_left: клавиша для поворота налево
        :param key_right: клавиша для поворота направо
        """
        self._regester_keys_for_new_function(
            function=self.instance._forward, key=key_forward
        )
        self._regester_keys_for_new_function(
            function=self.instance._backward, key=key_backward
        )
        self._regester_keys_for_new_function(function=self.instance._left, key=key_left)
        self._regester_keys_for_new_function(
            function=self.instance._right, key=key_right
        )

    def _listen(self):
        """Начинает прослушивать клавиатуру"""
        window.listen()


t1 = driver("turtle", "green", 3)
t1.creat_star(5, 100)
t1._goto(200, 100)
t1.create_polygon(3, 100)

t1_joystick = joystick(t1)
t1_joystick.regester_keys_for_moving_through_space()
t1_joystick._regester_keys_for_new_function(t1.creat_star, key="p")
t1_joystick._listen()
t2 = driver("turtle", "red", 3)
t2.creat_star(3, 150)
t2._goto(100, 200)
t2.create_polygon(3, 100)

t2_joystick = joystick(t2)
t2_joystick.regester_keys_for_moving_through_space(
    key_forward="Up", key_backward="Down", key_left="Left", key_right="Right"
)
t2_joystick._regester_keys_for_new_function(t2.creat_star, key="o")
t2_joystick._listen()
window = turtle.Screen()
window.mainloop()

