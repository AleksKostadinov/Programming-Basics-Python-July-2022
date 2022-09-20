n_movies = int(input())
h_rating = 1
l_rating = 10
movie_hr = ""
movie_lr = ""
count_r = 0
for i in range(1, n_movies + 1):
    movie = input()
    rating = float(input())
    count_r += rating
    if rating > h_rating:
        h_rating = rating
        movie_hr = movie
    if rating < l_rating:
        l_rating = rating
        movie_lr = movie
avg_rating = count_r / n_movies

print(f"{movie_hr} is with highest rating: {h_rating:.1f}")
print(f"{movie_lr} is with lowest rating: {l_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")