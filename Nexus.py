def release(string):
    print(string)

def inputint(type_input):
    int(input(type_input))

def inputstr(type_input):
    str(input(type_input))

def loopF(string = str, func = str, key = int, lock = int, footfall = int):
    string = string
    if func == ("release"):
        for string in range(key, lock, footfall):
            print(string)
    elif func == ("input"):
        for string in range(key, lock, footfall):
            input(string)

def loopW(string = str, func = str, boolean = True):
    string = string
    if func == ("release"):
        loop = boolean
        while loop:
            print(string)
    elif func == ("input"):
        loop = boolean
        while loop:
            input(string)
