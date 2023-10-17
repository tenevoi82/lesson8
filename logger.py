from data_create import input_user_data, edit_user_data
from base import *
import os

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(
        input(
            f"\nВ каком формате записать данные?\n"
            f"1 Вариант:\n"
            f"{name}\n"
            f"{surname}\n"
            f"{phone}\n"
            f"{adress}\n\n"
            f"2 Вариант:\n"
            f"{name};{surname};{phone};{adress}\n\n"
            f"\nВаш выбор: "
        )
    )
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name}\n" f"{surname}\n" f"{phone}\n" f"{adress}\n\n")
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name};{surname};{phone};{adress}\n\n")


def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != "\n":
                print(i, end="")


def edit_data():    
    num_of_file = int(input("Какой файл будем редактировать? Введите 1 или 2: "))
    while (num_of_file > 0 and num_of_file > 2 ):
        print("\033[1;31;40mОшибка!\033[0m")
        num_of_file = int(input("Какой файл будем редактировать? Введите 1 или 2: "))
    base = None
    if(num_of_file == 1):
        base = get_base_from_file_1()
    elif(num_of_file == 2):
        base = get_base_from_file_2()
    print_table_data(base,True,True)

    
    while (True):
        print("Для удаления записи введите D и номер записи через пробел, например для удаления записи номер 3 введите 'D 3'\n"
            "Для редактирования записи введите E и номер записи через пробел, например для редактирования записи номер 5 введите E 5")
        command_str =str(input(":")).lower()
        cmd = command_str.split(' ')[0]
        row = int(command_str.split(' ')[1])

        if(cmd != 'd' and cmd != 'e'):
            print("\033[1;31;40mОшибка! команда может быть тлько D или E\033[0m")
        elif(row < 0 or row > len(base)):
            print("\033[1;31;40mОшибка! Неправильно заданный номер записи\033[0m")
        else:
            break

    if(command_str.split()[0]=='d'):
        print(f"Удалить запись:{base[row]} ?",end='')
        if(input("y/n:").lower()=='y'):
            base.remove(base[row])
    elif(command_str.split()[0]=='e'):
        print("Подсказка: если не вводить данные, а просто нажать ENTER то в поле сохраниться старая запись.")
        base[row] = edit_user_data(base[row])
    print("Результат изменений:")
    print_table_data(base,True,True)
    if(input("Сохранить результат? y/n:").lower()=='y'):
        if num_of_file == 1 : save_base_to_file_1(base)
        else : save_base_to_file_2(base)

