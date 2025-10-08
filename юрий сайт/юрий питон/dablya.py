def circle_area(radius):
    pi = 3.14
    return pi * radius ** 2


def max_of_three(a, b, c):
    return max(a, b, c)


radius = float(input("введите радиус круга: "))
area = circle_area(radius)
print(f"площадь круга с радиусом {radius}: {area:.2f}")


a = int(input("введите 1 число: "))
b = int(input("введите 2 число: "))
c = int(input("введите 3 число: "))


largest_number = max_of_three(a, b, c)
print(f"максимальное из введенных чисел ({a}, {b}, {c}): {largest_number}")