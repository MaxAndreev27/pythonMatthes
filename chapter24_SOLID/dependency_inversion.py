# BAD practice
# class MySQLDatabase:
#     def insert(self, data):
#         print(f"Запис у MySQL: {data}")


# class Manager:
#     def __init__(self):
#         # Пряма залежність від конкретної реалізації!
#         self.db = MySQLDatabase()

#     def save_user(self, user_data):
#         self.db.insert(user_data)

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def insert(self, data):
        pass


class MySQLDatabase(Database):
    def insert(self, data):
        print(f"Запис у MySQL: {data}")


class PostgreSQLDatabase(Database):
    def insert(self, data):
        print(f"Запис у Postgres: {data}")


class Manager:
    # Залежимо від інтерфейсу Database, а не від конкретного класу
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user_data):
        self.db.insert(user_data)


# Тепер базу можна легко підмінити на льоту:
mysql_manager = Manager(MySQLDatabase())
postgres_manager = Manager(PostgreSQLDatabase())
