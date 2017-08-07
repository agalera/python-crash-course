#!/usr/bin/env python
import sys

def main(*args, **kwargs):
    print("Hello World!")
    print(args)
    print(kwargs)


if __name__ == '__main__':
   if len(sys.argv) < 2:
       sys.exit()

   main(sys.arg)
