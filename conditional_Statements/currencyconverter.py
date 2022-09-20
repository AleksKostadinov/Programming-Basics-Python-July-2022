amount = float(input("Enter the amount: "))
first_currency = input("Given currency: ")
second_currency = input("Exchanged currency: ")

firstValue = float
secondValue = float

if first_currency == "BGN":
    firstValue = 1

elif first_currency == "EUR":
    firstValue = 1.95583

elif first_currency == "USD":
    firstValue = 1.79549

elif first_currency == "GBP":
    firstValue = 2.53405

if second_currency == "BGN":
    secondValue = 1

elif second_currency == "EUR":
    secondValue = 1.95583

elif second_currency == "USD":
    secondValue = 1.79549

elif second_currency == "GBP":
    secondValue = 2.53405

exchanged_amount = amount * (firstValue / secondValue)
print('%.2f' % exchanged_amount)