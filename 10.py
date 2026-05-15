def three_sum(nums):
    """
    Находит все уникальные тройки в массиве, сумма которых равна нулю.

    Args:
        nums: список целых чисел

    Returns:
        Список уникальных троек [a, b, c], где a + b + c == 0
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Пропускаем дубликаты для первого элемента тройки
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Пропускаем дубликаты для второго элемента
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Пропускаем дубликаты для третьего элемента
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result



# Примеры использования
print(three_sum([-1, 0, 1, 2, -1, -4]))       # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 1, 1]))                   # []
print(three_sum([0, 0, 0]))                   # [[0, 0, 0]]
