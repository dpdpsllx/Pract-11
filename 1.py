numbers = list(map(int, input().split()))

num = int(input())

# Проверяем, повторяется ли число больше одного раза
if numbers.count(num) > 1:
    print("YES")
else:
    print("NO")
