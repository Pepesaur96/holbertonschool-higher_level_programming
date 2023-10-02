#!/usr/bin/python3
def magic_calculation(a, b):
    import sys
    if a < b:
        c = a + b
        for i in range(4, 6):
            try:
                c = c + i
            except:
                sys.stderr.write("Exception: {}\n".format(err))
                return c
        return c
    else:
        return a - b
