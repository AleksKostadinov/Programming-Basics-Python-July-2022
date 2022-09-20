height = int(input())
count = 0
unsuccessful = 0
starting_height = height - 30
while True:
    jump = int(input())
    count += 1
    if jump > starting_height:
        if starting_height == height:
            print(f"Tihomir succeeded, he jumped over {starting_height}cm after {count} jumps.")
            break
        starting_height += 5
        unsuccessful = 0
    else:
        unsuccessful += 1
        if unsuccessful == 3:
            print(f"Tihomir failed at {starting_height}cm after {count} jumps.")
            break