#!/usr/bin/python3
import os
os.write(os.sys.stderr.fileno(),
    bytes("and that piece of art is useful - Dora Korpar, 2015-10-19\n",
    encoding="utf-8"))
os.sys.exit(1)
