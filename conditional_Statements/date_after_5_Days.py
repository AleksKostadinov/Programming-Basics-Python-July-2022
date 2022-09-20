d = int(input())
m = int(input())

if m == 2:
    days = 28
    if d <= 23:
        future_day = d + 5
        print(f"{future_day}.02")
    else:
        future_day = d + 5
        out_date = future_day % days
        print(f"{out_date}.03")
elif m == 4 or m == 6 or m == 9 or m == 11:
    days = 30
    if d <= 25:
        future_day = d + 5
        if m != 11:
            print(f"{future_day}.0{m}")
        else:
            print(f"{future_day}.{m}")
    else:
        future_day = d + 5
        out_date = future_day % days
        if m == 9:
            print(f"{out_date}.{m + 1}")
        elif m != 11:
            print(f"{out_date}.0{m + 1}")
        else:
            print(f"{out_date}.{m + 1}")
else:
    days = 31
    if d <= 26:
        future_day = d + 5
        if m < 10:
            print(f"{future_day}.0{m}")
        else:
            print(f"{future_day}.{m}")
    else:
        future_day = d + 5
        out_date = future_day % days
        if m == 10:
            print(f"{out_date}.{m + 1}")
        elif m == 12:
            print(f"{out_date}.0{1}")
        else:
            print(f"{out_date}.0{m + 1}")
