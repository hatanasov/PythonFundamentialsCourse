triangle_size = int(input())

def print_line(start, end):
    for num in range(start, end + 1):
        print(num, end=' ')
    print()


def print_triangles(end):
    for num in range(1, end + 1):
        print_line(1, num)
    for num in range(end - 1, 0, -1):
        print_line(1, num)

print_triangles(triangle_size)
