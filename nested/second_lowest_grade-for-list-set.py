#Given the names and grades for each student in a class of  students, store them in a nested list\
# and print the name(s) of any student(s) having the second lowest grade.

number = int(input())
my_list = []
second_lowest_names = []
scores = set()

for i in range(number):
    name = input()
    score = float(input())
    my_list.append([name, score])
    scores.add(score)

second_lowest = sorted(scores)[1]

for name, score in my_list:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')