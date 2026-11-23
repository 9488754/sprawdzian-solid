"""
Zadanie 1: SRP i OCP w stołówce

łamanie zasad:
- SRP: CanteenOrder przechowywało zamówienie, liczyło cenę i drukowała paragon trzy odpowiedzialności a powwinna być jedna
- OCP: łańcuch if/elif w price() – nowy rodzaj klienta wymagał edycji tej metody.

Rozwiązanie: abstrakcyjny Customer + Student, Teacher, Guest, Intern.
CanteenOrder tylko trzyma dane, ReceiptPrinter drukuje paragon.
Intern dodany bez zmiany istniejących klas.



class CanteenOrder:
BASE_PRICE = 20
def __init__(self, dish: str, customer: str):
self.dish = dish
self.customer = customer
^przechowanie zamówienia (ma sens 1 funkcjonalność)
def price(self):
if self.customer == "uczen":
return self.BASE_PRICE * 0.5
elif self.customer == "nauczyciel":
return self.BASE_PRICE * 0.8
elif self.customer == "gosc":
return self.BASE_PRICE
^łamanie ocp i srp bo to druga funkcjonalność
def print_receipt(self):
return f"{self.dish} | {self.customer} | {self.price()} zł"
^drukowanie paragon trzecia funkcjonalnosc lamanie srp
"""
from abc import ABC, abstractmethod

BASE_PRICE: float = 20


class Customer(ABC):
    name: str = "klient"

    @abstractmethod
    def price(self, base: float) -> float:
        ...


class Student(Customer):
    name: str = "uczen"

    def price(self, base: float) -> float:
        return base * 0.5


class Teacher(Customer):
    name: str = "nauczyciel"

    def price(self, base: float) -> float:
        return base * 0.8


class Guest(Customer):
    name: str = "gosc"

    def price(self, base: float) -> float:
        return base


class CanteenOrder:
    def __init__(self, dish: str, customer: Customer) -> None:
        self.dish: str = dish
        self.customer: Customer = customer


class ReceiptPrinter:
    def __init__(self, base_price: float = BASE_PRICE) -> None:
        self.base_price: float = base_price

    def print_receipt(self, order: CanteenOrder) -> str:
        price: float = order.customer.price(self.base_price)
        return f"{order.dish} | {order.customer.name} | {price} zł"


class Intern(Customer):
    name: str = "praktykant"

    def price(self, base: float) -> float:
        return 0


def wyniki_stolowka() -> list[str]:
    printer: ReceiptPrinter = ReceiptPrinter()
    customers: list[Customer] = [Student(), Teacher(), Guest(), Intern()]
    return [printer.print_receipt(CanteenOrder("Pierogi z serem", c)) for c in customers]