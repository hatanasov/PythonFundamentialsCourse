inp_list = [int(num) for num in input().split()]

inp_list.sort()

for i in range(len(inp_list) - 1):
    print(inp_list[i], ' ', sep=' <=', end='')
print(inp_list[-1])
