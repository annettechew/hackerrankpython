n = int(input())
en = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))
diffset = en.difference(fr)
print(len(diffset))
