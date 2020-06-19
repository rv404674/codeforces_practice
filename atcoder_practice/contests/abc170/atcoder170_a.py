import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def proc():
    a = list(map(int, readline().rstrip().split()))
    for i,j in enumerate(a):
        if not j:
            print (i+1)
            return



#for _ in range(int(readline())):
proc()