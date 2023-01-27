chair = int(input("Ведите стоимость стульев : "))
table = int(input("Введите стоимость стола : "))
closet = int(input("Введите стоимость шкафа : "))
summa = chair + table + closet
discount = summa * 10 /100
if summa > 10000:
  summa = summa - discount
  print("Стоимость с учетом скидки 10% : ",summa )
else:
  print("Стоимость покупки : ",summa)
