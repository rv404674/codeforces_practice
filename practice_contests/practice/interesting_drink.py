# div2367 B
# https://codeforces.com/problemset/problem/706/B

import sys
# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def binary_search(arr,x):
    l,h = 0,len(arr)-1

    while l<=h:
        mid = l + (h-l)//2
        if x<arr[mid]:
            h = mid-1
        else:
            l = mid +1
    return l

def process():
    _ = int(readline())
    arr = sorted(map(int, readline().strip().split()))

    for _ in range(int(readline())):
        x = int(readline())
        print(binary_search(arr,x))

#for _ in range(int(readline())):
process()
        

# NOTE: More Optimized One
def process2():
    # instead of writing your owrn binary search
    import bisect
    print(bisect.bisect([3,5,6,7,8],10))
    # it will basically give the largest position where 10 should be inserted
    # so in this case 5