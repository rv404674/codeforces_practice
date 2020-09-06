import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit( 10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    a,b = map(int,readline().strip().split())
    if a==b:
        print(0)
        return
    
    diff = a-b if a>b else b-a
    if diff%10 == 0:
        print(diff//10)
        return
    
    print(1+diff//10)

for _ in range(int(readline())):
    process()