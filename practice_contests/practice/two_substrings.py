import sys

sys.setrecursionlimit(10 ** 5)
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

readline = sys.stdin.readline

def process():
    s = readline().strip()
    a = s.find('AB')
    if a!=-1 and s[a+2:].find('BA')!=-1:
        print("YES")
        return
    
    a = s.find('BA')
    if a!=-1 and s[a+2:].find('AB')!=-1:
        print("YES")
        return
    print("NO")


#for _ in range(int(readline())):
process()