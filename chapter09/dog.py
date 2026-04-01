class Dog:
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Имитирует, как собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Имитирует, как собака перекатывается по команде."""
        print(f"{self.name} rolled over!")
