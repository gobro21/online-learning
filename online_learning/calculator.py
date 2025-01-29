def give_sum(a, b):
    print("Результат:", a + b)

def give_difference(a, b):
    print("Результат:", a - b)

def give_product(a, b):
    print("Результат:", a * b)

def give_quotient(a, b):
    print("Результат:", a / b)
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Виберіть операцію (+, -, * або /): ")
    if operation == '+':
        give_sum(num1, num2)
    elif operation == '-':
        give_difference(num1, num2)
    elif operation == '*':
        give_product(num1, num2)
    elif operation == '/':
        give_quotient(num1, num2)
    else:
        print("Невідома операція")
except ZeroDivisionError:
    print('ділення на нуль неможливе')
except ValueError:
    print('введіть коректні цифри або числа')