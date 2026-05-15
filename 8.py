from itertools import combinations

def get_all_subsets():
    """Получает список всех подмножеств для заданного множества чисел."""
    numbers = list(map(int, input().split()))
    subsets = []

    #Перебираем размеры подмножеств
    for r in range(len(numbers) + 1):
        #Dсе комбинации длины r создаем
        for subset in combinations(numbers, r):
            subsets.append(list(subset))

    return subsets

#Получаем все подмножества
all_subsets = get_all_subsets()
for subset in all_subsets:
    print(' '.join(map(str, subset)))
