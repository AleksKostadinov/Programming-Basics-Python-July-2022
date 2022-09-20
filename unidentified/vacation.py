budget = float(input())
season = input()
rest = ""
location = ""

if budget <= 1000:
  rest = "Camp"
  if season == "Summer":
    percent_budget = 0.65
    location = "Alaska"
  else:
    percent_budget = 0.45
    location = "Morocco"
elif 1000 < budget <= 3000:
  rest = "Hut"
  if season == "Summer":
    percent_budget = 0.80
    location = "Alaska"
  else:
    percent_budget = 0.60
    location = "Morocco"
else:
  rest = "Hotel"
  if season == "Summer":
    percent_budget = 0.90
    location = "Alaska"
  else:
    percent_budget = 0.90
    location = "Morocco"

price = budget * percent_budget
print(f"{location} - {rest} - {price:.2f}")