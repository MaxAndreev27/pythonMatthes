numbers = [5, 7, 12, 25]
for num in numbers:
    print(num)

# iter(numbers) this is analog:
numbers_iter = iter(numbers)
for num in numbers_iter:
    print(num)

names = ["Tom", "Shelly", "Garth"]
names_iter = iter(names)
# Tom
print(next(names_iter))
# Shelly
print(next(names_iter))
# Garth
print(next(names_iter))
# Traceback StopIteration
# print(next(names_iter))
# Default value if StopIteration
print(next(names_iter, "Jack"))


# Function Generator use yield
def gen_nums(N):
    n = 1
    while n < N:
        # Always return object generator
        yield n
        n += 1

print('Use function generator in for:')
for num in gen_nums(5):
    print(num)

print("Use next:")
sequence = gen_nums(6)
print(next(sequence))
print(next(sequence))