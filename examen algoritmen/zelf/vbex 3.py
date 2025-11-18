# 1. Boek

class Boek:
    standaard_pagina = 100

    def __init__(self, titel, auteur, aantal_pagina=None):
        self.titel = titel
        self.auteur = auteur
        if aantal_pagina is None:
            self.aantal_pagina = Boek.standaard_pagina
        else:
            self.aantal_pagina = aantal_pagina

    @staticmethod
    def aanbevolen_leesduur(pagina_snelheid):
        # tijd in minuten
        return Boek.standaard_pagina / pagina_snelheid


# 2. Stack lenen boeken

def leen_boek(stack, boek):
    stack.push(boek)

def breng_terug(stack):
    return stack.pop()


# 3. Boeken per auteur dictionary

def boeken_per_auteur(boekenlijst):
    d = {}
    for b in boekenlijst:
        if b.auteur in d:
            d[b.auteur].append(b.titel)
        else:
            d[b.auteur] = [b.titel]
    return d


# 4. Linked List insert op index

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        nieuw = Node(x)
        if not self.head:
            self.head = nieuw
        else:
            huidig = self.head
            while huidig.next:
                huidig = huidig.next
            huidig.next = nieuw

    def insert(self, x, index):
        nieuw = Node(x)
        if index <= 0 or not self.head:
            nieuw.next = self.head
            self.head = nieuw
            return
        huidig = self.head
        prev = None
        i = 0
        while huidig and i < index:
            prev = huidig
            huidig = huidig.next
            i += 1
        prev.next = nieuw
        nieuw.next = huidig

    def __str__(self):
        waarden = []
        huidig = self.head
        while huidig:
            waarden.append(str(huidig.data))
            huidig = huidig.next
        return " -> ".join(waarden)


# 5. Bibliotheek

class Bibliotheek:
    def __init__(self, naam):
        self.naam = naam
        self.beschikbaar = LinkedList()
        self.geleend = Stack()

    def voeg_toe(self, boek):
        self.beschikbaar.append(boek)

    def leen(self):
        # haal eerst boek (head) uit beschikbaar
        if self.beschikbaar.head is None:
            return None
        boek = self.beschikbaar.head.data
        self.beschikbaar.remove(boek)
        self.geleend.push(boek)
        return boek

    def overzicht(self):
        # maak dict auteur -> aantal boeken beschikbaar
        d = {}
        huidig = self.beschikbaar.head
        while huidig:
            auteur = huidig.data.auteur
            d[auteur] = d.get(auteur, 0) + 1
            huidig = huidig.next
        return d


# Voorbeeld gebruik:

b1 = Boek("Python Basis", "Jan", 120)
b2 = Boek("Geavanceerd Python", "Marie", 200)
b3 = Boek("Python voor Data", "Jan", 150)

bib = Bibliotheek("Stadsbibliotheek")
bib.voeg_toe(b1)
bib.voeg_toe(b2)
bib.voeg_toe(b3)

geleend_boek = bib.leen()
print(geleend_boek.titel)  # bv "Python Basis"

print(bib.overzicht())  # bv {"Marie": 1, "Jan": 1}
