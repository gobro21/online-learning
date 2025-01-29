def give_sum(a, b):
    print("Результат:", a + b)
def give_difference(a, b):
    print("Результат:", a - b)
def give_product(a, b):
    print("Результат:", a * b)
def give_quotient(a, b):
    print("Результат:", a / b)
def give_remainder(a, b):
    print("Результат:", a % b)
def exponentiate(a, c):
    print("Результат:", a ** c)
try:
    operation = input("Виберіть операцію (+, -, *, /, % або **): ")
    if operation in ('+', '-', '*', '/', '%'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        if operation == '+':
            give_sum(num1, num2)
        elif operation == '-':
            give_difference(num1, num2)
        elif operation == '*':
            give_product(num1, num2)
        elif operation == '/':
            give_quotient(num1, num2)
        elif operation == '%':
            give_remainder(num1, num2)
    elif operation == '**':
        num1 = float(input("Введіть число: "))
        num3 = float(input("Введіть степінь, в яку хочете піднести число: "))
        exponentiate(num1, num3)
    else:
        print("Невідома операція")
except ZeroDivisionError:
    print("Ділення на нуль неможливе")
except ValueError:
    print("Введіть коректні числа")