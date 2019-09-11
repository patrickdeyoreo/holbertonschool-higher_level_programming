#!/usr/bin/python3
print(", ".join([", ".join([
    str(tens)+str(ones) for ones in range(tens + 1, 10)]) for tens in range(9)
]))
