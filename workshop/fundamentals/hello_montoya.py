#!/usr/bin/env python
# coding: utf-8
import sys

def main(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
   if len(sys.argv) < 2:
       sys.exit()

   main(sys.arg)
