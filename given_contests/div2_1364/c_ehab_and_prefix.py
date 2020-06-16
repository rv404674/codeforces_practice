# OBSERVE

# if i>a[i], -1. (i starts from 1)
# if a[i] != a[i-1], b[i] = a[i-1]

import sys
from sys import setrecursionlimit
setrecursionlimit(10 **5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

n = int(readline())
a = list(map(int, readline().split()))
b = [-1] *n
not_visited = []
visited = [-1] * 10**6

flag = True
for i,j in enumerate(a):
    if j>i+1:
        flag = False
        break
    visited[j] = 1

if not flag:
    print(-1)
    sys.exit(0)

for i in range(1, n):
    if a[i] != a[i-1]:
        b[i] = a[i-1]

for i,j in enumerate(visited):
    if j == -1:
        not_visited.append(i)

k=0
for i,j in enumerate(b):
    if j==-1:
        b[i] = not_visited[k]
        k+=1

print(*b)




