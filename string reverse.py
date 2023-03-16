def stringReverse(string):
    if len(string) == 0:
        return string
    elif len(string) == 1:
        return string
    else:
        return stringReverse(string[1:]) + string[0]


def main():
    string = input()
    print(stringReverse(string))

if __name__ == "__main__":
    main() 
