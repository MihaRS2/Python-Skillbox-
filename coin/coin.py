#Напишите программу, которая принимает на вход вес трёх монет (две одинаковые, третья меньше) и определяет, какая из них легче.
coin_1 = int(input("Введите вес монеты 1: "))
coin_2 = int(input("Введите вес монеты 2: "))
coin_3 = int(input("Введите вес монеты 3: "))
if coin_1 == coin_2:
    print("Третья монета легче ")
elif coin_1 > coin_2:
    print("Первая монета легче")
else:
    print("Вторая монета легче")