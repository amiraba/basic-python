# https://www.youtube.com/watch?v=cybMiQYuEwc&list=PLH1n1sJO7tbxmE36txTPhgidmW5Z9Bn7m&index=1

import time
import datetime

print(time.time())
print (datetime.datetime.fromtimestamp(time.time()))

def my_func():
    print (datetime.datetime.now())
    print('month = ', datetime.datetime.now().strftime("%m"))
    print(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

my_func()

from datetime import date
date1 = date(2019, 1, 1)
date2 = date(2022, 1, 1)
print(date1)
print(date2 - date1)

import getpass
print (getpass.getuser())

import os
print (os.environ)
print (os.environ['PATH'])

import cProfile
cProfile.run('my_func()')

#Difference between using ' and "? https://stackoverflow.com/questions/5087425/difference-between-using-and
#" is useful when you have ' into the string and vice versa
# """ on
# multiple
# lines """

from os import listdir
files_list = listdir('/usr')
files_list_same = [f for f in listdir('/usr')]
print (files_list, '\r\n', files_list_same)

from os.path import isfile, join
files_list_only_files = [f for f in listdir('/Users') if isfile(join('/Users', f))]
print (files_list_only_files)

import sys
print(sys.version)
print(sys.version_info)

from math import pi
r=1
#r = float(input("insert the cercle's radius here: "))
print(round(pi * r**2, 2))

values=("1,2,3")
list=values.split(',')
tuple=tuple(list)
print("list: ", list)
print("tuple: ", tuple)
# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.

print("%s and %s." %(list[-1], "Red"))

import calendar
print (calendar.month(2022,2))