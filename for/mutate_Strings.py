#https://judge.softuni.org/Contests/Compete/Index/1719#9

str1 = input()
str2 = input()
new = ""
add = ""

for i in range(len(str1)):
    if str1[i] == str2[i]:
        add = str1[i]
        new += add
    else:
        add = str2[i]
        new += add
        new_word = new
        for j in range(i + 1, len(str1)):
            new_word += str1[j]
        print(new_word)