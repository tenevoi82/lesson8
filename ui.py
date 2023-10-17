from logger import input_data, print_data, find_data, edit_data

def interface():
    print("Добрый день! Это бот-помощник. \n"
          "Что выхотите сделать?\n"
          "1 - Записать данные \n"
          "2 - Вывести данные\n"
          "3 - Найти по фамилии или имени\n"
          "4 - Изменить или Удалить"
          )
    command = int(input("Ваш выбор: "))

    while command < 1 or command > 4:
        command = int(input("Ошибка! Ваш выбор: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        find_data()
    elif command == 4:
        edit_data()