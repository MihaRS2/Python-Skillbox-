#Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов, остаток по кредиту и количество денег на еду.
#  После этого рассчитывается зарплата по формуле. Если зарплата больше или равна сумме, которая требуется на кредит и еду, то выводится сообщение: «Часов хватает. Можно отдохнуть».
#  В противном случае: «Часов не хватает. Придётся работать больше!»
Time = int(input("Сколько часов отработали? "))
Credit = int(input("Остаток за кредиты "))
Meal = int(input("Траты на еду "))
Summa_Meal_Credit = Credit + Meal
ZP = 200 * Time / 2 ** 3 + Time
if ZP >+ Summa_Meal_Credit:
    print("Часов хватает.Можно отдохнуть!")
else:
    print("Часов не хватает.Придется работать еще! ")    


