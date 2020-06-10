# take example
# 1 2 3 4 5
# 4 5 1 3 2

n = int(input())
a = list( map(int, input().split()))
b = list( map(int, input().split()))

hash_map = {}
for i,j in enumerate(a):
    hash_map[j] = i

count_array = [0] * n
for i,j in enumerate(b):
    diff = hash_map[j] - i
    if diff <0:
        diff +=n
    count_array[diff] += 1

print(max(count_array))

# here is the video editorial for this questions - 
# https://www.youtube.com/watch?v=5CNUgWx-Iuo&feature=youtu.be