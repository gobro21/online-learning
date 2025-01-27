def give_sum(a, b):
    return a + b
def give_difference(a, b):
    return a - b
def give_product(a, b):
    return a * b
def give_quotient(a, b):
    return a / b
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Виберіть операцію (+, -, * або /): ")
    if operation == '+':
        result = give_sum(num1, num2)
    elif operation == '-':
        result = give_difference(num1, num2)
    elif operation == '*':
        result = give_product(num1, num2)
    elif operation == '/':
        result = give_quotient(num1, num2)
    else:
        result = "Невідома операція"
    print("Результат:", result)
except ZeroDivisionError:
    print('ділення на нуль неможливе')
except ValueError:
    print('введіть коректні цифри або числа')