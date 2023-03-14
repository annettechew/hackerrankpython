from itertools import permutations
S, k = input().split(" ")
k = int(k)
permlist = list(permutations(S, k))
for i in sorted(permlist):
    print("".join(i))
