#!/usr/bin/python3
"""Contains script that reads stdin line by line and
computes metrics"""

import sys


def print_size_and_codes(size, codes):
    """Prints the size and codes"""
    print("File size: {}".format(size))
    for key, value in sorted(codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def parse_stdin_and_compute():
    """Parses stdin and computes metrics"""
    size = 0
    lines = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in codes:
                codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, codes)

    except KeyboardInterrupt:
        print_size_and_codes(size, codes)
        raise

    print_size_and_codes(size, codes)


parse_stdin_and_compute()
