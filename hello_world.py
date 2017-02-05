import random
import sys
import os

wordlist = ["Hello", "World", "how", "are", "you"]
todolist = ["wash", "cars", "go shopping"]

print(wordlist, todolist)

def fun(list):
    for i in list:
        print(i, end=" ")

def fib(n):
    a = 1
    b = 1
    print("1 \\\n1 \\")
    for i in range(0,n):
        tmp = b
        b += a
        a = tmp
        print(b, end="")
        for j in range(0,b):
            print(" \\", end="")
        print()

fib(10)
fun(wordlist)
fun(todolist)