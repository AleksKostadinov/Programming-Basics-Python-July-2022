n = int(input())
result = ""
a = 1

while a <= 9:
    b = 1
    while b <= 9:
        c = 1
        while c <= 9:
            d = 1
            while d <= 9:
                e = 1
                while e <= 9:
                    f = 1
                    while f <= 9:
                        if a * b * c * d * e * f == n:
                            result += ("" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + " ")
                        f += 1
                    e += 1
                d += 1
            c += 1
        b += 1
    a += 1
print(result)