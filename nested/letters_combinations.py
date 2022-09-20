f_letter = input()
s_letter = input()
pass_letter = input()
word = ""
count = 0
for a in range(ord(f_letter), ord(s_letter) + 1):
    if chr(a) == pass_letter:
        continue
    for b in range(ord(f_letter), ord(s_letter) + 1):
        if chr(b) == pass_letter:
            continue
        for c in range(ord(f_letter), ord(s_letter) + 1):
            if chr(c) == pass_letter:
                continue
            count += 1
            word += chr(a) + chr(b) + chr(c) + " "
print(f"{word}{count}")