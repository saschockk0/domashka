import random

print("Добро пожаловать в игру 'Отдадай число'!\nЯ загадал число от 1 до 100. Угадай его!")
number = random.randint(1,100)
guess = int(input("Угадай число!\n"))
tries = 5
while guess != number or tries != 0:
    if guess > number:
        print("Меньше")
    elif guess == number:
        print(f"Вы угадали число {number} и у вас осталось {tries} попыток!")
        break
    elif guess < number:
        print("Больше")
    if tries != 0:
        tries -= 1
    else:
        print("Вы проиграли, лох!")
        break
    guess = int(input("Угадай число!\n"))
