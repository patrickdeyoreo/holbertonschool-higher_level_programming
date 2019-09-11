#!/usr/bin/python3
print(''.join([
    '' if chr(i) in 'qe' else chr(i) for i in range(ord('a'), ord('z') + 1)
]), end=None)
