#Автодилер
car_price = input("Введите сумму\n")
tax = 0.05
reg_tax = 0.03
agency_tax = 15000
delivery_tax = 10000
final_price = int(car_price) + float(car_price) * reg_tax + float(car_price) * tax + agency_tax + delivery_tax
print(f"Финальная сумма - {final_price}")