# cf div2 277.5
# n,m <=100
# Brute
# 35min

import sys
from sys import setrecursionlimit
setrecursionlimit( 10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", "w")

readline = sys.stdin.readline

def process():
    n = int(readline())
    boys = list(map(int, readline().strip().split()))

    m = int(readline())
    girls = list(map(int, readline().strip().split()))
    visited_girls = [False] *m

    cnt = 0
    boys.sort()
    girls.sort()

    for i in range(n):
        for j in range(m):
            if abs(boys[i]-girls[j])<=1 and not visited_girls[j]:
                cnt +=1
                visited_girls[j] = True
                break
    print(cnt)

#for _ in range(int(readline())):
#process()


# OPTIMIZED ONE
# NOTE: sorted returns a list
def process2():
    I = lambda:sorted(map(int, input().split()))
    n = I()[0]
    boys = I()
    m = I()[0]
    girls = I()

    i,j,k = 0,0,0
    while i<n and j<m:
        if abs(boys[i]-girls[j])<2: i+=1;j+=1;k+=1
        elif boys[i]<girls[j]: i+=1
        else: j+=1
    
    print(k)


for _ in range(int(readline())):
    process2()