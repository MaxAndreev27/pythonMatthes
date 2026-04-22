from operator import attrgetter, itemgetter


# Extraction arguments use *
def print_args(*args):
    print(f"Use *args for extract {type(args)}: ")
    for item in args:
        print(item)


print_args(1, "Hello", "six")


# Extraction named arguments use **
def print_kwargs(**kwargs):
    print(f"Use *kwargs for extract {type(kwargs)}: ")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


print_kwargs(hero="Homer", antihero="Bart", genius="Lisa")


# Send function argument with * and **
def normal_function(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")


list = [1, 2, 3]
normal_function(*list)
dict = {"c": 3, "a": 7, "b": 5}
normal_function(**dict)


# Use diferent arguments
def general_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


general_function("foo", "bar", х=7, у=33)


# Use diferent arguments for send parameters
def addup(a, b, c=1, d=2, e=3):
    return a + b + c + d + e


nums = [3, 4]
extras = {"d": 5, "e": 2}
print(addup(*nums, **extras))


# Key-Function
def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest


nums = ["12", "7", "11", "30", "14", "3"]
integers = [3, -2, 7, -1, -20]
print(max_by_key(nums, int))
print(max_by_key(integers, abs))


def get_gpa(who):
    return who["gpa"]


student_joe = {"gpa": 3.7, "major": "physics", "name": "Joe Smith"}
student_jane = {"gpa": 3.8, "major": "chemistry", "name": "Jane Jones"}
student_zoe = {"gpa": 3.4, "major": "literature", "name": "Zoe Fox"}
students = [student_joe, student_jane, student_zoe]
# One way use helper function
print(max_by_key(students, get_gpa))

# Universal way use itemgetter from operator
print(max_by_key(students, key=itemgetter("gpa")))

# Use attrgetter for unnamed attr


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return f"{self.name}: {self.gpa}"


students_list = [
    Student("JoeSmith", "physics", 3.7),
    Student("Jane Jones", "chemistry", 3.8),
    Student("Zoe Fox", "literature", 3.4),
]
print(max_by_key(students_list, key=attrgetter("gpa")))
