from math import pi

def square_of_circle(a):        #Функция для поиска площади
    square=a * a * pi
    return square

def lenght_of_circle(a):        #Функция поиска длины
    lenght=2 * a* pi
    return lenght

def main():
    print("Введите радиус: ") #Ввод
    R = input()
    radius = int(R)
    square = square_of_circle(radius)             #Использовние функций
    lenght = lenght_of_circle(radius)
    print("Длина этой окружности:", lenght)    #Вывод
    print("Площадь этой окружности:", square)

main()