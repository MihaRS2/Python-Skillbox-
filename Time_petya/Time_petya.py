#Петя писал таймер для телефона, но у него что-то пошло не так.

#ount = 0
#While count <= 10
 #if count == 0:
   #print('Время вышло!')
 #else:
   #print(count)
   #count -= 1


count = 10
while count >= 0:
    print(count)
    count -= 1
count = 0
while count <= 10:
 if count == 0:
    count -= 1
    print('Время вышло!')
    break #Чтобы не цыклилось
else:
   print(count)
   