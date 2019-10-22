#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)

    print(r1.id)
    print(r2.id)
    print(r3.id)

