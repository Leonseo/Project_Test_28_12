respones = {}

polling_active = True
while polling_active:
    name = input("What is your name?")
    response = input("Withs mountain you like to climb someday?")

    respones[name] = response

    repet = input("Wold you like to let another person respond? (yes/no)")
    if repet == 'no':
        polling_active = False

print("\n--- Poll Result ---")
for name, respones in respones.items():
    print(f"{name} would like to climb {respones}.")

















# count = 0
# for x in range(1,10):
#     for y in range(1,10):
#         if -x / 3 ** 0.5 + 10 > y > x / 3 ** 0.5:
#             count += 1
# print(count)



# f = open('inf_26_04_21_26.txt')
# k = f.readlines() #создаем список строк
# print(k)
# n = list(map(int, k))
# print(n)
# m = 0
# s = 0
# c = 0
# ns = set(n)
# for i in range(1, len(n) - 1):
#     for j in range(i + 1, len(n)):
#         if((n[i] + n[j]) % 2 != 1):
#             s = n[i] + n[j]
#             if (s in ns ):
#                 c += 1
#                 if s > m:
#                     m = s
#
# print(c,m)



# count = 0
# i = 600_001
# while count < 5:
#     for j in range(17, i, 10):
#         if i % j == 0:
#             print(i, ' ', j)
#             count += 1
#             break
#     i += 1



# f = open("")
# x = f.read()
# print(x)
# count = 0
# count_old = 0
# m = 0
#
# for i in x: #проходим по каждой букве
#     if i == 'A': #если находим букву А
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# m = max(m,count + count_old + 1)
# print(m)

















# from turtle import*
# t = Turtle()
# t.penup()
# t.goto(-150,150)
# t.pendown()
# t.speed(300)
# # t.right(90)
#
# for i in range(15):
#     t.forward(300)
#     t.right(90)
#     t.forward(10)
#     t.right(90)
#     t.forward(300)
#     t.right(-90)
#     t.forward(10)
#     t.right(-90)
#
#
# for i in range(15):
#     t.right(-90)
#     t.forward(300)
#     t.right(90)
#     t.forward(10)
#     t.right(90)
#     t.forward(300)
#     t.right(-90)
#     t.forward(10)
#
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.right(-90)
# t.color('red')
#
# t.forward(150)
# t.right(180)
# t.forward(300)
#
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.right(-90)
#
# t.forward(150)
# t.right(180)
# t.forward(300)
#
# t.penup()
# t.goto(0,0)
# t.right(90)
#
# #перенос по условию
# t.forward(10)
# t.right(90)
# t.forward(10)
# t.right(30)
# t.pendown()
# t.color('green')
#
# # for i in range(10):
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(404)
# #     t.right(90)
#
# # Треугольник
# for i in range(7):
#     t.forward(100)
#     t.right(120)
#
#
#
#
#
# t.screen.exitonclick()
# t.screen.mainloop()






# user = {
#     'name' : {
#     'username':'leonid',
#     'first':'badeev',
#     'last':'fermi'
# },
#     'name2' : {
#     'username':'leonid2',
#     'first':'badeev2',
#     'last':'fermi2'
#     }
# }
# for username, user_info in user.items():
#     print(f"\nUsername: {username}")
#     fullname = f"{user_info['first']} {user_info['last']}"
#     print(fullname)
#

