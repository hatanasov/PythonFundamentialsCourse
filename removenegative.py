digits = [int(dig) for dig in input().split()]

positive_nums = [str(dig) for dig in digits[-1::-1] if dig > 0]

if not positive_nums:
    print('empty')
else:
    print(' '.join(positive_nums))