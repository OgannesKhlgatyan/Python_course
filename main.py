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

# text = 'Давай ПоУчиМ Python'
# print(text[0])  # Д
# print(text[1])  # а
# print(text[len(text)-1])  # Выведет n (последняя буква)
# print(text[-1])  # выведет первый элемент с конца - n
# print(text[:])  # вывод text
# print(text[:2]) # Вывод элементов с 0 до 2-го т.е. Да
# print(text[len(text)-2:])
# print(text[2:8]) # Вывод элементов с 2 до 9-го т.е. Да

# list_1 = [1, 2, 3, 4, 5]
# print(list_1.pop()) #5
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop(0))
# print(list_1)

# list_1 = [1, 2, 3, 4, 5]
# print(list_1.insert(2, 11)) # где 1-е число это индекс, а 2-е это 
# print(list_1)

# t = ()
# print(t)

# t= (1, 2, 3)
# print(type(t))

# list_1 = []
# for i in range (1,101):
#     if i%2==0:
#         list_1.append(i)
# print(list_1)

# list_1 = [i for i in range (1,101) if i%2==0]
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(*list_1[:]) # 1 2 3 4 5 6 7 8 9 10
# print(*list_1[:4]) # 1 2 3 4
# print(*list_1[4:]) # 5 6 7 8 9 10
# print(*list_1[5:9]) # 6 7 8 9
# print(list_1[len(list_1)-2:]) # 9 10 
# print(list_1[6:-18]) #[]
# print(list_1[::3]) #[1, 4, 7, 10]

# Insert(2, 11)

# t = ()

# v = [1, 2, 3]
# print(v) # [1, 2, 3] это список

# v = tuple(v) 
# print(v) # (1, 2, 3) это кортеж

# d = {} # создаем пустой словарь
# # d = dict() # создаем пустой словарь

# d['q'] = 'qwerty' # создали ключ q, при использовании которого мы получаем 'qwerty'
# d['w'] = 'werty' # создали ключ w, при использовании которого мы получаем 'werty'
# print(d) # {'q': 'qwerty', 'w': 'werty'}

# print(d['q'] + d['w'])

# del d ['q'] # удалили ключ d
# print(d) # {'w': 'werty'}

# for i in d:
#     print(i)
#     #выведет ключи словаря

# for i in d:
#     print('{}: {}'.format(i, d[i]))
#     #выведет ключи словаря и в формате '{}: {}' выведет рядом значения по ключу

# for (k,v) in d.items():
#     print(k,v)

# colors = {'green', 'red', 'blue'} #множество
# colors.add('white') #добавили элемент множества white
# colors.add('gray') #добавили элемент множества gray
# colors.add('gray') #если во множестве есть такой элемент, то он не добавится
# print(colors) #{'blue', 'green', 'red', 'white', 'gray'}

# colors.remove('gray')  #удалили элемент множества gray
# print(colors) #{'blue', 'green', 'red', 'white'}

# colors.discard('gray')  #удалили элемент множества gray

# colors.clear() # удаляет все элементы из множества. № set()
# q = set() #создает пустое множество


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # объединение a и b. u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # пересечение i = {8, 2, 5}
# dI = a.difference(b) # разность dI = {1, 3}
# dr = a.difference(b) # разность dr = {13, 21}
# q = a.union(b).difference(a.intersection(b)) # пример

a = {1, 8, 6}
b = frozenset(a) #замороженное множество
print(b) 

b = a.difference(b) # не сработает