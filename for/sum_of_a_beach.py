#https://judge.softuni.org/Contests/Practice/Index/1720#3
text = input()
text = text.lower()
mylist = ["sand", "water", "fish", "sun"]
counter = 0
for item in mylist:
    if item in text:
        total_count = text.count(item)
        counter += total_count
print(counter)