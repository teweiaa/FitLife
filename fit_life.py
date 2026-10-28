# Проект FitLife - MVP версия 1.0

# Константы
WATER_PER_KG = 30
ML_TO_L = 1000


# 1. Знакомство
user_name = input("Hello! Let's start with your name: ").strip()


while True:
    try:
        user_age = int(input("How old are you?: "))
        if user_age <= 0:
            print("Please enter a valid age greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number for your age.")


# 2. Сбор данных
user_weight = float(input("Write down your weight in kg (example: 81.2): "))
user_height = float(input("Write down your height in m (example: 1.62): "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
def calculate_bmi(weight, height):
    """Calculate BMI from weight and height."""
    return round(weight / (height ** 2), 1)  # расчёт индекса массы тела


result_bmi = calculate_bmi(user_weight, user_height)


# Подсчет воды: вес * 30 мл
def calculate_water_needed(weight):
    """Calculate recommended water intake based on weight."""
    return weight * WATER_PER_KG / ML_TO_L  # water in liters


result_water = calculate_water_needed(user_weight)


# 4. Вывод красивого результата
print(f"Report for user: {user_name} ({user_age} years old)")
print(f"Your Body Mass Index (BMI) is: {result_bmi}")
print(
    f"Recommended water amount for weight "
    f"{user_weight} kg: {result_water:.1f} l per day",
)
print()
print("The calculation is complete. Stay healthy!")
