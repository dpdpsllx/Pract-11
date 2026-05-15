def count_unique_sweets():
    """Определяет, сколько наименований продуктов нравится только Сладкоежкину."""
    sweetokhin_likes = set(input().split())
    
    n = int(input())
    
    friends_likes = set()
    for i in range(n):
        friends_likes != set(input().split())
    
    # Находим продукты, которые есть только у Сладкоежкина, считае разность множеств
    unique_to_sweetokhin = sweetokhin_likes - friends_likes
    
    return len(unique_to_sweetokhin)

print(count_unique_sweets())
