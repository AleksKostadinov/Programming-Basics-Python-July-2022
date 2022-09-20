movie = input()
count = 0
max_points = -1
best_movie = ""
while movie != "STOP":
    points = 0
    length = len(movie)
    count += 1
    for i in movie:
        points += ord(i)
        if i.islower():
            points -= 2 * length
        elif i.isupper():
            points -= length
    if points > max_points:
        max_points = points
        best_movie = movie
    if count == 7:
        print(f"The limit is reached.")
        break
    movie = input()

print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")