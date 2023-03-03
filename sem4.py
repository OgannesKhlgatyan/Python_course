# 25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. Решить через словарь!

# приветик
# п_1
# р_1
# и_2
# в_1
# е_1
# т_1
# к_1

# string = input('Введите любую строку')
# dict = {}

# for symbol in string:
#     if symbol not in dict:
#         dict[symbol] = 1
#     else:
#         dict[symbol] +=1
# for key, value in dict.items():
#     print(f'{key}_{value}')

# stroka = input()
# dictD = {}
# for i in stroka:
#     dictD[i] = dictD.get(i, 0)+1

# for key, elem in dictD.items():
#     print(f'{key}_{elem}')

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных 
# слов содержится в этом тексте.

# text = input('Введите текст: ')lower().split()
# word = set(text)
# print(word, len(word))


# text = input('введите текст: ').lower().split()
# words=set()
# for i in text:
#     words.add(i) 
# print(len(words))

# stroka = input().lower().split()
# print(type(stroka))
# print(stroka)
# result = set(stroka)
# print(len(result))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность 
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.

# numbers = int(input('Введите число'))
# max = 0

# while x != 0:
#     if x > max:
#         max = x
#     x = int(input())
# print(f'{max} biggest number')

a = int(input())
maximum = a
while a > 0:
    a = int(input())
    if a> maximum:
        maximum = a
print('----')
print(maximum)