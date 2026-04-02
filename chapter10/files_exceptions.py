from pathlib import Path
import json

# Read file content
base_dir = Path(__file__).parent
path = base_dir / "pi_digits.txt"
# print(base_dir)
print(f"File path: {path}")
print("File content:")
contents = path.read_text().strip()
print(contents)

print("File content split to lines:")
# Split content to lines
pi_string = ""
lines = contents.splitlines()
for line in lines:
    pi_string += line.strip()
    print(line)

print(f"Pi={pi_string}")
print(f"Pi length={len(pi_string)}")

# Get Pi Million digits
path = base_dir / "pi_million_digits.txt"
print(f"File path: {path}")
print("File content:")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:50]}...")
print(len(pi_string))

# Your birthday in Pi
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = base_dir / "programming.txt"
path.write_text(contents)

# Try Except
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Can't divide by 0")

# Try Except Else
try:
    result = 5 / 2
except ZeroDivisionError:
    print("Can't divide by 0")
else:
    print(f"Result 5/2={result}")


# Exception in file read
def count_words(path):
    """Подсчитывает приблизительное количество строк в файле."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # pass
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


books = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for book in books:
    count_words(base_dir / book)

# Work with JSON
numbers = [2, 3, 5, 7, 11, 13]
path = base_dir / "numbers.json"
# Write
contents = json.dumps(numbers)
path.write_text(contents)
# Read
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


def greet_user():
    """Приветствует пользователя по имени."""
    path = base_dir / "username.json"
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
