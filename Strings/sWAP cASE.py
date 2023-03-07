def swap_case(s):
    list = []
    for i in s:
        if i.islower() == True:
            i = i.upper()
        elif i.isupper() == True:
            i = i.lower()
        list.append(i)
    return "".join(list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
