import statistics
n, x = map(int, input().split(" "))
list = []
for i in range(x):
    scores = input().split(" ")
    list.append([float(j) for j in scores])
for k in zip(*list):
    print(statistics.mean(k))
