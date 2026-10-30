# Проект FitLife - MVP версия 1.0

# Константы
WATER_PER_KG = 30
ML_TO_L = 1000
MIN_AGE = 0
MIN_WEIGHT = 0
MIN_HEIGHT = 0.0
MAX_HEIGHT = 3.0  # Максимальный рост в метрах (для проверки ввода)


# 1. Знакомство
user_name = input("Hello! Let's start with your name: ").strip()


while True:
    try:
        user_age = int(input("How old are you?: "))
        if user_age <= MIN_AGE:
            print(f"Please enter a valid age greater than {MIN_AGE}.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number for your age.")


# 2. Сбор данных веса
while True:
    try:
        user_weight = float(input("Write down weight in kg (e.g.: 81.2): "))
        if user_weight <= MIN_WEIGHT:
            print(f"Please enter a valid weight greater than {MIN_WEIGHT} kg.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numbers for weight and height.")


# 3. Сбор данных роста
while True:
    try:
        user_height = float(input("Write down height in m (e.g.: 1.62): "))
        if MIN_HEIGHT <= user_height > MAX_HEIGHT:
            print(
                f"Please enter a valid height greater than {MIN_HEIGHT} m. "
                f"and less than {MAX_HEIGHT} m.",
            )
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number for your height.")


# 4. Логика расчетов (Функции как "черный ящик": используем арифметику)
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


# 5. Вывод красивого результата
print(f"Report for user: {user_name} ({user_age} years old)")
print(f"Your Body Mass Index (BMI) is: {result_bmi}")
print(
    f"Recommended water amount for weight "
    f"{user_weight} kg: {result_water:.1f} l per day",
)
print()
print("The calculation is complete. Stay healthy!")
