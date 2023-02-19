#  a = 5
# b = 5.6
# c = 'hi'

# print (f"{a}-{b}-{c}")
# print ("{} - {} - {}".format(a,b,c))

# a = int(input('введите первое число: '))
# b = int(input('введите второе число: '))
# print(a, ' + ' ,b, ' = ', a + b)

# a = 5.44444
# b = 6.44444
# print (round(a+b), 2)

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 3 # iter = iter - 3
# iter *= 3 # iter = iter * 3
# iter /= 3 # iter = iter / 3
# iter %= 3 # iter = iter % 3
# iter //= 3 # iter = iter // 3
# iter **= 3 # iter = iter ** 3

# text = 'Давай ПоУчиМ Python'
# print(len(text))  # Узнать длину строки

# print('Давай' in text)  # Поиск слова в строке

# print(text.lower())  # Перевод строки в нижний регистр

# print(text.upper()) # Перевод строки в верхний регистр

# print(text.replace('Давай', 'ДаВаЙ')) # Меняет сочетание символов в строке

text = 'Давай ПоУчиМ Python'
print(text[0])  # Д
print(text[1])  # а
print(text[len(text)-1])  # Выведет n (последняя буква)
print(text[-1])  # выведет первый элемент с конца - n
print(text[:])  # вывод text
print(text[:2]) # Вывод элементов с 0 до 2-го т.е. Да
print(text[len(text)-2:])
print(text[2:8]) # Вывод элементов с 2 до 9-го т.е. Да
