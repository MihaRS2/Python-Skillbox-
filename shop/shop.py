#Сделайте программу, которая получает на вход количество денег. Сыр стоит 60 рублей, мороженое — 20 рублей. Если денег на сыр хватает (больше либо равно), то:
#Выводите сообщение: «На сыр денег хватило», — и вычитайте стоимость сыра из кошелька.
#Если оставшихся денег хватает на мороженое, то выводите: «И на мороженое тоже!». Иначе выводите: «Денег маловато».
bank = int(input("Сколько у вас денег?: "))
cheese = 60
ice_cream = 20
if bank >= cheese:
    bank -= 60
    print("Денег на сыр хватило")
    if bank >= ice_cream:
        bank -= 20
        print("И на мороженное тоже!")
        print(("Осталость") + " " + str(bank) + " " + "рублей")
    else:
        print("На мороженное не хватило")
        print("У вас осталось" + " " + str(bank) + " " + "рублей")
else:
    print("Не хватет денег")
    print("У вас всего" + ' ' + str(bank) + ' ' + "рублей")        
       

