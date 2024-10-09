#!/usr/bin/env python3

from __future__ import print_function
from random import choice
import argparse


def generate_password(lowercase=False, include_symbols=False, length=16):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if lowercase:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if include_symbols:
        chars += '=+'

    return ''.join(choice(chars) for _ in range(length))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, action='store', default=16)
    parser.add_argument('-n', action='store_true')
    parser.add_argument('--count', type=int, action='store', default=1)
    parser.add_argument('--include-symbols', action='store_true')
    parser.add_argument('--lower', action='store_true')

    args = parser.parse_args()

    for i in range(args.count):
        password = generate_password(lowercase=args.lower,
                                     include_symbols=args.include_symbols,
                                     length=args.length)
        if args.n:
            print(password, end='')
        else:
            print(password)
