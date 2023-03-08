from collections import Counter

if __name__ == '__main__':
    s = input()
    logocount = Counter(sorted(s)).most_common()
    logocount = logocount[:3]
    for i in logocount:
        print(i[0], i[1])
