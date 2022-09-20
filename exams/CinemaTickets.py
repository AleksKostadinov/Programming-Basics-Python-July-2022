movie = input()
student = 0
standard = 0
kid = 0
total = 0
while movie != "Finish":
    seats = int(input())
    people = 0
    for _ in range(1, seats + 1):
        ticket = input()
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        elif ticket == "End":
            break
        people += 1
    percent_full_hall = people / seats * 100
    print(f"{movie} - {percent_full_hall:.2f}% full.")
    movie = input()
total = student + standard + kid
print(f"Total tickets: {total}")
percent_student = student / total * 100
print(f"{percent_student:.2f}% student tickets.")
percent_standard = standard / total * 100
print(f"{percent_standard:.2f}% standard tickets.")
percent_kid = kid / total * 100
print(f"{percent_kid:.2f}% kids tickets.")