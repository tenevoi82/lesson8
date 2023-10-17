def get_base_from_file_1():
    base = list()
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.read()
        words = data.split("\n")
        i = 0
        while i < len(words) // 5:
            human = {
                "name": words[i * 5],
                "surname": words[i * 5 + 1],
                "phone": words[i * 5 + 2],
                "address": words[i * 5 + 3],
                "index":i,
            }
            i += 1
            base.append(human)
    return base

def get_base_from_file_2():
    base = list()
    index = 0
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                continue
            else:
                line = line[0:-1]  # удаляем паразитный '\n' в конце строки
                splited_line = line.split(";")
                human = {
                    "name": splited_line[0],
                    "surname": splited_line[1],
                    "phone": splited_line[2],
                    "address": splited_line[3],
                    "index":index
                }
                base.append(human)
                index+=1
    return base

def save_base_to_file_1(base: list):
    with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            for person in base:
                file.write(f"{person['name']}\n" f"{person['surname']}\n" f"{person['phone']}\n" f"{person['address']}\n\n")

def save_base_to_file_2(base: list):
    with open("data_second_variant.csv", "w", encoding="utf-8") as file:
        for person in base:
            file.write(f"{person['name']};{person['surname']};{person['phone']};{person['address']}\n")
        file.write("\n")

def find_data_from_base(base: list, data: str):
    found_persons = list()
    for human in base:
        if str.lower(data) in str.lower(human["surname"]) or str.lower(data) in str.lower(human["name"]):
            found_persons.append(human)
    return found_persons


def print_table_data(
    persons: list, print_headers: bool = False, print_indexes: bool = False):
    if print_headers:
        print("\033[1;33;40m", end="")
        if print_indexes:
            print("INDEX\t\t", end="")
        print("ИМЯ\t\tФАМИЛИЯ\t\tТЕЛЕФОН\t\tАДРЕС", end="")
        print("\033[0m")
    for person in persons:
        if print_indexes:
            print(f"{person['index']}\t\t", end="")
        print(f"{person['name']}\t\t{person['surname']}\t\t{person['phone']}\t\t{person['address']}")

def find_data(print_: bool = False):
    x = input("Введите часть имени или фамилии :")
    base1 = get_base_from_file_1()
    base2 = get_base_from_file_2()
    persons = find_data_from_base(base1, x)
    print(f"\n-----------------------------------------------")
    print(f"Найдено {len(persons)} запись в первом файле.")
    if len(persons) > 0:
        print_table_data(persons,True)


    persons = find_data_from_base(base2, x)
    print(f"\n-----------------------------------------------")
    print(f"Найдено {len(persons)} запись во втором файле.")
    if len(persons) > 0:
        print_table_data(persons,True)