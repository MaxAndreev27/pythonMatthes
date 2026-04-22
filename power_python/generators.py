# List generator
squares = [n * n for n in range(6)]
print(squares)
# Same
squares = []
for n in range(6):
    squares.append(n * n)

# Dictionary generator
blocks = {n: "x" * n for n in range(5)}
print(blocks)
# Same
blocks = dict()
for n in range(5):
    blocks[n] = "х" * n
print(blocks)


# Polindrom
def is_palindrome(s):
    return s == s[::-1]


words = ["bib", "bias", "dad", "еуе", "deed", "tooth"]
print([word for word in words if is_palindrome(word)])

pets = ["dog", "parakeet", "cat", "llama"]
print([pet.upper() for pet in pets if len(pet) == 3])

numbers = [9, -1, -4, 20, 11, -3]
print([n for n in numbers if n > 0])
print([n * 2 for n in numbers if n % 2 == 0])

# Many independent for list
colors = ["orange", "purple", "pink"]
toys = ["bikе", "basketball", "skateboard", "doll"]
color_toys = [color + " " + toy for color in colors for toy in toys]
print(color_toys)

# Many relation for list
ranges = [range(1, 7), range(4, 12, 3), range(-5, 9, 4)]
print([float(num) for subrange in ranges for num in subrange])

# Many if
numbers = [9, -1, -4, 20, 17, -3]
print([num for num in numbers if num > 0 if num % 2 == 1])
print([num for num in numbers if num > 0 and num % 2])
print([num for num in numbers if num > 0 or num % 2])

# Generator in ()
NUM_SQUARES = 10 * 1000 * 1000
many_squares = [n * n for n in range(NUM_SQUARES)]
# Bad practice, before for need calculate many_squares
print(f"Type of many squares inside []: {type(many_squares)}")
for number in many_squares:
    # print(number)
    pass
# Best practice like yield style inside ()
generated_squares = (n * n for n in range(NUM_SQUARES))
print(f"Type of many squares inside (): {type(generated_squares)}")
