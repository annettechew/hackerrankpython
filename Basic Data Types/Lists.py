if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        text = input()
        command = text.split(" ")[0]
        if command == "insert":
            pos = int(text.split(" ")[1])
            val = int(text.split(" ")[2])
            list.insert(pos, val)
        elif command == "print":
            print(list)
        elif command == "remove":
            val = int(text.split(" ")[1]) 
            list.remove(val)
        elif command == "append":
            val = int(text.split(" ")[1]) 
            list.append(val)
        elif command == "sort":
            list.sort()
        elif command == "pop":   
            list.pop()
        elif command == "reverse":
            list.reverse()
