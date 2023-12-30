from logger import input_data, print_data, edit_data, delete_data

#  Главное меню программы
def interface():
    command = 1
    
    while command > 0:
        print(
            "ГЛАВНОЕ МЕНЮ \n",
            "1 - Просмотр данных \n",
            "2 - Ввод данных \n",
            "3 - Изменение данных \n",
            "4 - Удаление данных \n",
            "0 - Завершение работы",
        )
        command = int(input("\nВведите число: "))

        while command < 0 or command > 4:
            print("Неправильный ввод!")
            command = int(input("Введите число: "))


        match command:
            case 1:
                print_data()
            case 2:
                input_data()
            case 3:
                edit_data()
            case 4:
                delete_data()
            case 0:
                pass

