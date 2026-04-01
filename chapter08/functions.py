# Import all functions from module pizza.make_pizza
# import pizza
# import pizza as p

# Import all function from module pizza
# from pizza import *
# make_pizza(16, 'pepperoni')

# Use alias for function
from pizza import make_pizza as mp


# Greeter function
def greet_user(username):
    """Выводит простое приветствие."""
    print(f"Hello! {username.title()}")


greet_user("john")


# Keyword argument
def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")


# Default value for parameter
def describe_pet(pet_name, animal_type="dog"):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="Willie")


# Return value from function
def get_formatted_name(first_name, last_name):
    """Возвращает отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Return dictionary
def build_person(first_name, last_name):
    """Возвращает словарь с информацией о человеке."""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)


# List as parameter
def greet_users(names):
    """Выводит простое приветствие для каждого пользователя в списке."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

# Passing an arbitrary set of arguments (tuple)
# def make_pizza(size, *toppings):
#     """Выводит описание пиццы."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# pizza.make_pizza(16, "pepperoni")
mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")


# Using an arbitrary set of named arguments
def build_profile(first, last, **user_info):
    """Создает словарь, содержащий информацию о пользователе."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
