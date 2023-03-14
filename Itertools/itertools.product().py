from itertools import product
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
A = sorted(A)
B = sorted(B)
tupleA = tuple(A)
tupleB = tuple(B)
tuplelist = list(product(tupleA, tupleB))
for i in tuplelist:
    print(i, end=" ")
