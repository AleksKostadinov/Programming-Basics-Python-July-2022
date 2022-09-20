#https://judge.softuni.org/Contests/Practice/Index/1061#0
tribonacci1 = int(input())
tribonacci2 = int(input())
tribonacci3 = int(input())

spiralStart = int(input())
spiralStep = int(input())

spiralStep1 = 0
spiralStep2 = 0
number = spiralStep
count = 0

if tribonacci1 == spiralStart or tribonacci2 == spiralStart or tribonacci3 == spiralStart:
    print(spiralStart)

else:

    while spiralStep1 <= 1000000:

        tribonacciNext = 0
        a = tribonacci1
        b = tribonacci2
        c = tribonacci3
        while tribonacciNext <= spiralStep2:

            tribonacciNext = a + b + c
            if tribonacciNext == spiralStep1 or tribonacciNext == spiralStep2:
                print(tribonacciNext)
                spiralStart = 1000000
                count += 1
                break

            a = b
            b = c
            c = tribonacciNext

        spiralStep1 = spiralStart + spiralStep
        if spiralStep1 == tribonacci1 or spiralStep1 == tribonacci2 or spiralStep1 == tribonacci3:
            print(spiralStep1)
            break

        spiralStep2 = spiralStep1 + spiralStep
        if spiralStep2 == tribonacci1 or spiralStep2 == tribonacci2 or spiralStep2 == tribonacci3:
            print(spiralStep2)
            break

        spiralStart = spiralStep2
        spiralStep += number

if spiralStep1 > 1000000 and count == 0:
    print("No")