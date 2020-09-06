import sys
sys.setrecursionlimit(10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    n,k = map(int, readline().strip().split())
    if k%(n-1) == 0:
        bucket = k//(n-1)
        print(n*bucket-1)
        return
    
    bucket, left = k//(n-1), k%(n-1)
    lo = n*bucket+1
    print(lo+left-1)
    
for _ in range(int(readline())):
    process()