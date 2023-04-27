#Про тесты:
#Класс создаём для удобства тестирования.
#В начале каждого класса выполняестя инициализация обекта, то есть как бы задаётся начальное состояние программы.
#Далее, в тестировачных функциях мы только временно изменяем состояние программы.
#После того как тестировачная функция заканчивает свою работу, объект и программа переходят в первоначально установленное состояние.

from r2point import R2Point
from convex import Point, Segment, Polygon
from straight import Straight

class TestsPoint:

    def setup_method(self):
        Straight.set_straight(1, 1, -1, -1)
        self.f = Point(R2Point(1, 0))

    # Точка лежит в 1-окрестности
    def test_point(self):
        assert self.f.count == 1

class TestsSegment:

    def setup_method(self):
        Straight.set_straight(1, 1, -1, -1)
        self.f = Segment(R2Point(4, 0), R2Point(1, 0))

    # Вторая вершина сегмента не лежит в 1-окрестности
    def test_segment(self):
        assert self.f.count == 1

    # Ни одна вершина сегмента не лежит в 1-окрестности
    def test_segment2(self):
        assert self.f.add(R2Point(-3, 0)).count == 0

    # Не изменяющая оболочку вершина не учитывается
    def test_segment3(self):
        assert self.f.add(R2Point(-3, 0)).add(R2Point(-1, 0)).count == 0

class TestPolygon:

    def setup_method(self):
        Straight.set_straight(1, 1, -1, -1)
        self.f = Polygon(R2Point(-3, 0), R2Point(4, 0), R2Point(0, -1))

    # Одна вершина многоугольника лежит в 1-окрестности
    def test_polygon(self):
        assert self.f.count == 1

    # Вершина, лежащая на прямой, не учитывается
    def test_polygon2(self):
        assert self.f.add(R2Point(-2, -2)).count == 0

    # Работа с нецелыми числами
    def test_polygon3(self):
        assert self.f.add(R2Point(1, 2.414)).count == 2


