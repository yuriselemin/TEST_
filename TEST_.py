


# favorite_fruits = []
# not_favorite_fruits = []
#
# while True:
#     fruits = input('Название фрукта: ')
#     if fruits == 'Яблоко' or 'яблоко' or ' груша' \
#             or 'Груша' or 'Персик':
#         print('Вы угадали! Это я люблю ')
#         favorite_fruits.append(fruits)
#         print(f'Список любимых фруктов: \n{favorite_fruits}')
#     else:
#         print('Нет, спасибо - это не вкусно!')
#         not_favorite_fruits.append(fruits)
#
# _________________________________________________________________
# favorite_fruits = []
# not_favorite_fruits = []
#
# while True:
#     fruits = input('Название фрукта: ').lower()  # Приводим ввод к нижнему регистру
#
#     if fruits in ['яблоко', 'груша', 'персик']:
#         print('Вы угадали! Это я люблю ')
#         favorite_fruits.append(fruits)
#         print(f'Список любимых фруктов: \n{favorite_fruits}')
#     else:
#         print('Нет, спасибо - это не вкусно!')
#         not_favorite_fruits.append(fruits)
#         print(f'Список  не любимых фруктов: \n{not_favorite_fruits}')
#
#     continue_game = input("Хотите ввести ещё один фрукт? (y/n)")
#     if continue_game != 'y':
#         break  # Выходим из цикла, если пользователь не хочет продолжать
#
# print(f"Мои нелюбимые фрукты: {not_favorite_fruits}")


# __________________________________________________________________



# favorite_fruits = []
# unfavorite_fruits = []
#
# # Бесконечный цикл while, который завершится только когда пользователь введет "Стоп"
# while True:
#     # Запрашиваем у пользователя ввод названия фрукта
#     fruit_name = input("Введите название фрукта или 'Стоп' для выхода: ")
#
#     # Если введенный текст совпадает со словом "Стоп", завершаем цикл
#     if fruit_name == "Стоп":
#         break
#
#     # Проверяем, является ли введенный фрукт любимым
#     if fruit_name == "Яблоко" or fruit_name == "Груша":
#         favorite_fruits.append(fruit_name)
#         print("Спасибо! Вы угадали.")
#     else:
#         unfavorite_fruits.append(fruit_name)
#         print("Этот фрукт мне не нравится.")
#
# # Выводим результаты
# print(f"Любимые фрукты: {favorite_fruits}")
# print(f"Нелюбимые фрукты: {unfavorite_fruits}")

# ___________________________________________________

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

num = 0

while num <= len(my_list):
    if my_list[num] > 0:
        print(my_list[num])
    num += 1
    if my_list[num] == 0:
        continue
    if my_list[num] < 0:
        break
