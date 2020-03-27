# -*- coding: UTF-8 -*-

"""
Board-relate things
"""
import random


class Board(object):
    """
    A 2048 board
    """
    UP, DOWN, LEFT, RIGHT, PAUSE = 1, 2, 3, 4, 5

    GOAL = 2048
    SIZE = 4

    def __init__(self, goal=GOAL, size=SIZE, **_kwargs):
        self.__size = size
        self.__size_range = range(0, self.__size)
        self.__goal = goal
        self.__won = False
        self.cells = [[0] * self.__size for _ in range(self.__size)]
        self.addTile()
        self.addTile()

    def addTile(self, value=None, choices=None):
        """
        add a random tile in an empty cell
        :param value: value of the tile to add
        :param choices: a list of possible choices for the value of the tile. if
                        ``None`` (the default), it uses
                        ``[2, 2, 2, 2, 2, 2, 2, 2, 2, 4]``
        """
        if choices is None:
            choices = [2] * 9 + [4]

        if value:
            choices = [value]

        v = random.choice(choices)
        empty = self.getEmptyCells()
        if empty:
            x, y = random.choice(empty)
            self.setCell(x, y, v)

    def size(self):
        """return board size"""
        return self.__size

    def goal(self):
        """return the board goal"""
        return self.__goal

    def won(self):
        """return True if the board contains a least one tile with the board goal"""
        return self.__won

    def canMove(self):
        """
        test if a move is possible
        """
        if not self.filled:
            return True

        for y in self.__size_range:
            for x in self.__size_range:
                c = self.getCell(x, y)
                if (x < self.__size - 1 and c == self.getCell(x + 1, y)
                        or (y < self.__size - 1 and c == self.getCell(x, y + 1))):
                    return True

        return False

    def filled(self):
        """
        return true if the game is filled
        """
        return len(self.getEmptyCells()) == 0

    def getCell(self, x, y):
        """return the cell value at x, y"""
        return self.cells[y][x]

    def setCell(self, x, y, v):
        """set the cell value at x, y"""
        self.cells[y][x] = v

    def getEmptyCells(self):
        """return a (x, y) pair for each empty cell"""
        return [(x, y)
                for x in self.__size_range
                for y in self.__size_range if self.getCell(x, y) == 0]

    def getLIne(self, y):
        """return the y-th line, starting at 0"""
        return self.cells[y]

    def setLine(self, y, l):
        """set the y-th line, starting at 0"""
        self.cells[y] = l[:]

    def getCol(self, x):
        """return the x-th line, starting at 0"""
        return self.cells[x]

    def setCol(self, x, l):
        """set the x-th line, starting at 0"""
        self.cells[x] = l[:]

    def __collapseLineCol(self, line, d):
        """
        Merge tiles in a line column according to a direction and return a
        tuple with the new line and the score for the move on this line
        """
        if (d == Board.UP or d == Board.LEFT):
            inc = 1
            rg = range(0, self.__size - 1, inc)
        else:
            inc = -1
            rg = range(self.__size - 1, 0, inc)

        pts = 0
        for i in rg:
            if line[i] == 0:
                continue
            if line[i] == line[i + inc]:
                v = line[i] * 2
                if v == self.__goal:
                    self.__won = True

                line[i] = v
                line[i + inc] = 0
                pts += v

        return line(line, pts)

    

