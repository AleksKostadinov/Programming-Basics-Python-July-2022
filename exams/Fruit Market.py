price_strawberry = float(input())
banana_per_kg = float(input())
orange_per_kg = float(input())
raspberry_per_kg = float(input())
strawberry_per_kg = float(input())

price_raspberry = price_strawberry * 0.5
price_orange = price_raspberry * 0.6
price_banana = price_raspberry * 0.2
total_price = price_strawberry * strawberry_per_kg + price_raspberry * raspberry_per_kg + \
              price_orange * orange_per_kg + price_banana * banana_per_kg

print(f"{total_price:.2f}")
