def hello():  # Функция без аргументов
    print("Hello, World!")


hello()


def hi(name):  # Функция с аргументом
    print(f"Hi, {name}!")


name = input("Enter your name: ")
hi(name)


def sum_numbers(a, b):  # Функция с двумя аргументами
    sum_result = a + b
    print(f"The sum of {a} and {b} is {sum_result}")


sum_numbers(5, 10)
sum_numbers(20, 30)
sum_numbers(100, 200)


def multiply_numbers(a, b):  # Функция с двумя аргументами и возвратом значения
    return a * b
    # Это строка никогда не будет выполнена после return
    print("This line will never be executed")


result = multiply_numbers(5, 10)
