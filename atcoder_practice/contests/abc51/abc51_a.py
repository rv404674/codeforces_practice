import sys
sys.setrecursionlimit(10 ** 5)

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def process():
    temp_list = readline().rstrip().split(',')
    return ' '.join(temp_list)

# for _ in range(int(readline().rstrip())):
#    print(process())

print(process())