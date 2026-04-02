class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в милях."""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        if miles > 0:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """Заправка бака."""
        print("Tank FULL!")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't have a gas tank!")


class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=40):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода для аккумулятора."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