# f = open('26f.txt')
# n,m = f.readline().split() #Выпиливаем строку и разбиваем строку, значения передаем
# # print(n,m)
# n = int(n) #колличество дет
# m = int(m) #Сумма
#
# summ = 0
# arrayAB = [[0] * 2 for i in range(n)] # Двумерный массив для всех элементов
# # print(arrayAB)
# arrayB = [[0] * 2 for i in range(n)]
# for i in range(n):
#     x,z = f.readline().split()
#     arrayAB[i][0] = int(x)
#     if z == 'B':
#         arrayAB[i][1] = 0 # Заменяем B на 0
#     if z == 'A':
#         arrayAB[i][1] = 1 # Заменяем А на 1
#
# arrayAB.sort() # Сортируем массив по возрастанию тут и А и Б
# # print(arrayAB)
#
#
# #посчитаем максимальное количество изделий,
# # которое можем закупить на заданную сумму,
# # последовательно прибавляя к переменной
# # summ цену изделия в текущем элементе.
# count = 0
# i = 0
# while m > arrayAB[i][0] + summ:  #Пока Максимальная сумма больше текущей
#     if(summ + arrayAB[i][0]) < m:
#         summ = summ + arrayAB[i][0]
#         count += 1
#         print('count', count)
#     i += 1
#
# x = 0
# for i in range(count, n):
#     if arrayAB[i][1] == 0:
#         arrayB[x][0] = arrayAB[i][0] #Стоимость
#         arrayB[x][1] = arrayAB[i][1] #
#         x += 1
# # print(arrayB)
# x = 0
# for i in range(count-1, 0, -1):
#     if arrayAB[i][1] == 1: #если Тип = A
#         if(summ - arrayAB[i][0] + arrayB[x][0]) > m:
#             break
#         summ = summ - arrayAB[i][0] + arrayB[x][0]
#         arrayAB[i][0] = arrayB[x][0]
#         arrayAB[i][1] = arrayB[x][1]
#         x += 1
#
#
# countB = 0
# for i in range(count):
#     if arrayAB[i][1] == 0:
#         countB += 1
# print(countB, m - summ)
#



































# a = 185_311
# b = 185_330
#
#
# for i in range(a,b+1):
#     mass = []
#     for j in range(1, int(i**0.5) + 1):
#         if j * j == i :
#             mass.append(j)
#         elif i % j == 0:
#             mass.append(j)
#             mass.append(i//j)
#
#     if len(mass) == 4:
#         mass.sort()
#         print(mass[0],mass[1],mass[2],mass[3])
#






































# f = open('26f.txt')
# n,m = f.readline().split() #Выпиливаем строку и разбиваем строку, значения передаем
# print(n,m) # Проверям
# # pr1,pr2 = f.readline().split() # Проверяем что идет след строка
# # print(pr1,pr2) # Проверям
# n = int(n) # Число деталей
# m = int(m) # Максимальная сумма
# print(n)
# print(m)
# count = 0
# summ = 0
# arrayAB = [[0] * 2 for i in range(n)] # Двумерный массив для всех элементов
# arrayB = [[0] * 2 for i in range(n)] #
# #В первый массив считаем все элементы из файла и отсортируем его по возрастанию.
# for i in range(n):
#     x,z = f.readline().split()
#     # print('x =', x , 'z =', z)
#     arrayAB[i][0] = int(x)
#     if z == 'B':
#         arrayAB[i][1] = 0 # Заменяем B на 1
#     if z == 'A':
#         arrayAB[i][1] = 1 # Заменяем А на 0
# arrayAB.sort() # Сортируем массив по возрастанию тут и А и Б
# print(arrayAB) # Проверяем
# ##############
# i = 0
# # После этого посчитаем максимальное количество изделий,
# # которое можем закупить на заданную сумму,
# # последовательно прибавляя к переменной
# # sum цену изделия в текущем элементе.
# # Здесь A и B так,
# while m > arrayAB[i][0] + summ: #Пока Максимальная сумма больше текущей
#     if(summ + arrayAB[i][0]) < m:
#         summ = summ + arrayAB[i][0]
#         print(arrayAB[i][0])
#         count += 1
#         print('count', count)
#     i += 1
#
# x = 1 # не 0, потому что
# #Далее, в отдельный
# # двумерный массив вынесем только оставшиеся изделия B.
# # Те которые остались после внесения   arrayAB
# for i in range(count,n): # count 273 n = 916
#     if arrayAB[i][1] == 0: # Если == B, так как B = 0
#         # print(arrayAB[i][1]) # Проверяем
#         arrayB[x][0] = arrayAB[i][0] #Стоимость
#         arrayB[x][1] = arrayAB[i][1] #Индекс 0 так как B = 0
#         # Проверяем
#         # print('arrayB[x][0] = ',arrayB[x][0],'\n','arrayB[x][1] =' ,arrayB[x][1] )
#         x += 1
#
# # Далее, будем перебирать уже взятые изделия с конца,
# # пытаясь заменить изделия A на изделия B таким образом,
# # чтобы сумма взятых изделий не превышала заданную сумму
# x = 1
# for i in range(count-1, -1, -1):
#     if arrayAB[i][1] == 1: #если запчасть = A
#         #Если заложенная больше, чем дейстыующая
#         # сумма после вычета объекта A
#         # и прибавления объекта Б
#         if(summ - arrayAB[i][0] + arrayB[x][0]) > m:
#             break # заканчиваем цикл
#         #Иначе меняем сумму после вычета элемена А и
#         # прибавления элемента B
#         summ = summ - arrayAB[i][0] + arrayAB[x][0]
#         arrayAB[i][0] = arrayB[x][0] #меняем стоимость покупки с А на B
#         arrayAB[i][1] = arrayB[x][1] #меняем наименоание детали с А на B == c 1 на 0
#         x += 1
#
#  # После этого посчитаем,
# # сколько изделий B получилось закупить.
# countB = 0 # сохранять значения B
# for i in range(count):
#     if arrayAB[i][1] == 0:
#         countB = countB + 1
# print(countB, m - summ)
#
#
#
#
#
#
#
#
#
#
#










