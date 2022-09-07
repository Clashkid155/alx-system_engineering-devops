#!/usr/bin/env python3
import sys

x = [i for i in sys.stdin]
for i in x:
    if x.index(i) % 2 == 0:
        sys.stdout.write(i)

