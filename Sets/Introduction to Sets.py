def average(array):
    # your code goes here
    distinctset = set(array)
    avg = sum(distinctset)/len(distinctset)
    return (round(avg, 3))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
