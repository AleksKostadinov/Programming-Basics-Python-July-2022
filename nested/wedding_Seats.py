last_sector = input()
number_rows_first = int(input())
number_seats_odd = int(input())
count = 0
seats = 0
cound_sector = - 1
for sector in range(65, ord(last_sector) + 1):
    cound_sector += 1
    for row in range(1, (number_rows_first + cound_sector) + 1):
        if row % 2 != 0:
            for seats in range(97, number_seats_odd + 97):
                print(f"{chr(sector)}{row}{chr(seats)}")
                count += 1
        else:
            for seats in range(97, number_seats_odd + 97 + 2):
                print(f"{chr(sector)}{row}{chr(seats)}")
                count += 1
print(count)
