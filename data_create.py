def name_data(old_name=''):
    name = input(f"Введите Ваше имя{' ('+old_name+')' if old_name != '' else ''}: ").capitalize()
    print("Очень красивое имя!")
    if name == '': name = old_name
    return name


def surname_data(old_surname=''):
    surname = input(f"Введите Вашу фамилию{' ('+old_surname+')' if old_surname != '' else ''}: ").capitalize()
    if surname == '': surname = old_surname
    return surname


def phone_data(old_phone=''):
    phone = input(f"Введите Ваш телефон{' ('+old_phone+')' if old_phone != '' else ''}: ")
    if phone == '': phone = old_phone
    return phone


def address_data(old_address=''):
    address = input(f"Введите Ваш адрес{' ('+old_address+')' if old_address != '' else ''}: ").capitalize()
    if address == '': address = old_address
    return address