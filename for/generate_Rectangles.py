#https://judge.softuni.org/Contests/Practice/Index/1059#11
n = int(input())
m = int(input())
count = 0
for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left + 1, n + 1):
            for bottom in range(top + 1, n + 1):
                area = abs(right - left) * abs(bottom - top)

                if area >= m:
                    print('(%d, %d) (%d, %d) -> %d' % (left, top, right, bottom, area))

                    count += 1
if count == 0:
    print("No")