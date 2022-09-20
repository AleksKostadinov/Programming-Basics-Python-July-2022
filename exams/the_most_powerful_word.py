word = input()
max_sum_word = -1
max_word = ""
total_sum = 0

while word != "End of words":
    total_sum = 0

    if word == "End of words":
        break

    length = len(word)

    for i in word:
        total_sum += ord(i)

    if word[0].lower() in 'aeiouy':
        total_sum *= length
    else:
        total_sum = int(total_sum / length)

    if total_sum > max_sum_word:
        max_sum_word = total_sum
        max_word = word

    word = input()

print(f"The most powerful word is {max_word} - {max_sum_word}")