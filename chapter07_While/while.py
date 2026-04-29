# Input data
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Input with change string to integer
age = input("How old are you: ")
age = int(age)
if age >= 18:
    print("You can pass")
else:
    print("Access denied")

# Remainder of division by modulo
print(f"Remainder of division 5%3={5%3}")

# While loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

# While with break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# While remove value in list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")

print(pets)
