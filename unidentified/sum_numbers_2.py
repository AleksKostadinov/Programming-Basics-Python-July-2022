#from sys import maxsize
loops = int(input("Amount of loops: "))
sum = 0

#bigger_lis = -maxsize

for i in range(loops):
    lis = int(input("Input: "))
    sum += lis
print(sum)

#if lis > bigger_lis:
    #print(f"\n{lis} is the biggest!")