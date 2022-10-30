def write():
    file = open('file.txt', 'w')
    file.write("1\n")
    file.write("2\n")
    file.write("3\n")
    file.close()
    
def append():
    file = open('file.txt', 'a')
    first = input("What would you like to input on the fourth line?")
    second = input("What would you like to input on the fifth line?")
    file.write(f"{first}\n")
    file.write(second)
    file.close()
    
write()
append()


