# 1. Student

class Student:
    def __init__(self, naam, student_id):
        self.naam = naam
        self.student_id = student_id
        self.cijfers = []

    def voeg_cijfer_toe(self, cijfer):
        self.cijfers.append(cijfer)

    def gemiddelde(self):
        if not self.cijfers:
            return 0.0
        return sum(self.cijfers) / len(self.cijfers)

    def __str__(self):
        return f"Student {self.naam} ({self.student_id}): {self.gemiddelde():.2f}"


# 2. Stack

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop van lege stack")
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

def omgekeerd(tekst):
    s = Stack()
    for ch in tekst:
        s.push(ch)
    resultaat = ""
    while not s.is_empty():
        resultaat += s.pop()
    return resultaat


# 3. Dictionary frequentie

def frequenties(woordenlijst):
    freq = {}
    for w in woordenlijst:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


# 4. Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        nieuw = Node(x)
        if self.head is None:
            self.head = nieuw
        else:
            huidig = self.head
            while huidig.next is not None:
                huidig = huidig.next
            huidig.next = nieuw

    def find(self, x):
        huidig = self.head
        while huidig is not None:
            if huidig.data == x:
                return True
            huidig = huidig.next
        return False

    def __str__(self):
        waarden = []
        huidig = self.head
        while huidig is not None:
            waarden.append(str(huidig.data))
            huidig = huidig.next
        return " -> ".join(waarden)


# 5. Cursus casus

class Cursus:
    def __init__(self, naam):
        self.naam = naam
        self.studenten = Stack()

    def inschrijven(self, student):
        self.studenten.push(student)

    def toets_afnemen(self):
        resultaten = {}
        while not self.studenten.is_empty():
            student = self.studenten.pop()
            resultaten[student.student_id] = student.gemiddelde()
        return resultaten


# Voorbeeld gebruik:

s1 = Student("Anna", 1)
s1.voeg_cijfer_toe(8)
s1.voeg_cijfer_toe(9)

s2 = Student("Bert", 2)
s2.voeg_cijfer_toe(7)
s2.voeg_cijfer_toe(10)

c = Cursus("Programmeren")
c.inschrijven(s1)
c.inschrijven(s2)

print(c.toets_afnemen())  # bv {2: 8.5, 1: 8.5}
