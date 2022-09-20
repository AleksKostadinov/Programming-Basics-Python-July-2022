movie = input()
is_limit_reached = False
count = 0
best_movie = ""
max_points = 0
while movie != "STOP":
    count += 1
    total_points = 0
    movie_length = len(movie)
    for index, char in enumerate(movie):
        points = ord(char)
        if char.islower():
            total_points += points - 2 * movie_length
        elif char.isupper():
            total_points += points - movie_length
        else:
            total_points += points
    if total_points > max_points:
        max_points = total_points
        best_movie = movie

    if count == 7:
        is_limit_reached = True
        break

    movie = input()
    if movie == "STOP":
        break
if is_limit_reached:
    print(f"The limit is reached.")
    print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
else:
    print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
