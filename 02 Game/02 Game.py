
myFile = open("first.txt") #приветствие игрока
print(myFile.read())
myFile.close()
answer1 = input()

if answer1 == '1':

    life = 1 # жив ли игрок
    items = 0 # количество нужных предметов, которыми обладает игрок
    print("У тебя есть жизней -", life, "предметов -", items, )
    myFile1 = open("second.txt")
    print(myFile1.read())
    myFile1.close()
    answer2 = input()

    while life:

        if answer2 == '1':
            myFile2 = open("1 room.txt")
            print(myFile2.read())
            myFile2.close()
            life = 0
            print("Вы проиграли")
        elif answer2 == '2':
            myFile3 = open("2 room.txt")
            print(myFile3.read())
            myFile3.close()
            items = 1
            print("У вас есть один предмет, вам нужен второй")
            life = 1
        elif answer2 == '3':
            myFile4 = open("3 room.txt")
            print(myFile4.read())
            myFile4.close()
            life = 0
            print("вы проиграли")
        elif answer2 == '4':
            myFile5 = open("4 room.txt")
            print(myFile5.read())
            myFile5.close()
            life = 0
            print("Вы проиграли")
        elif answer2 == '5':
            myFile6 = open("5 room.txt")
            print(myFile6.read())
            myFile6.close()
            items = 2
            print("Вы выиграли")
            life = 0

