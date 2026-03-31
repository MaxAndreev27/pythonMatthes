alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# Add new keys to dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# Del key from dictionary
del alien_0["points"]
print(alien_0)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# Use get() method for safe get key value, None
point_value = alien_0.get("points", "Key don't exist")
print(point_value)

# Dictionary enumeration
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

# Only keys
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())

# Only values
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    "mike": "c",
}
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Without dooble, only unique values
print("\nUnique values:")
for language in set(favorite_languages.values()):
    print(language.title())

# Dictionary inside list
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Lists inside dictionary
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Dictionary inside dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
