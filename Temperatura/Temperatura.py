#Напишите программу, которая запрашивает у пользователя температуру, и, если она меньше нуля или больше 100, то выводится сообщение об опасности.
temp = int(input("Введите температуру : "))
if temp < 0 or temp > 100:
    print("Внимание опасная температура ! ! ! ")
else:
    print("Все в порядке !")