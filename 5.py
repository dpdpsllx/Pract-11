n = int(input())

#Множество всех чисел от 2 до n-1
numbers = set(range(2, n))

#Проходим по возможным делителям
for i in range(2, int(n ** 0.5) + 1):
    if i in numbers:
        #Удаляем все кратные i
        numbers -= set(range(i * i, n, i))

# Вывод элементв списка по отдельности
print(*sorted(numbers))
