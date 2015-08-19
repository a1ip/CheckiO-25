def checkio(data):

    UpFlag = False
    LowFlag = False
    DecFlag = False
    if len(data) < 10:
        return False
    for elem in data:
        if elem.isupper():
            UpFlag = True
        elif elem.islower():
            LowFlag = True
        elif elem.isdecimal():
            DecFlag = True
    return UpFlag and LowFlag and DecFlag

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
