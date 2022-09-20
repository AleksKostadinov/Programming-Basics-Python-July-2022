shirt_price = float(input())
expected_amount_for_ball = float(input())

short_price = shirt_price * 0.75
socks_price = short_price * 0.20
buttons_price = (shirt_price + short_price) * 2
discount = 0.85

cost = (shirt_price + short_price + socks_price + buttons_price) * 0.85

if cost >= expected_amount_for_ball:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {cost:.2f} lv.")
else:
    diff = expected_amount_for_ball - cost
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
