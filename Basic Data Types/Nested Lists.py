if __name__ == '__main__':
    n = int(input())
    records = []
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = []
    for i in range(n):
        scores.append(records[i][1])
    secondlowest = sorted(set(scores), reverse=False)[1]
    names = []
    for i in range(n):
        if records[i][1] == secondlowest:
            names.append(records[i][0])
    names.sort()
    print("\n".join(names))
