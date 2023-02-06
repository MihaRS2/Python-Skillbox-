bags = int(input("Сколько мешков?: "))
bags_count = 0
total_weigth = 0
while bags_count < bags:
    weigth = int(input('Сколько весит мешок '))
    total_weigth += weigth
    bags_count += 1
print('Общий вес мешков', total_weigth)