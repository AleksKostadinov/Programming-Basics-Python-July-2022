n = int(input())
m = int(input())
gcp = 1

if n != m:
    multiply = n * m
    if n > m:
        while n % m != 0:
            gcp = n % m
            n = m
            m = gcp
        else:
            gcp = m % n
    elif m > n:
        while m % n != 0:
            gcp = m % n
            m = n
            n = gcp
        else:
            gcp = n % m
    lcm = multiply / gcp
else:
    lcm = n

total = gcp + lcm
print('%d' % total)