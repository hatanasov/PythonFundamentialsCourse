lists_of_nums = [num for num in input().split('|')]
result = [num for i in lists_of_nums[-1::-1] for num in i.split()]
for i in result:
    print(i, end=' ')


# for i in lists_of_nums[-1::-1]:
#     for num in i.split():
#         print(num, end=' ')
