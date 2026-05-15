set1 = set(input().split())
set2 = set(input().split())

#Ввод числа для провереи
x = input().strip()

#Проверка принадлежности к пересечению
if x in (set1 & set2):
    print("YES")
else:
    print("NO")
