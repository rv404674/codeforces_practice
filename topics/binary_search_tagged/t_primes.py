import sys
from math import sqrt, ceil
from sys import setrecursionlimit

setrecursionlimit( 10 **5 )
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

readline = sys.stdin.readline

# SOLUTION
# observer t_primes are squares of prime number.
# t_primes <= 10^12
# max number = sqrt(10^12) = 10^6
# use sieve of eratosthenes to find prime numbers till (10^6)

# similar to sieve of eratosthenes
def util():
    a = set()

    n = 10 ** 6
    prime = [True] * (n+1)
    p=2
    while p <= n:
        if prime[p]:
            # modified it according to qn.
            # append the prime square
            a.add(p*p)
            for i in range(p*2, n+1, p):
                prime[i] = False
        p+=1
    
    prime[0] = prime[1] = False
    return a

def process():
    _ = int(readline())
    arr = map(int, readline().rstrip().split())
    # O(10^6)
    prime = util()

    for i in arr:
        print("YES") if i in prime else print("NO")

#for _ in range(int(readline())):
process()