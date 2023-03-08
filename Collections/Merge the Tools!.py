import textwrap

def merge_the_tools(string, k):
    list = textwrap.wrap(string, k)
    for substring in list:
        slist = []
        for character in substring:
            if character not in slist:
                slist.append(character)
        print("".join(slist))
        
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
