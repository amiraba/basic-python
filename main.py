# https://www.youtube.com/watch?v=cybMiQYuEwc&list=PLH1n1sJO7tbxmE36txTPhgidmW5Z9Bn7m&index=1

import time
import datetime

print(time.time())
print (datetime.datetime.fromtimestamp(time.time()))

def my_func():
    print (datetime.datetime.now())
    print('month =', datetime.datetime.now().strftime("%m"))
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

#printing styles
from os import listdir
files_list = listdir('/usr')
files_list_same = [f for f in listdir('/usr')]
print (files_list, '\r\n', files_list_same) # every comma adds a space automatically. Otherwise make 2 print() separately or :

name, age = "Amira", 20
address = "Tunisia"
print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

print("%s and %s." %("Peace", "Love"))

from os.path import isfile, join
files_list_only_files = [f for f in listdir('/Users') if isfile(join('/Users', f))]
print (files_list_only_files)

# The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
from subprocess import call
call(["ls", "-1"])

import sys
print(sys.version)
print(sys.version_info)

import multiprocessing
print("Number of CPUs : ", multiprocessing.cpu_count())

from math import pi
r=1
#r = float(input("insert the cercle's radius here: "))
print(round(pi * r**2, 2))

values=("1,2,3")
list=values.split(',')
mytuple=tuple(list)
print("list: ", list)
print("tuple: ", mytuple, type(mytuple))
# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.

# Set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
myset={3,1,2}
print(type(myset))

c1 = set(["Black", "Red", "White"])
c2 = set(["Black", "White"])
print("Difference between two sets: ", c1.difference(c2))

# Dictionary holds key-value pairs. However, you may not use an unhashable item as a key.
mydict1 = dict(one=1, two=2, three=3)
print(mydict1)
print(type(mydict1))
print(mydict1["three"])

mydict={1:"Yes",2:"No",3:"Maybe"}
print(mydict)
print(mydict[3])

# basic python collections (the 4: dict, list, set et tuple): https://data-flair.training/blogs/python-data-structures-tutorial/
# collections++ : https://docs.python.org/fr/3/library/collections.html

print("%s and %s." %(list[-1], "Red"))

import calendar
print (calendar.month(2022,2))

# Slicing
# slice(start-Optional-included, end-non-including, step-Optional-ifStepUShouldSpecifyAll2parametersBefore)
a = ("a", "b", "c", "d", "e", "f", "g", "h")
slicing= slice(0,7,-1)
reverse_number_slice= a[slicing]
print (reverse_number_slice)

y= slice(0, 8, 3)
print(y)
print(a[y])

x = slice(3, 5)
print(x)
print(a[x])

reverse_number = str(123)[::-1]
print (reverse_number)

# https://www.w3schools.com/python/ref_func_slice.asp#:~:text=The%20slice()%20function%20returns,slice%20only%20every%20other%20item.
#https://www.programiz.com/python-programming/methods/built-in/slice

list_numbers = [1,2,3]
print ("max:", max(list_numbers), "- min:", min(list_numbers), "- sum:", sum(list_numbers))

# convert list into string
list_b = [1,2,3]
result_string=""
for i in list_b:
    result_string +=str(i)
print(result_string)

# str to int/float and vice versa
n= 20
s= str(n)
print(type(n), type(s), n, s)

nn= "33"
ss= int(nn)
print(type(nn), type(ss), nn, ss)

nd= 20.0
sd= str(nd)
print(type(nd), type(sd), nd, sd)

nnd= "33.0"
ssd= float(nnd)
print(type(nnd), type(ssd), nnd, ssd)

# stopped at 56 if you wanna resume, resume from 57