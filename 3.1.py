import random
number = random.randint(1,5)
match number:
    case 1:
        print("Вам выпал сюрприз номер", number, "в нем лежит свинья!")
    case 2:
        print("Вам выпал сюрприз номер", number, "в нем лежит корова!")
    case 3:
        print("Вам выпал сюрприз номер", number, "в нем лежит утка!")
    case 4:
        print("Вам выпал сюрприз номер", number, "в нем лежит гусь!")
    case 5:
        print("Вам выпал сюрприз номер", number, "в нем лежит курица!")