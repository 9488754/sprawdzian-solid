"""class LabDevice:
def __init__(self, name: str):
self.name = name

def run_code(self, program: str):
return f"{self.name} uruchamia {program}"

def print_3d(self, model: str):
return f"{self.name} drukuje {model}"

def display(self, slide: str):
return f"{self.name} wyświetla {slide}"

class Printer3D(LabDevice):
def run_code(self, program: str):
raise Exception("Drukarka nie uruchamia kodu!")

def display(self, slide: str):
raise Exception("Drukarka nie ma ekranu!")

class SmartBoard(LabDevice):
def print_3d(self, model: str):
raise Exception("Tablica nie drukuje!")

def hackathon(devices: list[str]):
return [d.run_code("main.py") for d in devices]
"""


"""
Zadanie 2: LSP i ISP w pracowniach

- Printer3D lamie LSP, bo jest podklasa LabDevice, ale nie mozna go uzyc tam, gdzie oczekiwany jest LabDevice: run_code() i display() rzucaja wyjatki, wiec np. hackathon() wywala sie na drukarce.
  
- LabDevice lamie ISP, bo jeden gruby interfejs (run_code, print_3d, display) zmusza kazde urzadzenie do metod, ktorych nie potrzebuje.

Rozwiazanie: LabDevice ma tylko name, a mozliwosci to male interfejsy CodeRunner, Printer, Display.
"""
from abc import ABC, abstractmethod


class LabDevice:
    def __init__(self, name: str):
        self.name = name


class CodeRunner(ABC):
    @abstractmethod
    def run_code(self, program: str) -> str:
        ...


class Printer(ABC):
    @abstractmethod
    def print_3d(self, model: str) -> str:
        ...


class Display(ABC):
    @abstractmethod
    def display(self, slide: str) -> str:
        ...


class Workstation(LabDevice, CodeRunner, Display):
    def run_code(self, program):
        return f"{self.name} uruchamia {program}"

    def display(self, slide):
        return f"{self.name} wyświetla {slide}"


class Printer3D(LabDevice, Printer):
    def print_3d(self, model):
        return f"{self.name} drukuje {model}"


class SmartBoard(LabDevice, Display):
    def display(self, slide):
        return f"{self.name} wyświetla {slide}"


def hackathon(devices: list[CodeRunner]):
    return [d.run_code("main.py") for d in devices]


def wyniki_pracownie():
    devices = [
        Workstation("Komputer 204-1"),
        Printer3D("Drukarka 3D 204"),
        SmartBoard("Tablica 204"),
    ]
    wyniki = []
    for d in devices:
        if isinstance(d, CodeRunner):
            wyniki.append(d.run_code("main.py"))
        if isinstance(d, Printer):
            wyniki.append(d.print_3d("obudowa.stl"))
        if isinstance(d, Display):
            wyniki.append(d.display("Prezentacja SOLID"))
    return wyniki