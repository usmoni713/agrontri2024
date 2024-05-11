"""Модуль для управления тюльками turtle в tkinter"""

import turtle

# список доступных фигур тюльки
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']


class driver:
    """Класс для управления тюльками turtle
    
    :param shape: форма тюльки из списка shapes
    :type shape: str
    :param color: цвет тюльки, может быть строкой или кортежем с RGB
    :type color: str | tuple
    :param pensize: толщина линии, в пикселях
    :type pensize: float
    :param speed: скорость тюльки, от 0 до 10
    :type speed: int
    """
    def __init__(self, shape:str='classic', color:str|tuple='green', pensize:float=3, speed:int=-1):
        self.t = turtle.Turtle()  # создаем тюльку
        self.t.shape(shape)  # устанавливаем форму
        self.t.color(color)  # устанавливаем цвет
        self.t.pensize(pensize)  # устанавливаем толщину линии
        self.t.speed(speed)  # устанавливаем скорость

    def _forward(self, dist:float):
        """Перемещает тюльку вперед
        
        :param dist: расстояние в пикселях
        :type dist: float
        """
        self.t.forward(dist)

    def _backward(self, dist:float):
        """Перемещает тюльку назад
        
        :param dist: расстояние в пикселях
        :type dist: float
        """
        self.t.backward(dist)

    def _left(self, angle:float):
        """Поворачивает тюльку на угол
        
        :param angle: угол в градусах
        :type angle: float
        """
        self.t.left(angle)

    def _right(self, angle:float):
        """Поворачивает тюльку на угол
        
        :param angle: угол в градусах
        :type angle: float
        """
        self.t.right(angle)

    def _goto(self, x:float, y:float, paint=False):
        """Перемещает тюльку на координаты
        
        :param x: координата по оси x
        :type x: float
        :param y: координата по оси y
        :type y: float
        :param paint: рисовать ли линию при перемещении
        :type paint: bool
        """
        if not paint:
            self.t.penup()  # поднимаем перо
        self.t.goto(x, y)  # перемещаемся
        if not paint:
            self.t.pendown()  # опускаем перо

    def creat_star(self, number_sides:int, length:float=100, paint=True):
        """Рисует звезду
        
        :param number_sides: количество сторон
        :type number_sides: int
        :param length: длина сторон
        :type length: float
        :param paint: рисовать ли заливку
        :type paint: bool
        """
        if paint:
            self.t.begin_fill()  # начинаем заливку
        for i in range(number_sides):
            self._forward(length)  # двигаемся вперед
            angle = number_sides//2 * 360/number_sides  # вычисляем угол поворота
            self._left(angle)  # поворачиваемся
        if paint:
            self.t.end_fill()  # заканчиваем заливку

    def create_polygon(self, number_sides:int, length:float=100, paint=True):
        """Рисует многоугольник
        
        :param number_sides: количество сторон
        :type number_sides: int
        :param length: длина сторон
        :type length: float
        :param paint: рисовать ли заливку
        :type paint: bool
        """
        if paint:
            self.t.begin_fill()  # начинаем заливку
        for i in range(number_sides):
            self._forward(length)  # двигаемся вперед
            self._right(360/number_sides)  # поворачиваемся
        if paint:
            self.t.end_fill()  # заканчиваем заливку


t = driver('turtle', 'green', 3)
t.creat_star(5, 100)
t._goto(200, 100)
t.create_polygon(5, 100)
input()  # оставляем окно открытым

