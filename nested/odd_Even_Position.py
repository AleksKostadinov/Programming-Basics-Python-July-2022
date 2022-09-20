n = int(input())
odd_sum = 0
max_odd = -100000
min_odd = 100000
even_sum = 0
max_even = -100000
min_even = 100000
i = None
for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        even_sum += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    else:
        odd_sum += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num

if i is None:
    print(f'OddSum=0.00,')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif i == 1:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_odd:.2f},')
    print(f'OddMax={max_odd:.2f},')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={min_odd:.2f},')
    print(f'OddMax={max_odd:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={min_even:.2f},')
    print(f'EvenMax={max_even:.2f}')