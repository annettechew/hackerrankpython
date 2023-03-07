from collections import Counter

X = int(input()) # no of shoes
sizesavai = Counter(map(int, input().split(" ")))

N = int(input()) # no of customers
earn = 0 #counter
for i in range(0, N):
    size, x = map(int, input().split(" "))
    if sizesavai[size] != 0:
        earn += x
        sizesavai[size] -= 1
print(earn)
