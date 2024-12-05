def temp(tc):
    for i in range(tc):
        tf = (9 / 5) * tc + 32
    return tf
 
def main():
    tc = int(input('Введите температуру по Цельсию: '))
    while tc >= -273:
        tf = temp(tc)
        print('Температура Цельсия', tc, 'равна', tf, 'градусам Фаренгейта.')
 
 
main()