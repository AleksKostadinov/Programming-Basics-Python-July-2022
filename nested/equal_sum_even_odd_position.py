start = int(input())
end = int(input())
for number in range(start, end + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for j in range(len(number_to_str)):
        digit = int(number_to_str[j])
        if j % 2:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(number_to_str, end=" ")