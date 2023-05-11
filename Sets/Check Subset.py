t = int(input())
for i in range(t):
    a = int(input())
    aset = set(map(int, input().split(" ")))
    
    b = int(input())
    bset = set(map(int, input().split(" ")))
    
    print(aset.issubset(bset))
