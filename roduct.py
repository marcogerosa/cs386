from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price: float) -> float:
        pass

class RegularPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price

class SalePricing(PricingStrategy):
    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent

    def calculate_price(self, base_price: float) -> float:
        return base_price * (1 - self.discount_percent / 100)

class Product:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.pricing_strategy = RegularPricing()  # default strategy

    def set_pricing_strategy(self, strategy: PricingStrategy):
        self.pricing_strategy = strategy

    def get_final_price(self) -> float:
        return self.pricing_strategy.calculate_price(self.base_price)

# Usage example
product = Product("Laptop", 1000.00)
# Change to sale pricing
product.set_pricing_strategy(SalePricing(20))  # 20% discount
sale_price = product.get_final_price()  # Returns 800.00
