number_groups = int(input())

summ = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
tr_musala = 0
tr_monblan = 0
tr_kilimandjaro = 0
tr_k2 = 0
tr_everest = 0

for i in range(number_groups):
    number_people_per_group = int(input())
    summ += number_people_per_group
    if number_people_per_group <= 5:
        musala += number_people_per_group
    elif number_people_per_group <= 12:
        monblan += number_people_per_group
    elif number_people_per_group <= 25:
        kilimandjaro += number_people_per_group
    elif number_people_per_group <= 40:
        k2 += number_people_per_group
    else:
        everest += number_people_per_group

    tr_musala = musala / summ * 100
    tr_monblan = monblan / summ * 100
    tr_kilimandjaro = kilimandjaro / summ * 100
    tr_k2 = k2 / summ * 100
    tr_everest = everest / summ * 100

print(f"{tr_musala:.2f}%")
print(f"{tr_monblan:.2f}%")
print(f"{tr_kilimandjaro:.2f}%")
print(f"{tr_k2:.2f}%")
print(f"{tr_everest:.2f}%")