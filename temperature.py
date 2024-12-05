def temp(tc):
    tf = (9 / 5) * tc + 32
    return tf
 
def main():
    tc = float(input('Введите температуру по Цельсию: '))
    if tc >= -273:
        tf = temp(tc)
    
    print('Температура Цельсия', tc, 'равна', tf, 'градусам Фаренгейта.')


main()