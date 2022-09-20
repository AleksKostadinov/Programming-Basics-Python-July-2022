rent = int(input())

statues = rent * 0.7
catering = statues * 0.85
music = catering * 0.5
total = rent + statues + catering + music

print(f"{total:.2f}")
