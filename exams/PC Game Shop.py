n = int(input())
count_Hearthstone = 0
count_Fornite = 0
count_Overwatch = 0
count_Others = 0
for i in range(1, n + 1):
    game = input()
    if game == "Hearthstone":
        count_Hearthstone += 1
    elif game == "Fornite":
        count_Fornite += 1
    elif game == "Overwatch":
        count_Overwatch += 1
    else:
        count_Others += 1
perc_Hearthstone = (count_Hearthstone / n) * 100
perc_Fornite = (count_Fornite / n) * 100
perc_Overwatch = (count_Overwatch / n) * 100
perc_Others = (count_Others / n) * 100
print(f"Hearthstone - {perc_Hearthstone:.2f}%")
print(f"Fornite - {perc_Fornite:.2f}%")
print(f"Overwatch - {perc_Overwatch:.2f}%")
print(f"Others - {perc_Others:.2f}%")
