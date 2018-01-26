list_of_nums = [int(num) for num in input().split()]
multiply_by = int(input())


def multiply_list_by_num(list_numbers, multiply_num):
    for num in list_numbers:
        print(num * multiply_num, end=' ')


multiplyed_list = multiply_list_by_num(list_of_nums, multiply_by)
