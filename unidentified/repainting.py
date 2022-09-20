nylon = int(input())
paint = int(input())
thinner = int(input())
workHours = int(input())

bags = 0.40
nylonPrice = (nylon + 2) * 1.5
paintPrice = (paint + (paint * 0.1)) * 14.50
thinnerPrice = thinner * 5
priceForMaterials = bags + nylonPrice + paintPrice + thinnerPrice
workHoursPrice = workHours * (priceForMaterials * 0.3)

print(workHoursPrice + priceForMaterials)
