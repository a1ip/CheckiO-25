def checkio(words):
    count = 0
    isWord = False


    for letter in words:
        if(not letter.isspace() and not letter.isnumeric()):
            isWord = True
        if(letter.isspace() and isWord):
            count += 1
            isWord = False
            if count == 3:
                return True
        if(letter.isnumeric()):
            count = 0
            isWord = False
        
    return count >= 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
