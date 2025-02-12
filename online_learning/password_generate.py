import random
def generate_password(length):
    if length < 6 or length > 32:
        raise ValueError("Довжина пароля має бути від 6 до 32 символів")
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+="
    password = ''
    for i in range(length):
        password += random.choice(all_chars)
    return password
def main():
    try:
        num_passwords = int(input("Скільки паролів потрібно згенерувати? "))
        passwords = []
        for i in range(num_passwords):
            length = int(input(f"Введіть довжину пароля {i + 1}: "))
            passwords.append(generate_password(length))
        print("Згенеровані паролі:")
        for password in passwords:
            print(password)
    except ValueError as e:
        print(f"Помилка: {e}")
main()