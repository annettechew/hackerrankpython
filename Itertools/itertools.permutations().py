from itertools import permutations
S, k = input().split(" ")
k = int(k)
S = list(S)
permlist = list(permutations(S, k))
for i in sorted(permlist):
    print("".join(i))
