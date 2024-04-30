start = int(input("Введите число для начала отсчета"))
end = int(input("Введите число для конца отсчета"))
step = int(input("Введите число для определения шага"))

for i in range(start, end, step):
    print(i)