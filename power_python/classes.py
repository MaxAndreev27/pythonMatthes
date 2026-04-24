import abc
import re


# Simle class with getters and setters
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # Pattern Simple Factory or Alternate Constructor
    @classmethod
    def from_pennies(cls, total_cents):
        dollars = total_cents // 100
        cents = total_cents % 100
        return cls(dollars, cents)

    # Pattern Simple Factory or Alternate Constructor
    @classmethod
    def from_string(cls, amount):
        match = re.search(r"^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$", amount)
        if match is None:
            raise ValueError(f"Invalid amount: {amount}")
        dollars = int(match.group("dollars"))
        cents = int(match.group("cents"))
        return cls(dollars, cents)

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents


piggie_bank_cash = Money.from_pennies(3217)
print(f"piggie_bank_cash: {piggie_bank_cash.total_cents}")

m2 = Money.from_string("$140.75")
print(f"m2: {m2.total_cents}")


# Pattern Factory method or Dynamic Туре
class ImageReader(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def read(self):
        pass  # Этот метод должен реализовать подкласс.

    def __repr__(self):
        return f"{self.__class__.__name__}({self.path})"


class GIFReader(ImageReader):
    def read(self):
        pass  # Чтение изображения в формате GIF


class JPEGReader(ImageReader):
    def read(self):
        pass  # Чтение изображения в формате JPEG


class PNGReader(ImageReader):
    def read(self):
        pass  # Чтение изображения в формате PNG


class RawByteReader(ImageReader):
    def read(self):
        pass  # Чтение необработанных байтов


def extension_of(path):
    # Возвращает "png", "gif", "jpg" и т. д.
    position_of_last_dot = path.rfind(".")
    return path[position_of_last_dot + 1 :]


READERS = {
    "gif": GIFReader,
    "jpg": JPEGReader,
    "png": PNGReader,
}


def get_image_reader(path):
    reader_class = READERS.get(extension_of(path), RawByteReader)
    return reader_class(path)


# Pattern Observer or Publisher Subscriber
class SubscriberOne:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} got message: {message}")


class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"{self.name} got message: {message}")


class Publisher:
    def __init__(self, channels):
        self.subscribers = dict()
        self.channels = {channel: dict() for channel in channels}

    def register(self, channel, who, callback=None):
        if callback is None:
            callback = who.update
        subscribers = self.channels[channel]
        subscribers[who] = callback

    def unregister(self, channel, who):
        subscribers = self.channels[channel]
        del subscribers[who]

    def dispatch(self, channel, message):
        subscribers = self.channels[channel]
        for callback in subscribers.values():
            callback(message)


pub = Publisher(["lunch", "dinner"])
bob = SubscriberOne("Bob")
alice = SubscriberTwo("Alice")
john = SubscriberOne("John")

# pub.register(bob, bob.update)
# pub.register(alice, alice.receive)
# pub.register(john)

pub.register("lunch", bob)
pub.register("dinner", alice, alice.receive)
pub.register("lunch", john)
pub.register("dinner", john)

pub.dispatch("lunch", "It's lunchtime!")
# Джон отписывается от dinner
pub.unregister("dinner", john)

# отправка нового сообщения.
pub.dispatch("dinner", "Dinner is served")
