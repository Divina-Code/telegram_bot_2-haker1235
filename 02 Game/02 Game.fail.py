myFile = open("first.txt", 'w')
myFile.write("\nВы попали в игру, каждый ход у вас будет выбор, что бы принять первый вариант нажимайте [1], что бы принять второй нажимайте[2]. Цель игры найти 2 предмета в доме и сбежать из него. Вы хотите начать игру?")
myFile.close()

myFile = open("first.txt")
print(myFile.read())
myFile.close()



myFile1 = open("second.txt", 'w')
myFile1.write("\nВы попали в дом, в нём 5 комнат, в двух лежат нужные вам предметы, а именно ключ от дома и фонарик, в трёх других находятся монстры. Напишите номер комнаты в которую вы хотите войти [1], [2], [3], [4], [5]")
myFile1.close()

myFile1 = open("second.txt")
print(myFile1.read())
myFile1.close()



myFile2 = open("1 room.txt", 'w')
myFile2.write("\nВы ошиблись комнатой. Вас съел монстр(")
myFile2.close()

myFile2 = open("1 room.txt")
print(myFile2.read())
myFile2.close()



myFile3 = open("2 room.txt", 'w')
myFile3.write("\nВы угадали комнату и получаете фонарик")
myFile3.close()

myFile3 = open("2 room.txt")
print(myFile3.read())
myFile3.close()



myFile4 = open("3 room.txt", 'w')
myFile4.write("\nВы ошиблись комнатой. Вас съел монстр(")
myFile4.close()

myFile4 = open("3 room.txt")
print(myFile4.read())
myFile4.close()



myFile5 = open("4 room.txt", 'w')
myFile5.write("\nВы ошиблись комнатой. Вас съел монстр(")
myFile5.close()

myFile5 = open("4 room.txt")
print(myFile5.read())
myFile5.close()



myFile6 = open("5 room.txt", 'w')
myFile6.write("\nВы угадали комнату и получаете ключ")
myFile6.close()

myFile6 = open("5 room.txt")
print(myFile6.read())
myFile6.close()
