#https://judge.softuni.org/Contests/Practice/Index/1720#1
text = input()
mylist = []

for i in range(len(text)):
    if text[i].isupper():
        mylist.append(i)
print(mylist)
