#https://judge.softuni.org/Contests/Practice/Index/1061#1
from datetime import date as datetime
from datetime import timedelta
from math import floor

first_year = int(input())
second_year = int(input())
number_to_search_for = int(input())

date = datetime(first_year, 1, 1)
date = date + timedelta(days=1)
found = False
while date.year <= second_year:

    date = date + timedelta(days=1)

    d1 = floor(date.day / 10)
    d2 = date.day % 10
    d3 = floor(date.month / 10)
    d4 = date.month % 10
    d5 = floor(date.year / 1000)
    d6 = floor(date.year / 100) % 10
    d7 = floor(date.year / 10) % 10
    d8 = date.year % 10

    weight = d1 * (d2 + d3 + d4 + d5 + d6 + d7 + d8) + d2 * (d3 + d4 + d5 + d6 + d7 + d8) + \
             d3 * (d4 + d5 + d6 + d7 + d8) + d4 * (d5 + d6 + d7 + d8) + \
             d5 * (d6 + d7 + d8) + d6 * (d7 + d8) + d7 * d8

    if weight == number_to_search_for:
        print(str(d1) + str(d2) + "-" + str(d3) + str(d4) + "-" + str(d5) + str(d6) + str(d7) + str(d8))
        found = True
if not found:
    print("No")
