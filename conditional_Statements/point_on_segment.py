first = int(input())
second = int(input())
point = int(input())

left = min(first, second)
right = max(first, second)

distance_left = abs(left - point)
distance_right = abs(right - point)
min_distance = min(distance_left, distance_right)
if left <= point <= right:
    print("in")
else:
    print("out")
print(min_distance)