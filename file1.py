# Вводятся 2 числа a, b. Найти сумму чисел в даиапозоне от a до b включительно
x = 2
y = 10
res = 0
for i in range(x, y + 1, 1):
    res = res + i
print(res)
