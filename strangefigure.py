number = int(input())

def print_header(number):
    print('-' * 2 * number)


def print_middle(number):
    count = number - 2
    while count > 0:
        print('-', end='')
        for i in range(1, number):
            print('\/', end='')
        print('-', end='\n')
        count -= 1

print_header(number)
print_middle(number)
print_header(number)