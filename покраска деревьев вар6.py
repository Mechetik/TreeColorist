P, V = map(int, input().split(" "))  #ввод для Васи
Q, M = map(int, input().split(" "))  #ввод для Маши
Trees_quantity = 0
a1, b1 = P - V, P + V                # перевод участков в отрезки
a2, b2 = Q - M, Q + M
if a1 > a2:                          #нахождение самого левого дерева
    a1, b1, a2, b2 = a2, b2, a1, b1  # делаем так что Вася всегда слева

if (a2 > b1):  # отрезки не соприкасаются
    Trees_quantity = (b1-a1) + (b2-a2) + 2
else:  # проверка на пересечение или соприкосновение концами
    Trees_quantity = (max(b1,b2) - a1) + 1

print(Trees_quantity)
