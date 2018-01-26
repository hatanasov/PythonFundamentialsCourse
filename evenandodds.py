number = input()


def sum_evens(lsit_of_digits):
    result = 0
    for num in lsit_of_digits:
        if num % 2 == 0:
            result += num
    return result


def sum_odds(lsit_of_digits):
    result = 0
    for num in lsit_of_digits:
        if num % 2 == 1:
            result += num
    return result


def even_by_odds(digit):
    """digit must be type 'str'."""
    if '-' in digit:
        digit = digit[1:]
    list_of_numbers = [int(num) for num in digit]
    evens = sum_evens(list_of_numbers)
    odds = sum_odds(list_of_numbers)
    return evens * odds


result = even_by_odds(number)
print(result)
