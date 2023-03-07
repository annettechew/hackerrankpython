def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        w = len(bin(number)[2:]) #width
        octal = oct(i)[2:]
        hexadec = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print (str(i).rjust(w, " "), str(octal).rjust(w, " "), str(hexadec).rjust(w, " "), str(binary).rjust(w, " "))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
