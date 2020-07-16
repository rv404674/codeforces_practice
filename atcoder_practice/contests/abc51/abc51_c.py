import sys
sys.setrecursionlimit(10 ** 5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def process():
    sx, sy, tx, ty = map(int, readline().rstrip().split())
    dx = tx-sx
    dy = ty-sy

    ans = ""
    # covers going both up and down
    ans += 'U'*dy + 'R'*dx + 'D'*dy + 'L'*dx
    # now going up again
    ans += 'L' + 'U'*(dy+1) + 'R'*(dx+1) + 'D'
    ans += 'R' + 'D'*(dy+1) + 'L'*(dx+1) + 'U'

    return ans

#for _ in range(int(readline().rstrip())):
print(process())