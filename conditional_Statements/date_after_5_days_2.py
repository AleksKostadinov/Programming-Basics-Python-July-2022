d = int(input())
m = int(input())

days = 31

if m == 2:
    days = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    days = 30
d += 5

if d > days:
    d -= days
    m += 1
    if m > 12:
        m = 1
print('%d.%02d' % (d, m))
