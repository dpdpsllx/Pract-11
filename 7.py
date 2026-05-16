from itertools import permutations

numbers = input().split()

numbers.sort()

for p in permutations(numbers):
    print(*p)
