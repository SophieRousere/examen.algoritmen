# 1. Klassen met erfelijkheid

class Dier:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def geluid(self):
        raise NotImplementedError

class Hond(Dier):
    def geluid(self):
        return "Woef"

class Kat(Dier):
    def geluid(self):
        return "Miauw"


# 2. Stack dieren

# nemen aan dat Stack zoals hierboven bestaat

def verwerk_stack_dieren(dieren_stack):
    while not dieren_stack.is_empty():
        dier = dieren_stack.pop()
        print(f"Naam: {dier.naam}, geluid: {dier.geluid()}")


# 3. Tellingen per diersoort

def tellingen(dierenlijst):
    tel = {}
    for dier in dierenlijst:
        soort = type(dier).__name__  # "Hond" of "Kat"
        tel[soort] = tel.get(soort, 0) + 1
    return tel


# 4. Linked List remove

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        nieuw = Node(x)
        if self.head is None:
            self.head = nieuw
        else:
            huidig = self.head
            while huidig.next:
                huidig = huidig.next
            huidig.next = nieuw

    def remove(self, x):
        huidig = self.head
        prev = None
        while huidig:
            if huidig.data == x:
                if prev is None:
                    # verwijderen head
                    self.head = huidig.next
                else:
                    prev.next = huidig.next
                return True  # verwijderd
            prev = huidig
            huidig = huidig.next
        return False  # niet gevonden

    def find(self, x):
        huidig = self.head
        while huidig:
            if huidig.data == x:
                return True
            huidig = huidig.next
        return False

    def __str__(self):
        waarden = []
        huidig = self.head
        while huidig:
            waarden.append(str(huidig.data))
            huidig = huidig.next
        return " -> ".join(waarden)


# 5. Dierenopvang

class Dierenopvang:
    def __init__(self, naam):
        self.naam = naam
        self.wachtrij = LinkedList()
        self.history = Stack()

    def breng_in(self, dier):
        self.wachtrij.append(dier)

    def haal_op(self):
        # verwijder het eerste dier: head van linked list
        if self.wachtrij.head is None:
            return None
        opgehaald = self.wachtrij.head.data
        # head verwijderen
        self.wachtrij.remove(opgehaald)
        # in geschiedenis steken
        self.history.push(opgehaald)
        return opgehaald

    def soort_telling(self):
        tel = {}
        # We moeten alle dieren uit de stack bekijken, zonder ze permanent te verwijderen.
        temp = Stack()
        while not self.history.is_empty():
            dier = self.history.pop()
            soort = type(dier).__name__
            tel[soort] = tel.get(soort, 0) + 1
            temp.push(dier)
        # terugzetten
        while not temp.is_empty():
            self.history.push(temp.pop())
        return tel


# Voorbeeld gebruik:

opvang = Dierenopvang("Pootjes")

opvang.breng_in(Hond("Rex", 5))
opvang.breng_in(Kat("Miepie", 3))
opvang.breng_in(Hond("Buddy", 2))

d1 = opvang.haal_op()
print(d1.naam, d1.geluid())  # bv "Rex Woef"

d2 = opvang.haal_op()
print(d2.naam, d2.geluid())  # "Miepie Miauw"

print(opvang.soort_telling())  # bv {"Hond": 1, "Kat": 1}
