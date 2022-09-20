from math import ceil
price_per_video_card = int(input())
price_per_transition = int(input())
price_electricity_per_video_card_daily = float(input())
profit_per_card_daily = float(input())
price_for_other_components = 1000

price_cards = price_per_video_card * 13
price_transition = price_per_transition * 13
total_price = price_transition + price_cards + price_for_other_components
profit_per_day = profit_per_card_daily - price_electricity_per_video_card_daily
total_profit_cards = 13 * profit_per_day

print(f"{total_price}")
days = total_price / total_profit_cards
print(f"{ceil(days)}")
