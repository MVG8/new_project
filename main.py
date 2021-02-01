# for i in range(31):
#     x = int(input("Введите температуру: "))
#     if (x < -273 or x > 50):
#         print("Ошибка. Диапазон температуры не верен!")
#     elif (x < 0):
#         print("Холодно")
#     elif (x > 0):
#         print("Тепло")
#     else:
#        print("ноль")

# money = 1000
# for i in range(10):
#     print()
#     buy = int(input("Введите стоимость товара: "))
#     money = money - buy
#     print("У вас осталось:",money, "денег.")
#     if (money <= 0):
#         print("Все! Стоп! Деньги потрачены!")
#
# a = 5
# b = 10
# while (b > a):
#     a = a + 1
#     print(a)

# sum = 0
# a = int(input("Введите число: "))
# sum += a
# a = int(input("Введите число: "))
# sum += a
# a = int(input("Введите число: "))
# sum += a
# a = int(input("Введите число: "))
# sum += a
# print("Сумма =", sum)

# summa = 0
# for i in range(10000):
#     a = int(input("Введите число: "))
#     summa += a
#     print("Сумма =", summa)

# fact = 1
# x = int(input("Введите число (x!): "))
# for i in range(2, x + 1):
#     fact *= i
#     print(str(x) + "! =", fact)

# print("""Здравствуйте!
# Вас приветствует программа, которая сэкономит бюджет.
# Для выхода из подсчетов введите -1""")
#
# valuta = "денег"
# summa = 0 #Общая сумма на покупки
# count = 0 #Сколько совершено покупок
# buy = 0 #Сумма текущей покупки
#
# summa = int(input("Введите предельную сумму для трат: "))
# startSumma = summa #исходная сумма на покупки
#
# while (summa > 0 and buy != -1):
#     print("Остаток:", summa, valuta)
#     buy = int(input("Введите стоимость покупки: "))
#     if (buy > summa):
#         print("-" * 40)
#         print("Сумма товара не может быть больше суммы на покупки")
#         print("-" * 40)
#     elif (summa > 0):
#         summa -= buy
#         count += 1
#         if (summa < 200 and summa > 0):
#             print("Внимание! Осталщсь", summa, valuta + "!", "Осторожней с тратами!")
#             print("*" * 20)
#
# print("Вы потратили:", startSumma - summa, valuta)
# print("При этом совершили", count, "покупок.")
# # Угадай число-----------
# import random  # Для генерации случайного числа
#
# lowDigit = 10  # Нижняя граница случайгого числа
# highDigit = 50  # Верхняя граница случайного числа
# digit = 0  # Загаданное компьютером число
#
# countInput = 0  # Количество попыток угадать
# win = False  # Угадал текущее число?
# playGame = True  # Продолжается ли игра?
# x = 0  # Число, которое вводит пользователь
# startScore = 100  # Константа ,начальное количество очков
# maxScore = 0  # Максимальное за сессию игры
#
# #
# # _______MainLoop
# while (playGame):  # Главный цикл!
#     digit = random.randint(lowDigit, highDigit)  # Загадываем число
#     print("-" * 30)  # оформление для красоты
#     countInput = 0  # Сколько чисел предложил пользователь
#     score = startScore  # очки ставим на максимум доступных
#     print("Компьютер загадал число, попробуйте отгадать!")
#
#     while (not win and score > 0):  # Внутренний цикл отвечает за один раунд
#         print("-" * 30)  # для красоты
#         print(f"Заработано очков: {score}")  # оформление интерфейс
#         print(f"Рекорд: {maxScore}")  # для красоты оформление
#         # print(f"Загаданное число: {digit}") #Наш чит подсказчик.
#
#         x = ""  # Сбрасываем для условия в while
#         while (not x.isdigit()):  # Контроль ,чтобы пользователь ввел обязательно число
#             x = input(f"Введите число от {lowDigit} до {highDigit}: ")
#             if (not x.isdigit()):
#                 print("." * 27 + "Введите, пожалуйста,число.")
#
#         x = int(x)  # Преобразование из строки в целое число
#         if (x == digit):  # Если пользователь ввел число,загаданное компьютером,то
#             win = True  # Победа
#         else:  # В другом случае продолжать раунд и выводить подсказки
#             length = abs(x - digit)
#
#             if (length < 3):
#                 print("Очень горячо!")
#             elif (length < 5):
#                 print("Горячо!")
#             elif (length < 10):
#                 print("Тепло!")
#             elif (length < 15):
#                 print("Прохладно!")
#             elif (length < 20):
#                 print("Холодно!")
#             else:
#                 print("Ледяной ветер!")
#
#             if (countInput == 7):
#                 score -= 10  # Уменьшаем очки,"стоимость подсказки"
#                 if (digit % 2 == 0):
#                     print("Число четное")
#                 else:
#                     print("Число нечетное")
#             elif (countInput == 6):
#                 score -= 8
#                 if (digit % 3 == 0):
#                     print("Число делится на  3")
#                 else:
#                     print("Число не делится на 3")
#             elif (countInput == 5):
#                 score -= 4
#                 if (digit % 4 == 0):
#                     print("Число делится на 4")
#                 else:
#                     print("Число не делится на 4")
#             elif (countInput > 2 and countInput < 5):
#                 score -= 2
#                 if (x > digit):
#                     print("Загаданное число МЕНЬШЕ вашего")
#                 else:
#                     print("Загаданное число БОЛЬШЕ вашего")
#             score -= 5  # За каждый ход вычитаем 5 из очков
#         countInput += 1  # Обязательно увеличиваем количество "сделанных ходов"
#         print("*" * 40)  # Оформление
#         if (x == digit):  # Если победа ,то поздравляем
#             print("Победа! Поздравляем!")
#         else:
#             print("ОЙ,у вас закончились очки. Вы проиграли :(")  # когда очки закончились
#
#         # Сыграть?
#         if (input("Enter - сыграть еще, 0 - выход ") == "0"):
#             playGame = False
#         else:
#             win = False
#         # Вычитываем максимальное количество очков
#         if (score > maxScore):
#             # Это все после того, как пользователь закончил игру
#             print("*" * 40)
#             print("""Спасибо что сыграли в мою игру!
#     Возвращайтесь скорей! Буду ждать с нетерпением!
#     Р.S. Вы хорошо держались:)""")
#     # КОНЕЦ
# Сложение
# import random
# lowDiapazon = 10
# highDiapazon = 100
#
# for i in range (10):
#    z = random.randint(lowDiapazon, highDiapazon)
#    x = random.randint(lowDiapazon , z)
#    y = z - x
#
#    if (random.randint(0, 1) == 0):
#       print(f"{x} + {y} = {z}")
#    else:
#        print(f"{y} + {x} = {z}")
# Вычитание
# import random
#
# lowDiapazon = 10
# highDiapazon = 100
#
# for i in range(10):
#     x = random.randint(lowDiapazon, highDiapazon)
#     y = random.randint(0, x - lowDiapazon)
#     z = x - y
#     print(f"{x} - {y} = {z}")

