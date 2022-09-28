# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input())

list = []
for i in range(-n, n+1):
    list.append(i)

f = open('file.txt')
i1 = f.readline().rstrip('\n') # чтение строки файла и удаление \n-символа
i2 = f.readline().rstrip('\n')
f.close()

mult = list[int(i1)] * list[int(i2)]

print(mult)