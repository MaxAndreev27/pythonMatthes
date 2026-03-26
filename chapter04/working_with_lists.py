# For cicle example
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone. That was a great magic show!")

# Range from 1 to 4!!!
for value in range(1, 5):
    print(value)

# Create list from range with step 2
numbers = list(range(2, 11, 2))
print(numbers)

# List of squares
squares = []
for value in range(1, 21):
    square = value**2
    squares.append(square)

print(squares)
print(f"Min: {min(squares)}")
print(f"Max: {max(squares)}")
print(f"Sum: {sum(squares)}")

# List generator
squares = [value**2 for value in range(1, 21)]
print(squares)

# List slice
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
# Equal
print(players[:3])
# From 3 to end
print(players[2:])
# From end to -2
print(players[-2:])
# From 0 to -1, skip 2
print(players[0:-1:2])

# Copy all list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My foods: {my_foods}")
print(f"Friend foods: {friend_foods}")

# Tuples
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
# You can't change element of tuple error
# dimensions[0] = 100

# But you can change tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
