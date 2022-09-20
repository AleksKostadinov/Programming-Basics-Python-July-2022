heritage_money = float(input())
year_to_live = int(input())
current_age = 18

for years in range(1800, year_to_live + 1):

    if years % 2 == 0:
        heritage_money -= 12000
    else:
        heritage_money -= 12000 + 50 * current_age
    current_age += 1

if heritage_money >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage_money):.2f} dollars to survive.")

# Иванчо е на 18 години и получава наследство, което се състои от X сума пари и машина на времето. Той решава да се
# върне до 1800 година, но не знае дали парите ще са достатъчни, за да живее без да работи. Напишете програма,
# която пресмята, дали Иванчо ще има достатъчно пари, за да не се налага да работи до дадена година включително. Като
# приемем, че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева. За всяка нечетна (1801,1803  и т.н.) ще
# харчи 12 000 + 50 * [годините, които е навършил през дадената година].
