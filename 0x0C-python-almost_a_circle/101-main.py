#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [
        Rectangle(2**i, 2**i) for i in range(1, 5)
    ]
    list_squares = [
        Square(2**i) for i in range(5, 9)
    ]
    Base.draw(list_rectangles, list_squares)
