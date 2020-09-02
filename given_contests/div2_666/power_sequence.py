# Reall good questions, observation is required.
# codeforces div2b 666

import sys
sys.setrecursionlimit(10 ** 5)

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

readline = sys.stdin.readline

def process():
    _ = int(readline())
    arr = list(map(int, readline().strip().split()))
    # NOTE:
    # it makes sense to sort array
    # because as our c^i will be increasing, so our number should increase as well
    # to make diff min.
    arr.sort()

    # we are not taking mx=10 ** 9, because that is the limit on the input.
    # it is not necessary that our c^i can't reach there.
    ans, mx = 10 ** 20, 10 **20
    overflow = False

    # we wont get TLE because of the two loops
    # as if n=50, and c=2, 2**50 = 1125899906842624
    # so if we increase c, we will reach overflow in no time.
    for i in range(1, 10**5):
        # i is used as c
        val,diff = 1,0
        for num in arr:
            if val*i > mx:
                overflow = True
                break
            else:
                diff += abs(val-num)
                val *=i
        
        ans = min(ans, diff)
        if overflow:
            break
    
    print(ans)

# for _ in range(int(readline())):
process()
