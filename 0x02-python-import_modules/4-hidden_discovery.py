#!/usr/bin/python3

import os


if __name__ == "__main__":

    fd = os.open("hidden_4.pyc", os.O_RDONLY)
    status = 1
    hidden = b''
    while status:
        status = os.read(fd, 42)
        if (status):
            hidden += status
    os.close(fd)

    names = []
    for line in hidden.split(b'\xda'):
        if (line.startswith(b'\x0c') or
                line.startswith(b'\x0f') or
                line.startswith(b'\x01')):
            names.append(line[1:])

    for i, name in enumerate(names):
        end = 0
        while (ord('A') <= name[end] <= ord('Z') or
               ord('a') <= name[end] <= ord('z') or
               ord('0') <= name[end] <= ord('9') or
               name[end] == ord('_')):
            end += 1
        names[i] = name[:end]

    names.sort()
    for name in names:
        if name[:2] != b'__':
            print(name.decode())
