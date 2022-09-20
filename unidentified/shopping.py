budget = float(input())
video = int(input())
processor = int(input())
ram = int(input())

video_prices = 250 * video
processor_prices = (video_prices * 35 / 100) * processor
ram_prices = (video_prices * 10 / 100) * ram

stocks = video_prices + processor_prices + ram_prices

if video > processor:
    total = stocks * (1 - 15 / 100)
    if budget >= total:
        print(f"You have {budget - total:.2f} leva left!")
    else:
        print(f"Not enough money! You need {total - budget:.2f} leva more!")

else:
    total = stocks
    if budget >= total:
        print(f"You have {budget - total:.2f} leva left!")
    else:
        print(f"Not enough money! You need {total - budget:.2f} leva more!")