def input_user_data():
    name = input("Введите имя: ") 
    surname = input("Введите фамилию: ") 
    phone = input("Введите телефон: ") 
    adress = input("Введите адрес: ") 
    return name, surname, phone, adress

def edit_user_data(old_data):
    name = input(f"Введите имя [{old_data['name']}]: ") 
    surname = input(f"Введите фамилию [{old_data['surname']}]: ") 
    phone = input(f"Введите телефон [{old_data['phone']}]: ") 
    address = input(f"Введите адрес [{old_data['address']}]: ") 

    if(name != ""): old_data['name'] = name
    if(surname != ""): old_data['surname'] = name
    if(phone != ""): old_data['phone'] = name
    if(address != ""): old_data['address'] = name

    return old_data
