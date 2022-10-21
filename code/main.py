name = input("Введите свое имя: ")
print("Привет,", name)
age = int(input("Сколько вам лет? "))
print(f"Через 17 лет вам будет {age + 17} лет")
if age > 20:
    print(f"20 лет назад вам было {age - 20} лет")