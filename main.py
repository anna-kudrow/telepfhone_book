def find_contact():
    searching_data = input('Введите данные для поиска: ')
    with open('data.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if searching_data in line.lower():
                return line   

def add_contact():
    name = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    status = input('Введите статус: ')
    phone_number = input('Введите номер телефона: ')
    contact = ''
    contact = name + ' ' + lastname + ' ' + status + ' ' + phone_number + '\n'
    phone_book = open('data.txt', 'a', encoding='UTF-8')
    phone_book.write(contact)
    phone_book.close()   
    print(f'Контакт сохранён!')  
    print()
    print()

def delete_contact():
    delete_it = input('Введите данные контакта для удаления: ')
    with open('data.txt', 'w', encoding='UTF-8') as file:
        for line in file:
            if delete_it in line.lower():
                print(line)
                question = int(input('Точно хотите удалить этот контакт? 1 - да/ 2 - нет: '))
                if question == 1:
                    line.split().clear()
                    print('Контакт удалён!')
            else:
                print('Нет такого контакта')    
                
                    
def change_contact():
    change_it = input('Введите данные контакта для изменения: ')
    with open('data.txt', 'r+', encoding='UTF-8') as file:
        for line in file:
            if change_it in line:
                add_contact


def show_all_contacts():
    with open('data.txt', 'r', encoding='UTF-8') as file:
        all_contacts = file.readlines()
    return all_contacts    


while True:
    print('МЕНЮ:\nКакое действие выполнить?:\n\t1 - Найти контакт\n\t2 - Добавить контакт\n\t3 - Удалить контакт\n\t4 - Изменить контакт\n\t5 - Показать контакты\n\t6 - Выйти из телефонной книги')
    user_choice = int(input('Введите действие: '))

    if user_choice == 1:
        print(find_contact())

    elif user_choice == 2:
        add_contact()

    elif user_choice == 3:
        delete_contact()

    elif user_choice == 4:
        change_contact()

    elif user_choice == 5:
        print(show_all_contacts())
    elif user_choice == 6:
        print('==================\nДо свидания!\n==================')
        break    
    else:
        print('Вам необходимо выбрать пункт из меню от 1 до 6')







