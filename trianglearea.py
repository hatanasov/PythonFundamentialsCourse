base = float(input())
height = float(input())


def get_triangle_area(base, height):
    return (base * height) / 2


def main():
    area = get_triangle_area(base, height)
    return area


# area = main()

# print(f'{area:.12g}')

if __name__ == '__main__':
    area = main()
    print(f'{area:.12g}')
