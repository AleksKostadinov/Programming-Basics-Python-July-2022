number = float(input())

while number >= 0:
  double_number = number * 2
  print(f"Result: {double_number:.2f}")
  number = float(input())
else:
  print("Negative number!")