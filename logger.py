from data_create import name_data, surname_data, phone_data, address_data
from filer import read_first_var, read_second_var, write_first_var, write_second_var


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
            f.write(f"{name};{surname};{phone};{address}\n\n")     


def print_data():
    print("Вывожу данные из 1 файла: \n")
    # with open("data_first_variant.csv", "r", encoding="utf-8") as f:
    #     data_first = f.readlines()
    #     print(*data_first,"\n")
    #     # data_first_list = []
    #     # j = 0
    #     # for i in range(len(data_first)):
    #     #     if data_first[i] == "\n" or i == len(data_first) - 1:
    #     #         data_first_list.append("".join(data_first[j:i+1]))
    #     #         j = i
    #     # print(*data_first_list,"\n")
    data_first = read_first_var()
    for record in data_first:
        for field in record:
            print(field)
        print()


    print("Вывожу данные из 2 файла: \n")
    # with open("data_second_variant.csv", "r", encoding="utf-8") as f:
    #     data_second = f.readlines()
    #     print(*data_second,"\n")
    data_second = read_second_var()
    for record in data_second:
        print(";".join(record))
    print()




def delete_data():
    print("Удаляем данные")
    var = int(input(f"\nИз какого файла удалять данные? \n\n"
        f"Выберите 1 или 2 вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число "))    
    
    match var:
        case 1:
            data_first = read_first_var()
            name_to_del = input("Введите имя контакта, который хотите удалить: ")
            name_list = list(data_first[i][0] for i in range(len(data_first)))
            if name_to_del in name_list:
                index_del = name_list.index(name_to_del)
                answer = input(f'Вы хотите удалить запись "{";".join(data_first[index_del])}"? (y/N) ')
                if answer.lower() == "y":
                    data_first.pop(index_del)
                    print("ЗАПИСЬ УДАЛЕНА!\n")
                    write_first_var(data_first) 
            else:
                print("КОНТАКТ НЕ НАЙДЕН!/n")           
        case 2:
            data_second = read_second_var()
            name_to_del = input("Введите имя контакта, который хотите удалить: ")
            name_list = list(data_second[i][0] for i in range(len(data_second)))
            if name_to_del in name_list:
                index_del = name_list.index(name_to_del)
                answer = input(f'Вы хотите удалить запись "{";".join(data_second[index_del])}"? (y/N) ')
                if answer.lower() == "y":
                    data_second.pop(index_del)
                    print("ЗАПИСЬ УДАЛЕНА!\n")
                    write_second_var(data_second) 
            else:
                print("КОНТАКТ НЕ НАЙДЕН!\n")   



def edit_data():
    print("Редактируем данные")
    var = int(input(f"\nВ каком файла редактировать данные? \n\n"
        f"Выберите 1 или 2 вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input("Введите число "))    
    
    match var:
        case 1:
            data_first = read_first_var()
            name_to_edit = input("Введите имя контакта, который хотите изменить: ")
            name_list = list(data_first[i][0] for i in range(len(data_first)))
            if name_to_edit in name_list:
                index_edit = name_list.index(name_to_edit)
                name = name_data(data_first[index_edit][0])
                surname = surname_data(data_first[index_edit][1])
                phone = phone_data(data_first[index_edit][2])
                address = address_data(data_first[index_edit][3])
                answer = input(f'Вы хотите сохранить изменения? (Y/n) ')
                if answer.lower() == "y" or answer == '':                
                    data_first[index_edit][0] = name                
                    data_first[index_edit][1] = surname
                    data_first[index_edit][2] = phone
                    data_first[index_edit][3] = address 
                    print("ИЗМЕНЕНИЯ СОХРАНЕНЫ!\n")                
                    write_first_var(data_first) 
            else:
                print("КОНТАКТ НЕ НАЙДЕН!\n")               
        case 2:
            data_second = read_second_var()
            name_to_edit = input("Введите имя контакта, который хотите удалить: ")
            name_list = list(data_second[i][0] for i in range(len(data_second)))
            if name_to_edit in name_list:
                index_edit = name_list.index(name_to_edit)
                name = name_data(data_second[index_edit][0])
                surname = surname_data(data_second[index_edit][1])
                phone = phone_data(data_second[index_edit][2])
                address = address_data(data_second[index_edit][3])
                answer = input(f'Вы хотите сохранить изменения? (Y/n) ')
                if answer.lower() == "y" or answer == '':                
                    data_second[index_edit][0] = name                
                    data_second[index_edit][1] = surname
                    data_second[index_edit][2] = phone
                    data_second[index_edit][3] = address  
                    print("ИЗМЕНЕНИЯ СОХРАНЕНЫ!\n")                   
                    write_second_var(data_second)  
            else:
                print("КОНТАКТ НЕ НАЙДЕН!\n")    

# print_data()
