#!/usr/bin/python3
print("\n".join(
    map(lambda n: '{0} = {0:#x}'.format(n), range(99))
))
