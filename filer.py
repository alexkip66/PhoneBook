#  Чтение списка контактов из файла вариант 1
#  Список контактов сохраняется в массиве
def read_first_var():
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        record = []
        for line in data_first:
            if line not in ["","\n"]:
                record.append(line.replace("\n", ""))
            else:
                data_first_list.append(record)
                record = []                
    return data_first_list



#  Чтение списка контактов из файла вариант 2
#  Список контактов сохраняется в массиве
def read_second_var():
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        data_second_list = []
        for line in data_second:
            data_second_list.append(line.replace("\n", "").split(";"))
    return data_second_list



#  Запись списка контактов в файл вариант 1
#  Список контактов хранится в массиве
def write_first_var(data):
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for record in data:
            for field in record:
                f.write(str(field)+"\n")
            f.write("\n")
    f.close()



#  Запись списка контактов в файл вариант 2
#  Список контактов хранится в массиве
def write_second_var(data):
    with open("data_second_variant.csv", "w", encoding="utf-8") as f:
        for record in data:
            f.write(";".join(record)+"\n")
    f.close()
    pass


