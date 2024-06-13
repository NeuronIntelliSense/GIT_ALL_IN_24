def count_chars(word):
    diction = {}
    for character in word:
        if character not in diction:
            diction[character] = 1
        else:
            diction[character] += 1

    return diction
