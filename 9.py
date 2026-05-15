from itertools import combinations

numbers = list(map(int, input().split()))
k = int(input())

#Получаем все k-элементные подмножества
subsets = combinations(numbers, k)

#Вывод каждоно подмножества
for subset in subsets:
    print(' '.join(map(str, subset)))
