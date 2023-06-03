import random

# функция для записи результата игры в файл
def result(name, attempts):
    with open("game.txt", "a") as file:
        file.write(f"{name}: {attempts} attempts\n")

# загадываем число
number = random.randint(1, 100)
attempts = 0
name = input("Введите свое имя: ")

# игровой цикл
while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    attempts += 1
    if guess < number:
        print("Задуманное число больше вашего ответа")
    elif guess > number:
        print("Задуманное число меньше вашего ответа")
    else:
        print(f"Вы угадали число за {attempts} попыток!")
        result(name, attempts)
        break