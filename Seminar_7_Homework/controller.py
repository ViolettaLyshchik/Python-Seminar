
from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data


def greeting():
    print("Здравствуйте!")

def input_data():
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    phone_number = input("Контактный телефон: ")
    note = input("Примечание: ")
    return [last_name, first_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Выбор действия:\n\
    введите 1 если хотите добавить контакт;\n\
    введите 2 для экспорта контакта;\n\
    введите 3 для поиска контакта.")
    num = input("Введите цифру: ")
    if num == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif num == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Конакт не найден")