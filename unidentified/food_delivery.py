chicken = int(input())
fish = int(input())
vegan = int(input())
chickenM = chicken * 10.35
fishM = fish * 12.4
veganM = vegan * 8.15
menu = chickenM + fishM + veganM
desert = menu * 0.2
delivery = 2.5
price = chickenM + fishM + veganM + desert + delivery
price = str(round(price, 2))
print(price)
