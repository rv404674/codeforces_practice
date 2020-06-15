import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)
readline = sys.stdin.readline

for _ in range(int(readline())):
    n = int(readline())
    a = list(map(int, readline().split()))

    # dry run on
    # check aryan solution on yt
    # 7
    # 2 9 10 1 7 10 13
    ans = [a[0]]
    for i in range(1, n-1):
        if a[i-1]>a[i]<a[i+1] or a[i-1]<a[i]>a[i+1]:
            ans.append(a[i])
    
    ans.append(a[-1])

    print(len(ans))
    # dont do print(ans) = it will give list [1,2,3]
    print(*ans) # 1 2 3



