#!/usr/bin/env python

from http.server import test

if __name__ == '__main__':
    try:
        print("welcome")
        test()
    except KeyboardInterrupt:
        print('exiting server...x')

