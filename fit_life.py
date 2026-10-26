# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Hello! Let's start with your name: ")
user_age = int(input("How old are you?: "))


# 2. Сбор данных
user_weight = float(input("Write down your weight in kg (example: 81.2): "))
user_height = float(input("Write down your height in m (example: 1.62): "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
def calculate_bmi(weight, height):
    bmi = round(weight / (height ** 2), 1)  # расчёт индекса массы тела
    return bmi


result_bmi = calculate_bmi(user_weight, user_height)


# Подсчет воды: вес * 30 мл
def calculate_water_needed(weight):
    WATER_PER_KG = 30
    ML_TO_L = 1000
    water_ml = weight * WATER_PER_KG
    water_l = water_ml / ML_TO_L
    return water_l


result_water = calculate_water_needed(user_weight)


# 4. Вывод красивого результата
print(f"Report for user: {user_name} ({user_age} years old)")
print(f"Your Body Mass Index (BMI) is: {result_bmi}")
print(f"Recommended water amount for weight {user_weight} kg: {result_water:.1f} l per day")
print()
print("The calculation is complete. Stay healthy!")
