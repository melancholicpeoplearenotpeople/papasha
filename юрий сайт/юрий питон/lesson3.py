length1 = 5
width1 = 3
area = length1 * width1
print(f"Площадь комнаты: {area}")

length2 = 7
width2 = 4
area2 = length1 * width1
print(f"Площадь комнаты: {area2}")

def ploshad(lenght, width):
    area2 = length1 * width1
    return area

area = ploshad(5,3)
print(f"Площадь подсчитанная через функцию: {area}")

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
if is_adult(20):
    print("Доступ разрешен")
else:
    print("Катись от сюда малой))")






def circle_area(radius):
    pi = 3.14
    squared_radius = radius ** 2
    area = pi * squared_radius
    return area

result = circle_area(5)
print(result)