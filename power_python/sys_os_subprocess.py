import os
import subprocess
import sys

# SYS
# 1. Аргументи командного рядка (наприклад: python script.py data.json)
print(f"Назва скрипта: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Перший аргумент: {sys.argv[1]}")

# 2. Шлях до поточного інтерпретатора (корисно для дебагу venv)
print(f"Python запущено з: {sys.executable}")

# 3. Версія Python
print(f"Версія: {sys.version}")
print("\n")

# 4. Негайний вихід
# sys.exit(0)  # 0 означає успішне завершення

# Stop Debug Point
# pdb.set_trace()

# OS
# 1. Отримання поточної директорії
current_dir = os.getcwd()
print(f"Ми зараз тут: {current_dir}")

# 2. Перелік файлів у папці
files = os.listdir(".")
print(f"Файли в папці: {files}")

# 3. Робота зі змінними оточення (Environment Variables)
user_home = os.environ.get("HOME")
print(f"Домашня папка користувача: {user_home}")

# 4. Створення папки з перевіркою
# if not os.path.exists("new_assets"):
#     os.mkdir("new_assets")
#     print("Папку створено")
print("\n")

# SUBPROCESS
# 1. Простий запуск команди (результат піде в консоль)
subprocess.run(["ls", "-lah"])

# 2. Запуск команди та збереження результату в змінну
result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
print(f"Ваша система: {result.stdout.strip()}")

# 3. Перевірка коду повернення (якщо код 0 — все ок)
if result.returncode == 0:
    print("Команда виконана успішно")
