import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit( 10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline
ans_d = float('+INF')

def binary_search(lo,hi,diff,n):
    mid = lo + (hi-lo)//2
    if diff%mid == 0:
        if diff//mid +1 == n:
            ans_d = min(ans_d, mid+(n-1)*mid)

    if diff%mid !=0:
        binary_search(lo,mid-1,diff,n)
        binary_search(mid+1,hi,diff,n)
    else:
        total_num = diff//mid +1
        if total_num>n:
            lo = mid+1
        else:
            hi = mid

def process():
    n,x,y = map(int, readline().strip().split())
    if n==2:
        #TODO:
        pass
    
    lo,hi,diff = 1,10**9, y-x
    binary_search(lo,hi,diff,n)
    print(ans_d)


for _ in range(int(readline())):
    x = process()
