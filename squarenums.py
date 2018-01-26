import math

inp_list = [int(num) for num in input().split()]

squared_nums = []

for num in inp_list:
    if num > 0:
        if math.sqrt(num) == int(math.sqrt(num)):
            squared_nums.append(num)

squared_nums.sort(reverse=True)

print(*squared_nums)



