bicycles = ["trek", "cannondale", "redline", "specialized"]

# Get first element
print(bicycles[0])

# Get last element -1 always last, -2 penultimate
print(bicycles[-1])

# Change first element
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"
print(motorcycles)

# Append element
motorcycles.append("honda")
print(motorcycles)

# Insert element
motorcycles.insert(1, "kawasaki")
motorcycles.insert(-1, "иж")
print(motorcycles)

# Delete element by index
del motorcycles[-2]
print(motorcycles)

# Pop operation remove last element
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Pop by index
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

# Removing element by value
motorcycles.remove('suzuki')
print(motorcycles)

# Sorting elements of list and change order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting elements in output but not change list order
print(f"Sorted: {sorted(cars)}")
print(f"But list still in old order: {cars}")

# Reverse elements in list
cars.reverse()
print(f"Reverse: {cars}")

# Length of list
print(f"Length: {len(cars)}")