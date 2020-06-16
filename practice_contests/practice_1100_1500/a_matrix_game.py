import sys
from sys import setrecursionlimit
setrecursionlimit(10 **5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

# take cases
# n>m, n<m
# 3 1
# 0
# 0
# 0

def util():
    n,m = list(map(int, readline().split()))
    grid = [ list(map(int,readline().split())) for _ in range(n)]

    # so that you dont count a row twice
    visited_r = set()
    visited_c = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                visited_r.add(i)
                visited_c.add(j)

    mn = min(n-len(visited_r), m-len(visited_c))
    if mn %2:
        print("Ashish")
    else:
        print("Vivek")

for _ in range(int(readline())):
    util()