# cf271B
# AC 6min. 1go

import sys
import bisect
sys.setrecursionlimit( 10 **5 )

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    n = int(readline())
    arr, tmp = [], 0
    tmp_list = list(map(int, readline().strip().split()))
    for i in tmp_list:
        tmp += i
        arr.append(tmp)
    
    #print(arr, "ARR")
    m = int(readline())
    tmp_list = list(map(int, readline().strip().split()))
    for target in tmp_list:
        print(bisect.bisect_left(arr, target)+1)

process()