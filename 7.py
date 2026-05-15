from itertools import permutations

numbers = input().split()

#Сортируем чтобы порядок был лексикографическим как надо
numbers.sort()

#Генерируем перестановки
for p in permutations(numbers):
    print(*p)
