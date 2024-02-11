from data_create import name_data, surname_data, phone_data, adres_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adres = adres_data()
    var = int (input(f"В каком варианте записать данные?\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adres}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{adres}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2: # проверка на правильность ввода числа пользователем
        print("Неправильный ввод")
        var = int(input('Введите число ')) #повторный ввод числа

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f: #открытие файла1 и запись в него данных
            f.write(f"{name}\n{surname}\n{phone}\n{adres}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f: #открытие файла2 и запись в него данных
            f.write(f"{name};{surname};{phone};{adres}\n\n")
            
        
                
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f: #вывод данных из первого файла
       data_first = f.readlines() #читаем все наши строки
       data_first_list = [] #создадим переменную, где будет храниться итоговый результат
       j = 0
       for i in range(len(data_first)):
           if data_first[i] == '\n' or i == len(data_first) - 1:
               data_first_list.append(''.join(data_first[j:i+1])) #в список data_first дбавляем новую запись
               j = i
    print(''.join(data_first_list))
                
        
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f: #вывод данных из второго файла
       data_second = f.readlines() #читаем все наши строки
       print(*data_second)
    
       
print_data()


# Функция для удаления контакта
def delete_data():
    var = int (input(f"Из какого файла удалить данные?\n\n"
                     f"Выберите вариант: "))
    while var != 1 and var != 2: # проверка на правильность ввода числа пользователем
        print("Неправильный ввод")
        var = int(input('Введите число ')) #повторный ввод числа

    if var == 1:
    #из первого файла
        name = input('Имя кого удаляем: ')
        surname = input('Фамилия кого удаляем: ')
        phone = input('Телефон кого удаляем: ')
        adres = input('Адрес кого удаляем: ')
        
        with open('data_first_variant.csv', "r", encoding="utf-8") as f:
            data = f.readlines()
        with open('data_first_variant.csv', "w", encoding="utf-8") as f:
            for line in data :
                if line.strip("\n") != name and line.strip("\n") != surname and line.strip("\n") != phone and line.strip("\n") != adres:
                    f.write(line) 

    #из второго файла
    elif var == 2:
        data_second = input('Имя;Фамилия;телефон;адрес кого удаляем: ')
        with open('data_second_variant.csv', "r", encoding="utf-8") as f:
            data = f.readlines() 
        with open('data_second_variant.csv', "w", encoding="utf-8") as f:
            for line in data :
                if line.strip("\n") != data_second:
                    f.write(line) 
                

#Функция замены данных
def change_data():
    var = int (input(f"В каком файле заменить данные?\n\n"
                     f"Выберите вариант: "))
    while var != 1 and var != 2: # проверка на правильность ввода числа пользователем
        print("Неправильный ввод")
        var = int(input('Введите число ')) #повторный ввод числа
    if var == 1: #из первого файла 
        old_data = input('Введите данные, которые нужно заменить: ')  # текст, который нужно найти
        new_data = input('Введите новые данные: ')  # текст, на который нужно заменить
        with open('data_first_variant.csv', "r", encoding="utf-8") as f:
            data = f.readlines()
                           
        with open('data_first_variant.csv', "w", encoding="utf-8") as f:
            for line in data:
                line = line.replace(old_data, new_data)
                f.write(line) 

    elif var == 2:#из второго файла
            old_data = input('Имя;Фамилия;телефон;адрес кого удаляем: ')
            new_data = input('Введите новые данные: ')
            with open('data_second_variant.csv', "r", encoding="utf-8") as f:
                data = f.readlines()
           
            with open('data_second_variant.csv', "w", encoding="utf-8") as f:
                for line in data:
                    line = line.replace(old_data, new_data)
                    f.write(line) 