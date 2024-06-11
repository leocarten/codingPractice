class StringMethods:
    def __init__(self) -> None:
        pass

    def charInString(self, charToFind, string):
        charCount = 0 
        for i in string:
            if i == charToFind:
                charCount += 1
        return charCount
    
def main():
    myObj = StringMethods()
    print(myObj.charInString('l','hello'))

main()