import sys
sys.setrecursionlimit(10 ** 5)

# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

readline = sys.stdin.readline

def process():
    n = int(readline())
    a = list(map(int, readline().strip().split()))
    a.sort()

    # n>=2
    max_diff = a[-1]-a[0]
    if max_diff == 0:
        print("{} {}".format(max_diff, n*(n-1)//2))
        return

    x = a.count(a[-1]) * a.count(a[0])
    print("{} {}".format(max_diff, x))
    
#for _ in range(int(readline())):
process()