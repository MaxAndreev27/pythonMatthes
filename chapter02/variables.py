# Simple string var
message = "This is new message"
print(message)

# formatting string
firstName = "ada"
lastName = "lovelace"
fullName = f"{firstName} {lastName}"
print(f"Hello {fullName.title()}")
print(f"Hello {fullName.upper()}")

# \t Tab symbol
print("\tPythoon")

# \n New line symbol
print("Languages:\n\tPython\n\tPHP\n\tTypeScript")

# Remove space left and right
favoriteLanguage = "    C, Python, Go, PHP       "
print(favoriteLanguage.strip())

# Remove prefix
siteUrl = "https://mysite.com"
print(siteUrl.removeprefix("https://"))

# Operation with digits
print(f"4 to the power of 3 = {4**3}")

print(f"Wow result 0.2+0.1 = {0.2+0.1}")

print(f"Universe_age = {14_000_000_000}")

x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Constants
MAX_VALUE = 5_000
print(f"MAX_VALUE: {MAX_VALUE}")

# The Zen of Python, by Tim Peters Write in python terminal: import this
