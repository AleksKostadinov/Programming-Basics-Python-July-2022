min_control = int(input())
sec_control = int(input())
length_control = float(input())
sec_100m = int(input())

sec_control = min_control * 60 + sec_control
total_slow = (length_control / 120) * 2.5
total_time = (length_control / 100) * sec_100m - total_slow

if total_time <= sec_control:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {total_time:.3f}.")
else:
    diff = total_time - sec_control
    print(f"No, Marin failed! He was {diff:.3f} second slower.")