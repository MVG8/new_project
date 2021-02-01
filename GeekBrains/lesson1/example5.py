# ФОРМАТИРОВАНИЕ СТРОК
# ******** ОПЕРАТОР % *******
name = input("Enter your name: ")
print("Hello, %s!" % name)

# Выравнивание по левой стороне
print("%-10s %-10s %-10s" % ('papam1', 'papam2', 'papam3'))

# Указание количества цифр после запятой
print("%.2f" % (20.0/8))

"""

Подстановка      Тип данных
“%s”             Строка
“%d”             Десятичное число
“%f”             Число с плавающей точкой
“%o”             Число в восьмеричной системе
“%x”             Число в шестнадцатеричной системе
 
"""
my_str = "text"
mu_numb = 540
print('%s %d' % (my_str, mu_numb))

#******* МЕТОД FORMAT()********
print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))
"""Используется специальный символ {} для указания точки подстановки значения,
 передаваемого методу format. Каждая пара скобок определяет одно место для подстановки.
"""

print("{:>20} {:>20} {:>20}".format('my_param_1', 'my_param_2', 'my_param_3'))
"""
Вывод данных столбцами одинаковой ширины
 по 20 символов с выравниванием по правой стороне.

"""
print("{:.3f}".format(5.0/3))
"""
Указание количества цифр после запятой
"""

print('Третий элемент: {2}; Второй элемент: {1}; Первый элемент:'
      ' {0}'.format('el_1', 'el_2', 'el_3'))
"""
Передать параметры можно и через указание их индексов
 в фигурных скобках:

"""
#****************** F-СТРОКИ **********

ip = '192.168.1.4'
mask = 10

print(f"ip-params: {ip}, mask: {mask}")
"""
f-строки — механизм форматирования строки с префиксом f.
 Внутри f-строки в паре фигурных скобок указываются 
 имена переменных, которые необходимо подставить.
"""


octets = ['10', '1', '1', '1']
mask = 10

print(f"ip-params: {'.'.join(octets)}, mask: {mask}")

"""
Помимо подстановки значений переменных,
 в фигурных скобках допустимо применить выражение:
"""

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]

print(f'''IP address: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}''')
"""
Через f-строки также возможен вывод столбцами
 с одинаковым расстоянием между ними:
"""