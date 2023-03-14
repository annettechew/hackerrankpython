# Change language to Pypy 3
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuplei = tuple(integer_list)
    print(hash(tuplei))
