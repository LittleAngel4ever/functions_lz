def sum_of_digits(a):                          #Функция для нахождения суммы цифр числа
    a_1 = list(a)

    for i in range (0, len(a_1)):
        a_1[i] = int(a_1[i])
    summ = 0

    for i in a_1:
        summ = summ + i
    return summ


def main():
    print("Введите число для поиска суммы его цифр: ") #Вводим число для поиска суммы
    number = input()
    summ = sum_of_digits(number)                                  #Используем функции
    print("Сумма цифр данного числа:", summ)            #Выводим результат


main()