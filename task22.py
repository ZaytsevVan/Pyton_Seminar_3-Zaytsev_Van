# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
numb1 = int(input("Введите количество чисел в первом множестве: "))
numb2 = int(input("Введите количество чисел во втором множестве: "))

list1 = []
for i in range(numb1):
    list1.append(int(input("Введите новое целое число первого множества: ")))

list2 = []
for i in range(numb2):
    list1.append(int(input("Введите новое целое число второго множества: ")))

set1 = set(list1)
set2 = set(list2)
set1.union(set2)

print(set1)