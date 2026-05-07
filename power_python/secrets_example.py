# import secrets
import secrets
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)

str_for_pass = string.ascii_letters + string.digits + string.punctuation
print(f"Random pass: {''.join(secrets.choice(str_for_pass) for i in range(8))}")
