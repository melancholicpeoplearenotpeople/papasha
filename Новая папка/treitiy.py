age = int(input("введите возраст"))
if age > 0 and age <= 10:
    print("вы ребёнок")
elif age > 10 and age <= 16:
    print("вы подросток")
elif age > 16 and age < 50:
    print("вы взрослый")
elif age >= 50 and age < 120:
     print("вы пожилой человек")
else:
    print("возраст введён не правильно")