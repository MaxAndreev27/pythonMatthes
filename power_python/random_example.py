import random

print(f"Random 0..1: {random.random()}")
print(f"Random int 1..100: {random.randint(1, 100)}")
print(f"Random from string: {random.choice('abcdef')}")
print(f"Random from list: {random.choice(['a', 'b', 'c', 'd', 'e', 'f'])}")
print(f"Random 2 from list: {random.choices([1, 2, 3, 4, 5, 6], k=2)}")
my_list = [1, 2, 3, 4, 5, 6]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")
