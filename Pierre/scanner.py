#!/usr/bin/python

import sys

print("What is your name?")
name = sys.stdin.readline()
print"Hello", name
print("How old are you?")
age = sys.stdin.readline()
string = "You are %d years old" % (age)
print string
print"You are %s years old",age
print("What is the name of your country?")
country = sys.stdin.readline()
print"your country is",country
