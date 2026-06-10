from abc import ABC, abstractmethod

# BAD practice
# class DiscountCalculator:
#     def get_discount(self, customer_type, total):
#         if customer_type == "Regular":
#             return total * 0.05
#         elif customer_type == "VIP":
#             return total * 0.10
#         # Довелося лізти всередину класу, щоб додати нову логіку


class Discount(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class RegularDiscount(Discount):
    def apply(self, total: float) -> float:
        return total * 0.05


class VIPDiscount(Discount):
    def apply(self, total: float) -> float:
        return total * 0.10


class DiscountCalculator:
    def calculate(self, discount: Discount, total: float) -> float:
        return discount.apply(total)
