def sign_of_numbers(num):
    if num > 0:
        print('The number {} is positive.'.format(num))
    elif num < 0:
        print('The number {} is negative.'.format(num))
    else:
        print('The number {} is zero.'.format(num))

num = int(input())

sign_of_numbers(num)