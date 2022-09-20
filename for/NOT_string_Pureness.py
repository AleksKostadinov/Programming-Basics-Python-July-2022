num = int(input())

for i in range(1, num + 1):
    text = input()
    for j in range(len(text)):
        if text.find('.') != -1:
            print(f"{text} is not pure!")
            break
        elif text.find('_') != -1:
            print(f"{text} is not pure!")
            break
        elif text.find(',') != -1:
            print(f"{text} is not pure!")
            break
        else:
            print(f"{text} is pure.")
            break