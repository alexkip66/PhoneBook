def read_first_var():
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        # print(*data_first,"\n")
        data_first_list = []
        record = []
        for line in data_first:
            if line not in ["","\n"]:   #!= "\n" and line != "":
                record.append(line.replace("\n", ""))
            else:
                data_first_list.append(record)
                record = []                
    return data_first_list



def read_second_var():
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        # print(*data_second,"\n")
        data_second_list = []
        for line in data_second:
            data_second_list.append(line.replace("\n", "").split(";"))
    return data_second_list



def write_first_var(data):
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for record in data:
            for field in record:
                f.write(str(field)+"\n")
            f.write("\n")
    f.close()




def write_second_var(data):
    with open("data_second_variant.csv", "w", encoding="utf-8") as f:
        for record in data:
            f.write(";".join(record)+"\n")
    f.close()
    pass


