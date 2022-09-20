a1 = int(input())
a2 = int(input())
n = int(input())

for symbol1 in range(a1, a2):
    symbol1_char = chr(symbol1)
    if symbol1 % 2 != 0:
        symbol4 = symbol1
        for symbol2 in range(1, n):
            for symbol3 in range(1, int(n/2)):
                if (symbol2 + symbol3 + symbol4) % 2 != 0:
                    print(f"{symbol1_char}-{symbol2}{symbol3}{symbol4}")