# Умножение
# import random
#
# lowDiapazon = 10
# highDiapazon = 100
# for i in range(10):
#     x = random.randint(1, (highDiapazon - lowDiapazon) // 5 + 1)
#     y = random.randint(lowDiapazon, highDiapazon) // x
#
#     z = x * y
#     print(f"{x} * {y} = {z}")

# Деление

# import random
#
# lowDiapazon = 10
# hightDiapazon = 1000
#
# for i in range(10):
#     x = random.randint(1, (hightDiapazon - lowDiapazon) //
#                        random.randint(1, hightDiapazon // 10) + 1)
#     y = random.randint(lowDiapazon, hightDiapazon) // x
#     if (y == 0): #если y=0 то у присвоить 1один
#         y = 1
#     x = x * y
#     z = x // y
#     print(f"{x} / {y} = {z}")

# # *** УЧИСЬ СЧИТАТЬ***
# # Каркас программы
#
#
# import random
#
# lowDiapazon = 10     # нижняя граница чисел
# highDiapazon = 100   # верхняя граница чисел
# sign = 0            # знак операции
# playGame = True     # Главный цикл
# count = 0           # Количество решенных примеров(счетчик)
# right = 0          # Правильные ответы (счетчик)
# score = 0          # Очки
# # Вывод - приветствие
# print("""Компьютер составляет пример. Введите ответ.
# Для завершения работы введите STOP""")
# print("*" * 40)
# # *************************
# # ГЛАВНЫЙ ЦИКЛ ИГРЫ
# #*************************
# while (playGame):
#     # Сообщаем информацию
#     print(f"Ваши очки: {score}")
#     print(f"Обработано задач: {count}")
#     print(f"Правильных ответов : {right}")
#     print("-" * 20)
#
# # Генерируем математический знак
# # Он у нас закодирован числом:
#     # 0 - плюс
#     # 1 - минус
#     # 2 - умножить
#     # 3 - делить#
#     sign = random.randint(0, 3)
#     # ******** СЛОЖЕНИЕ
#     if (sign == 0):
#         z = random.randint(lowDiapazon, highDiapazon)
#         x = random.randint(lowDiapazon, z)
#         y = z - x
#         if (random.randint(0, 1) == 0):
#             print(f"{x} + {y} = ?")
#         else:
#             print(f"{y} + {x} = ?")
#
#     # ********** ВЫЧИТАНИЕ
#     elif (sign == 1):
#         x = random.randint(lowDiapazon, highDiapazon)
#         y = random.randint(0, x - lowDiapazon)
#         z = x - y
#         print(f"{x} - {y} = ?")
#
#     # ********** УМНОЖЕНИЕ
#     elif (sign == 2):
#         x = random.randint(1, (highDiapazon - lowDiapazon) //
#                            random.randint(1, highDiapazon // 10) + 1)
#         y = random.randint(lowDiapazon, highDiapazon) // x
#         z = x * y
#         print(f"{x} * {y} = ?")
#
#     # ************* ДЕЛЕНИЕ
#     elif (sign == 3):
#         x = random.randint(1, (highDiapazon - lowDiapazon) //
#                            random.randint(1, highDiapazon // 10) + 1)
#         y = random.randint(lowDiapazon, highDiapazon) // x
#         if (y == 0):
#             y = 1
#         x = x * y
#         z = x // y
#         print(f"{x} / {y} = ?")
# #------Здесь  Ошибка---------------------------------------------
#  #   x = int(input("Ваш ответ!Введите число: "))
#     #x = ""  # Сбрасываем для условия в while
#  #   while (not x.isdigit()):  # Контроль ,чтобы пользователь ввел обязательно число
#         x = input(f"Введите число от {lowDiapazon} до {highDiapazon}: ")
#   #      if (not x.isdigit()):
#   #          print("." * 27 + "Введите, пожалуйста,число.")
# #--------------------------------------------------------------------------
# #  Блок ввода ответа с провркой на ошибки
# user = ""
# while (not user.isdigit()
#        and user.upper() != "STOP"
#        and user.upper() != "S"
#        and user.upper() != "Ы"
#        and user.upper() != "ЫЕЩЗ"):
#     user = input("Ваш ответ? ")
#
#  # Проверяем ввод: сначала возможные команды
#     if (user.upper() == "HELP"
#             or user == "?"
#             or user == ","
#             or user.upper() == "РУДЗ"):
# # Если число состоит из двух и более цифр , то
#         if (z > 9):
#        # Находим последнюю цифру числа (z % 10)
#             print(f"Последняя цифра ответа: {z % 10}")
#         else:
#             print("Ответ состоит из одной цифры, подсказка невозможна.")
#  # Вычитаем очки за использование подсказки
#         score -= 10
#
# # Команда STOP
#     elif (user.upper() == "STOP"
#
#           or user.upper() == "S"
#           or user.upper() == "Ы"
#           or user.upper() == "ЫЕЩЗ"):
#       # Прекращаем игру, следующей итерации mainloop не будет
#         playGame = False
#     else:
#     # Счетчик обработаных вопросов
#         count += 1
#         if (int(user) == z):
#             print("\nПравильно!\n")
#             right += 1   # Увеличиваем правильные ответы
#             score += 10  # Увеличиваем очки
#         else:
#             print(f"\nОтвет неправильный... Правильно: {z}")
#             print(f"Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (- 10 очков)\n")
#             score -= 20
#
# #********************************
# # Конец ГЛАВНОГО ЦИКЛА
# #*******************************
#
# # Прощальные надписи
# print("*" * 45);
# print("СТАТИСТИКА ИГРЫ:")
# print(f"Всего примеров: {count}")
# print(f"Правильных ответов: {right}")
# print(f"Неправильных ответов: {count - right}")
#
# #count проверяем обязательно, т.к в коде есть строка,
# # в которой count выступает делителем. Он не должен быть
# # равен нулю.
# if (count > 0):
#     print(f"Процент верных ответо : {int(right / count * 100)}")
# else:
#     print("Процент верных ответов: 0%")
#     print("Возвращайтесь!")
#  # КОНЕЦ

# ***Казино***
# def proavec(summa):
#     pokupka1 = 600
#     pokupka2 = 100
#     stoimost = pokupka1 + pokupka2
#     return summa - stoimost
# print(proavec(1000))
#
# def summa(x, y):
#     return x + y
# print(summa(5, 10))
#
# def summa(x, y):
#     return x + y
# x = summa(5, 10)
# y = summa(10, 15)
# print(summa(x, y))
#
# def summa(x, y):
#     return x + y
# for i in range(10):
#     print(summa(i, i + 1))

#def summa(a, b):
#    return a + b
#print("Вернулся результат:", summa(1, 3))

# def summa(a, b):
#     print(a + b)
# print("Вернулся резудьтат:", summa(1, 3))

# s = "Привет! Я строка в файле!"
# a = 100
#
# f = open("testfile.txt", "w", encoding="utf-8")
# f.write(s + "\n")
# f.write(str(a))
# f.close()
#
# f = open("testfile.txt", "r", encoding="utf - 8")
# s = f.readline()
# a = int(f.readline())
# f.close()
#
# s = s.replace("\n", "")
# print(s)
# print(a)