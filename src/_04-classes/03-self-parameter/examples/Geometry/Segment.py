from Geometry.Point import Point


class Segment:
    def __init__(self, start=Point(0,0), end=Point(1,1)):
        self.start = start
        self.end = end

    @staticmethod
    def point_is_valid(point):
        return point.distance(Point(0, 0)) > 1

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        if point_is_valid(value):
            self.__start = value
        else:
            self.__start = Point(0, 0)

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        if point_is_valid(value):
            self.__end = value
        else:
            self.__end = Point(0, 0)