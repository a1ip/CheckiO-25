def check_pangram(text):

    list = set()
    for ch in text:
        if (ch.lower() in list) and (ch.lower().isalpha()):
            continue
        elif ch.lower().isalpha():
            list.add(ch.lower())

    return len(list) == 26

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
