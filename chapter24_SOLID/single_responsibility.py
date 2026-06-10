# BAD practice
# class Order:
#     def __init__(self, items):
#         self.items = items

#     def calculate_total(self):
#         return sum(item["price"] for item in self.items)

#     def save_to_db(self):
#         print("Збереження замовлення в БД...")

#     def send_confirmation_email(self):
#         print("Відправка листа клієнту...")


class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)


class OrderRepository:
    def save(self, order: Order):
        print("Збереження замовлення в БД...")


class NotificationService:
    def send_email(self, order: Order):
        print("Відправка листа клієнту...")
