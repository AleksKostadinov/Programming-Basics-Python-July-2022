player1 = input()
player2 = input()
command = ""
points_1 = 0
points_2 = 0
command_1 = input()
command_2 = input()
is_number_wars = False
while command != "End of game":

    # if command_1 == "End of game" or command_2 == "End of game":
    #     break

    card_1 = int(command_1)
    card_2 = int(command_2)

    if card_1 > card_2:
        points_1 += card_1 - card_2
    elif card_1 < card_2:
        points_2 += card_2 - card_1
    else:
        card_1 = int(input())
        card_2 = int(input())
        print(f"Number wars!")
        if card_1 > card_2:
            print(f"{player1} is winner with {points_1} points")
            is_number_wars = True
            break
        elif card_1 < card_2:
            print(f"{player2} is winner with {points_2} points")
            is_number_wars = True
            break
    command_1 = input()
    if command_1 == "End of game":
        break
    command_2 = input()

if not is_number_wars:
    print(f"{player1} has {points_1} points")
    print(f"{player2} has {points_2} points")
