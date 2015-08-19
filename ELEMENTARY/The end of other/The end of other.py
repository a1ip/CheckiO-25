def checkio(words_set):
    for w1 in words_set:
        for w2 in words_set:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False