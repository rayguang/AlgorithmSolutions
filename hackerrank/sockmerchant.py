import math
import os
import random
import re
import sys

def sockmerchant(n,ar):
    b = set(ar)
    counter = 0

    for i in b:
        counter += ar.count(i)//2
    
    return counter

if __name__== "__main__":
    fptr = open('output.txt', 'w')

    n = int(input())
    print("Number of sockes: ", n)
    ar = list(map(int, input().rstrip().split()))
    print("Color array: ", ar)
    

    print("Pair of socks:", result)
    result = sockmerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
