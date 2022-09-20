#https://judge.softuni.org/Contests/Practice/Index/1060#4
n = int(input())
str1 = '.' * ((4 * n // 2) - 1)
str2 = '/' + '|' + '\\'
str3 = '\\' + '|' + '/'
dash = 0
dots = 0
print(str1 + str2 + str1)
print(str1 + str3 + str1)
for i in range(0, 2 * n):
    dots += 1
    print('.' * ((4 * n // 2) - dots) + '*' + '-' * dash + '*' + '-' * dash + '*' + '.' * ((4 * n // 2) - dots))
    dash += 1

print('*' * (4 * n + 1))
print('*.' * (2 * n) + "*")
print('*' * (4 * n + 1))