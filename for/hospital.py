period = int(input())
doctors = 7
treated = 0
untreated = 0

for days in range(1, period + 1):
    patients = int(input())

    if days % 3 == 0:
        if untreated > treated:
            doctors += 1

    if patients <= doctors:
        treated += patients
    else:
        treated += doctors
        untreated += (patients - doctors)

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")