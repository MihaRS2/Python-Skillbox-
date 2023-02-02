Gazalin = int(input("Введите цену топлива "))
Distance = int(input("Введите растояние "))
fuel_consumption = int(input("Введите средний расход "))
price_1km = fuel_consumption * Gazalin / 100
total_price = Distance * price_1km
Total_consumption = total_price / Gazalin
print("Затраты на топливо: " ,total_price)
print("Потраченное топливо: " ,Total_consumption)
