# 	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

n = int(input())
sum = 0
for i in range(1, n+1):      
    sum += (1 + (1 / i)) ** i


print(round(sum, 2))