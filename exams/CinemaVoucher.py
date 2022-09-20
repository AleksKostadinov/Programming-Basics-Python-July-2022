budget = int(input())
purchase = input()
movie = 0
other = 0
while purchase != "End":
    if len(purchase) > 8:
        budget -= ord(purchase[0]) + ord(purchase[1])
        if budget < 0:
            break
        movie += 1
    else:
        budget -= ord(purchase[0])
        if budget < 0:
            break
        other += 1
    purchase = input()
print(f"{movie}")
print(f"{other}")