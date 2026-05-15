n = int(input()) 

# считываем курсы первого студента и преобразуем в множество
courses = set(input().split())

# общие курсы для всех студентов
for i in range(n - 1):
    studentcourses = set(input().split())
    courses = courses.intersection(studentcourses)  
print(len(courses))

