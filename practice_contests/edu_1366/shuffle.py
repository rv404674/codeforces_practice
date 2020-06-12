from sys import setrecursionlimit
from sys import stdin

readline = stdin.readline
setrecursionlimit( 10 **5)

for _ in range(int(input())):
    n,x,m = list(map(int, input().split()))
    l,r = x,x
#    print("L R", l,r)

    for i in range(m):
        l1, l2 = map(int, readline().split())

        if l1 <=r and l2 >=l:
            l,r = min(l,l1), max(r,l2)
    
    print(r-l+1)
