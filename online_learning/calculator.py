def give_sum(a, b):
    print("Сума:", a + b)
def give_difference(a, b):
    print("Різниця:", a - b)
def give_product(a, b):
    print("Добуток:", a * b)
def give_quotient(a, b):
    print("Частка:", a / b)
def give_remainder(a, b):
    print("Залишок від ділення:", a % b)
def exponentiate(a, c):
    print(f"Піднесення до {int(c)} степення: ", a ** c)
try:
    action = input("Виберіть дію (+, -, *, /, % або **): ")
    if action in ('+', '-', '*', '/', '%'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        if action == '+':
            give_sum(num1, num2)
        elif action == '-':
            give_difference(num1, num2)
        elif action == '*':
            give_product(num1, num2)
        elif action == '/':
            give_quotient(num1, num2)
        elif action == '%':
            give_remainder(num1, num2)
    elif action == '**':
        num1 = float(input("Введіть число: "))
        num3 = float(input("Введіть степінь, в яку хочете піднести число: "))
        exponentiate(num1, num3)
    else:
        print("Невідома дія")
except ZeroDivisionError:
    print("Ділення на нуль неможливе")
except ValueError:
    print("Введіть коректні числа")
except OverflowError:
    print("Число занадто велике для обчислення")