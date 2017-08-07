#!/usr/bin/env python
import sys


def main(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    main(sys.args)
