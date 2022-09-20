from math import floor

n = int(input())
stars = 1
dash = floor((n - stars) / 2)

if n % 2 != 0:
    stars = 1
else:
    stars = 2
print(str("-" * dash) + str("*" * stars) + str("-" * dash))

for i in range(1, floor((n + 1) / 2)):
    print(str("-" * (dash - i)) + str("*" * ((i * 2) + stars)) + str("-" * (dash - i)))

for j in range(1, floor((n + 1) / 2)):
    print('|' + str('*' * (n - 2)) + '|')