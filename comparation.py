inp_type = input()
inp_1 = input()
inp_2 = input()


def check_Grater(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def compare_things(first, second, types):
    if types == 'int':
        first = int(first)
        second = int(second)
        check_Grater(first, second)
    else:
        check_Grater(first, second)

    # try:
    #     first = int(first)
    #     second = int(second)
    # except ValueError:
    #     if type(first) == type(second):
    #         check_Grater(first, second)
    #     else:
    #         first = str(first)
    #         second = str(second)
    #         check_Grater(first, second)
    # else:
    #     check_Grater(first, second)


compare_things(inp_1, inp_2, inp_type)
