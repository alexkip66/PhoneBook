from data_create import name_data, surname_data, phone_data, address_data
from filer import read_first_var, read_second_var, write_first_var, write_second_var


#  Ввод данных 
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"\nВ каком формате записать данные? \n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число "))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name};{surname};{phone};{address}\n")     


#  Печать списков контактов, сохраненных в файлах
def print_data():
    print("Вывожу данные из 1 файла: \n")
    data_first = read_first_var()
    for record in data_first:
        for field in record:
            print(field)
        print()

    print("Вывожу данные из 2 файла: \n")
    data_second = read_second_var()
    for record in data_second:
        print(";".join(record))
    print()



# Поиск контякта
#  Поиск производится по имени и фамилии
def find_data(action, data):
    name_list = list(' '.join(data[i][j] for j in range(2)) for i in range(len(data)))
    match action:
        case 3:
            message = ", который хотите изменить"
        case 4:
            message = ", который хотите удалить"
    contact_for_search = ' '.join(list(input(f"Введите имя и фамилию контакта{message}: ").split()[:2]))
    if contact_for_search in name_list:
        found_index = name_list.index(contact_for_search) 
    else:
        found_index = None
        print("ЗАПИСЬ НЕ НАЙДЕНА!\n")
    return found_index



#  Удаление контакта из выбранного списка и сохранение списка в файле
#  Поиск контакта производится по имени
def delete_data():
    
    def delete(data, index):
        answer = input(f'Вы хотите удалить запись "{";".join(data[index])}"? (y/N) ')
        if answer.lower() == "y":
            data.pop(index)
            print("ЗАПИСЬ УДАЛЕНА!\n")
        return data        
    
    print("Удаляем данные")
    var = int(input(f"\nИз какого файла удалять данные? \n\n"
        f"Выберите 1 или 2 вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число "))    
    
    match var:
        case 1:
            data_first = read_first_var()        
            index_del = find_data(4, data_first)
            if index_del != None:
                data_first = delete(data_first, index_del)
                write_first_var(data_first) 
        case 2:
            data_second = read_second_var()
            index_del = find_data(4, data_second)
            if index_del != None:
                data_second = delete(data_second, index_del)
                write_second_var(data_second) 


#  Редактирование контакта в выбранном списке и сохранение списка в файле
#  Поиск контакта производится по имени и фамилии
def edit_data():
    
    def edit(data, index):
        name = name_data(data[index_edit][0])
        surname = surname_data(data[index_edit][1])
        phone = phone_data(data[index_edit][2])
        address = address_data(data[index_edit][3])
        answer = input(f'Вы хотите сохранить изменения? (Y/n) ')
        if answer.lower() == "y" or answer == '':                
            data[index_edit][0] = name                
            data[index_edit][1] = surname
            data[index_edit][2] = phone
            data[index_edit][3] = address 
            print("ИЗМЕНЕНИЯ СОХРАНЕНЫ!\n")
        return data     
    
    print("Редактируем данные")
    var = int(input(f"\nВ каком файла редактировать данные? \n\n"
        f"Выберите 1 или 2 вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число "))    
    
    match var:
        case 1:
            data_first = read_first_var()
            index_edit = find_data(3, data_first)
            if index_edit != None:
                data_first = edit(data_first, index_edit)
                write_first_var(data_first)         
        case 2:
            data_second = read_second_var()        
            index_edit = find_data(3, data_second)        
            if index_edit != None:
                data_second = edit(data_second, index_edit)             
                write_second_var(data_second)
