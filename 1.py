numbers = list(map(int, input().split()))
num = int(input())

dubbles = set(x for x in numbers if numbers.count(x) > 1)

if num in dubbles:
    print("YES")
else:
    print("NO")
