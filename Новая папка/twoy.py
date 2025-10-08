counter = 0
answer = input("как зовут твою маму =")
if answer == "никита" or answer == "никита":
    print ("Молодец теперь ты знаешь как зовут твою маму +балл")
    counter += 1
elif answer == "сам ты лох":
    print("а ловко ты это придумал я сначала даже не и понял")
    counter += 1
else:
    print("Неправильно ты лох")
    print(f"у тебя {counter} баллов" )

    answer = input( "какой твой любимый брейнрот ")
    if answer == "тралалело" or answer == "тун тун сахур":
        print("хороший брейнрот + 1 балл")
        counter += 1
    elif answer== "бр бр патапим":
        print ("струя бобра")
        counter -= 1
    else:
        print("а я люблю тун тун сахура и тралалело")
        print(f"у тебя {counter} баллов")