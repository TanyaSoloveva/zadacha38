from logger import input_data, print_data, delete_data, change_data

def interface(): #Функция интерфейс, здороваемся с пользоватлем
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - заись данных \n 2 - вывод данных \n 3 - измнение данных \n 4 - удаление данных")
    command = int(input('Введите число ')) #принимать данные с консоли в виде числа.
    
    while command != 1 and command != 2 and command != 3 and command !=4: # проверка на правильность ввода числа пользователем
        print("Неправильный ввод")
        command = int(input('Введите число ')) #повторный ввод числа
        
    if command == 1: # ввод данных
        input_data()
    elif command == 2: # вывод данных
        print_data()
    elif command == 3: # изменение данных
        change_data()
    elif command == 4: # удаление данных
        delete_data()  