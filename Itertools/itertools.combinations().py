from itertools import combinations
s, k = input().split(" ")

for i in range(1, int(k)+1):
    comlist = list(combinations(sorted(s), i))
    for j in comlist:
        print("".join(j))
