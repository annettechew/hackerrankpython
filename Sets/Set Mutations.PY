A = int(input())
setA = set(map(int, input().split()))
N = int(input())
for i in range(N):
    ops = input().split()
    seto = set(map(int, input().split()))
    if ops[0] == 'intersection_update':
        setA.intersection_update(seto)
    elif ops[0] == 'update':
        setA.update(seto)
    elif ops[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(seto)
    elif ops[0] == 'difference_update':
        setA.difference_update(seto)
print(sum(setA))
