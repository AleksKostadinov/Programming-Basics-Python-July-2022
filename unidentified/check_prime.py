from math import sqrt
n = int(input())
is_prime = True
for i in range(2, int(sqrt(n)) + 1):

    if n % i == 0:
        is_prime = False
        break
if n <= 1:
    is_prime = False
if is_prime:
    print("Prime")
else:
    print("Not prime")