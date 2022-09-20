word = input()

max_total = -1
total = 0
powerful_word = ""
first = ""
while word != "End of words":
    summ = 0
    if word == "End of words":
        break
    length = len(word)
    for i in range(0, length):
        first = word[0]
        summ += ord(word[i])
        if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" or \
                first == "y" or first == "A" or first == "E" or first == "I" or first == "O" or \
                first == "U" or first == "Y":
            total = summ * length
        else:
            total = round(summ / length)
        if total > max_total:
            max_total = total
            powerful_word = word

    word = input()

print(f"The most powerful word is {powerful_word} - {max_total}")