# n = int(input()) #Дней в отпуске # 14
# d = int(input()) #Номер дня недели # 1
# monday = False
# s = 0
#
# for i in range(n):
#     if (d + i) % 7 == 1: # 1 + 7 = 8 % 7 = 1
#         monday = True
#     elif (d + i) % 7 == 0 and monday : # 1 + 6 = 7 % 7 = 0
#         s += 1 # + 1
# print(s)
#




    # if (n != 1):
# print('x','y','z','w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if (not(y <= (x == w)) and (z <= x)):
#                     print(x,y,z,w)
# n = int (input ())
# d = int (input ())
# monday = False
# sunday = 0
# for i in range ( n ) :
#     if ( d + i ) % 7 == 1 :
#         monday = True
#     elif ( d + i ) % 7 == 0 and monday :
#         sunday += 1
# print(sunday)









# for i in range(10000, 1, -1):
#     s = i
#     s = s // 10
#     n = 1
#     while s < 51:
#         s = s + 5
#         n = n * 2
#     if n == 64:
#         print(i)
#         break








# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not(y <= (x == w)) and (z <= x):
#                     print(x, y, z, w)




# def sum_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_n(n-1)
# def factorial(n):
#     result = 1
#
#     for i in range(1, n + 1):
#         result = result * i
#
#     return result
#
# print(factorial(10))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * 1
# = 120

# Например — 1, 1, 2, 3, 5, 8, 13, 21
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     i1 = 0
#     i2 = 0
#     num = 1
#     for x in range(1, n):
#         num = i1 + i2
#         i1 = i2
#         i2 = num
#     return num
#
# for i in range(10):
#     print(fibonacci(i), end=" ")
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for i in range(10):
#     print(fibonacci(i), end=" ")
#
# fibonacci(5)
# fibonacci(5)
# = fibonacci(4) + fibonacci(3)
# = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
# = fibonacci(2) + fibonacci(1) + 2*(fibonacci(1) + fibonacci(0)) + 1
# = fibonscci(1) + fibonacci(0) + 1 + 2*(1 + 0) + 1

# s = int(input())
# n = int(input())
# s1 = 0
# s2 = 0
# for i in range(n):
#     a = int(input())
#     if s1 + a <= s:
#         s1 = s1 + a
#     else:
#         s2 += a
# print(s1,s2)




