n = int(input())
sells_count = 0
rate_count = 0
for i in range(n):
    sells_rate = int(input())
    rate = sells_rate % 10
    sells = sells_rate // 10

    if rate == 2:
        sells_count += sells * 0
    elif rate == 3:
        sells_count += sells * 0.5
    elif rate == 4:
        sells_count += sells * 0.7
    elif rate == 5:
        sells_count += sells * 0.85
    elif rate == 6:
        sells_count += sells * 1

    rate_count += rate

avg_rate = rate_count / n
print(f"{sells_count:.2f}")
print(f"{avg_rate:.2f}")