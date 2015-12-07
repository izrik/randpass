#!/usr/bin/env python

from __future__ import print_function
from random import choice
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, action='store', default=8)
parser.add_argument('-n', action='store_true')
parser.add_argument('--count', type=int, action='store', default=1)

args = parser.parse_args()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+'

for i in xrange(args.count):
    password = ''.join(choice(chars) for _ in xrange(args.length))

    if args.n:
        print(password, end='')
    else:
        print(password)

