#!/usr/bin/python3
print(*("{} = {:#x}".format(i, i) for i in range(100)), sep='\n')
