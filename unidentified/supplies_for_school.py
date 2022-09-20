pen = int(input())
marker = int(input())
cleaner = int(input())
discount = float(input())
price = pen * 5.8 + marker * 7.2 + cleaner * 1.2
finalPrice = price - (price * (discount/100))
print(finalPrice)
