first_letter = input()
last_letter = input()
pass_letter = input()
new_word = ""
valid_count = 0
for i in range(ord(first_letter), ord(last_letter) + 1):
    if chr(i) == pass_letter:
        continue
    for j in range(ord(first_letter), ord(last_letter) + 1):
        if chr(j) == pass_letter:
            continue
        for k in range(ord(first_letter), ord(last_letter) + 1):
            if chr(k) == pass_letter:
                continue
            new_word += chr(i) + chr(j) + chr(k) + " "
            valid_count += 1
print(new_word, end="")
print(valid_count)