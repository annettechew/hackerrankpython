setA = set(map(int, input().split(" ")))
num = int(input())

count = 0
for i in range(num):
    s = set(map(int, input().split(" ")))
    if setA.issuperset(s):
        count += 1
if count == num:
    print(True)
else:
    print(False)
