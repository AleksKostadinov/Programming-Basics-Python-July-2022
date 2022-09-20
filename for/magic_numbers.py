n = int(input())
result_str = ""
for i1 in range(1, 10):
    for i2 in range(1, 10):
        for i3 in range(1, 10):
            for i4 in range(1, 10):
                for i5 in range(1, 10):
                    for i6 in range(1, 10):
                        if i1 * i2 * i3 * i4 * i5 * i6 == n:
                            result_str += ("" + str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6) + " ")
print(result_str)