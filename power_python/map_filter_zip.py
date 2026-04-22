# Тернарний оператор у Python
age = 20
status = "дорослий" if age >= 18 else "дитина"

# Моржовий оператор :=
if line := 1 < 10:
    print(line)

# Функція map()
names = ["max", "anna", "dmitry"]
clean_names = list(map(str.capitalize, names))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# Функція zip()
names = ["Max", "Anna", "Dmitry"]
stars = [150, 85, 200]
# Об'єднуємо два списки
combined = list(zip(names, stars))
for name, star_count in zip(names, stars):
    print(f"Проєкт {name} має {star_count} зірок.")

# Функція filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Функція повертає True, якщо число ділиться на 2 без залишку
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Виведе: [2, 4, 6, 8, 10]

data = ["Django", "", "Python", None, "Flask", " ", False, 0]
# Якщо не вказувати функцію (None), filter просто прибере все, що оцінюється як False
clean_data = list(filter(None, data))

print(clean_data)
