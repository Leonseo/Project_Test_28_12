from itertools import product

alphabet = '1234'
ap=[]
for i in product(alphabet, repeat=5):
    if i.count('1') == 2:
        ap.append(i)
    print(i)
print(len(ap))











# n = int(input())
# metki = [int(input()) for _ in range(n)]
# print(metki)
#
# x = 1 #номер вхождения числа, 1- т к индекс с '0'
# y = 1 #номер вхождения числа, 1- т к индекс с '0'
#
# count = 0 # для сохранение
# count_2 = 0
#
# for i in range(len(metki) - 1):
#     if metki[i] < metki[i+1] and metki[i+1] >= metki[i+2]:
#         count = i
#         for j in range(count + 1, len(metki)):
#             if metki[j] > metki[j + 1]:
#                 count_2 = j + 1
#                 break
#
# x += count
# y += count_2
# print(f"Начало - {metki[count]} \nпо индексу - {count} \nпо порядку - {x}")
# print(f"Конец - {metki[count_2]} \nпо индексу - {count_2} \nпо порядку - {y}")


