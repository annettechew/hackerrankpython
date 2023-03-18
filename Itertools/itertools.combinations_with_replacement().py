from itertools import combinations_with_replacement
s, k = input().split(" ")


comlist = list(combinations_with_replacement(sorted(s), int(k)))
for i in comlist:
    print("".join(i))
