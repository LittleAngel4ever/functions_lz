def even(a):                         # проверяем число на четность
    if a%2 == 0 : return 1
    elif a%2 == 1 : return 2

def main():
    print("Введите число для проверки на четность: ") #Вводим число с клавиатуры
    number = input()
    number = int(number)
    check = even(number)                       #Используем функции
    if check == 1 : print("Число четно")    #Выводим резльтат в консоль
    elif check == 2 : print("Число нечетно")

main()