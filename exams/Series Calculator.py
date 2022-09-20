serial = input()
n_seasons = int(input())
n_episodes = int(input())
time_per_episode = float(input())

time_per_episode *= 1.2
special_episodes = n_seasons * 10
total_minutes = n_seasons * n_episodes * time_per_episode + special_episodes

print(f"Total time needed to watch the {serial} series is {int(total_minutes)} minutes.")
