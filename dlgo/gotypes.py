import enum
from collections import namedtuple


class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]


if __name__ == '__main__':
    print(type(range(1,5)))

    # player1 = Player(value=Player.black)
    # print(type(player1.other))
    # point1 = Point(2,4)
    # print(point1.neighbors())
    name = 'Ivan'
    for i in range(1,5):
        print(i)


