from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure
from straight import Straight

class Tests:

    def setup_method(self):
        Straight.set_straight(1, 1, -1, -1)
        self.f = Void()

    # Точка лежит в 1-окрестности
    def test_point(self):
        self.f = self.f.add(R2Point(1, 0))
        assert isinstance(self.f, Point)

    # Вторая вершина сегмента не лежит в 1-окрестности
    def test_segment(self):
        self.f.add(R2Point(4, 0))
        assert Figure.count == 1

    # Ни одна вершина сегмента не лежит в 1-окрестности
    def test_segment2(self):
        self.f.add(R2Point(-3, 0))
        assert Figure.count == 0

    # Не изменяющая оболочку вершина не учитывается
    def test_segment3(self):
        self.f.add(R2Point(-1, 0))
        assert Figure.count == 0

    # Одна вершина многоугольника лежит в 1-окрестности
    def test_polygon(self):
        self.f.add(R2Point(0, -1))
        assert Figure.count == 1

    # Вершина, лежащая на прямой, не учитывается
    def test_polygon2(self):
        self.f.add(R2Point(-2, -2))
        assert Figure.count == 0

    # Работа с нецелыми числами
    def test_polygon3(self):
        self.f.add(R2Point(1, 2.414))
        assert Figure.count == 1

