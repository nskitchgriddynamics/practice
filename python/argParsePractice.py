#!/usr/bin/python

__author__ = 'Nick'

import argparse
import os


parser = argparse.ArgumentParser(description='parsing some stuff')
parser.add_argument("-a", "--add",nargs="+", help='add users')
parser.add_argument("-d", "--delete",nargs="+", help='delete users')
args = parser.parse_args()

if args.add:
    for u in args.add:
        print('adding user ' + u)
        os.system('useradd -m -p "test1234" ' + u)

elif args.delete:
    for u in args.delete:
        print('deleting user '+u)
        os.system('userdel '+ u)