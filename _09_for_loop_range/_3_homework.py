# задание
# Сделайте таблицу умножения. Построчно выведите в консоль примеры:
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 9 * 9 = 81

multi = 0
for i in range(1, 10):
    for j in range(1, 10):
        multi = i * j
        print(i, " * ", j, " = ", multi)

#  решение

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
