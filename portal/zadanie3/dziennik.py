"""
Zadanie 3: DIP w TechniDzienniku

Oryginalnie GradeReport sam tworzyl PaperJournal (twarda zaleznosc od konkretnej klasy) nie dalo sie podmienic zrodla ani testowac
na   danych probnych. Teraz GradeReport zalezy od abstrakcji GradeSourcei dostaje zrodlo w konstruktorze (wstrzykiwanie zaleznosci).
"""
from abc import ABC, abstractmethod


class GradeSource(ABC):
    @abstractmethod
    def get_grades(self, student: str) -> list[int]:
        ...


class PaperJournal(GradeSource):
    def get_grades(self, student):
        return {"Ada": [5, 6, 5], "Linus": [3, 4, 4]}.get(student, [])


class TechniDziennik(GradeSource):
    DATA = {
        "Ola": [6, 5, 5, 6],
        "Marek": [4, 3, 4],
        "Kasia": [5, 5, 4, 5],
    }

    def get_grades(self, student):
        return self.DATA.get(student, [])


class GradeReport:
    def __init__(self, source: GradeSource):
        self.source = source

    def average(self, student):
        grades = self.source.get_grades(student)
        if not grades:
            return None
        return round(sum(grades) / len(grades), 2)


def wyniki_dziennik():
    wyniki = []
    for label, source, students in [
        ("PaperJournal", PaperJournal(), ["Ada", "Linus", "Nowy"]),
        ("TechniDziennik", TechniDziennik(), ["Ola", "Marek", "Kasia", "Nowy"]),
    ]:
        report = GradeReport(source)
        for s in students:
            avg = report.average(s)
            wyniki.append(f"{label}: {s} - " + (str(avg) if avg is not None else "brak ocen"))
    return wyniki