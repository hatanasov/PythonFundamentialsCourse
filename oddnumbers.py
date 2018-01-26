collect_of_nums = [int(num) for num in input().split()]

for index, num in enumerate(collect_of_nums):
    if index % 2 ==1 and num % 2 ==1:
        print('Index {} -> {}'.format(index, num))
