n = int(input())
nlist = list(map(int, input().split(" ")))
print(all([i>0 for i in nlist]) and any([str(i) == str(i)[::-1] for i in nlist]))
