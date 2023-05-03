def print_rectangle(width, height, symbol):
    rectangle = []
    for i in range(height):
        row = []
        for j in range(width):
            row += symbol
            print(symbol, end='')
        rectangle.append(row)
        print()

    return rectangle

print_rectangle(12, 4, '@')
