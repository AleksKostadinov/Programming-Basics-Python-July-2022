text = input()
summ = 0

for i in range(0, len(text)):
    if text[i] == "a":
        summ += 1
    if text[i] == "e":
        summ += 2
    if text[i] == "i":
        summ += 3
    if text[i] == "o":
        summ += 4
    if text[i] == "u":
        summ += 5
print(summ)
