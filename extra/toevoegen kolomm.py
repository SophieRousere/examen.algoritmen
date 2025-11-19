class Kolom:
    def __init__(self, naam, data):
        self.naam = naam
        self.data = data[:]   # lijst van floats

    def __str__(self):
        return f"{self.naam}:{self.data}"

    # ------- OPTELLEN -------
    def __add__(self, other):
        # Kolom + Kolom
        if isinstance(other, Kolom):
            nieuwe_data = [self.data[i] + other.data[i] for i in range(len(self.data))]
            nieuwe_naam = f"{self.naam}+{other.naam}"
            return Kolom(nieuwe_naam, nieuwe_data)

        # Kolom + getal
        elif isinstance(other, (int, float)):
            nieuwe_data = [x + other for x in self.data]
            nieuwe_naam = f"{self.naam}+{other}"
            return Kolom(nieuwe_naam, nieuwe_data)

        return NotImplemented

    # getal + Kolom
    def __radd__(self, other):
        return self + other

    # ------- VERMENIGVULDIGEN -------
    def __mul__(self, other):
        # Kolom * Kolom
        if isinstance(other, Kolom):
            nieuwe_data = [self.data[i] * other.data[i] for i in range(len(self.data))]
            nieuwe_naam = f"{self.naam}*{other.naam}"
            return Kolom(nieuwe_naam, nieuwe_data)

        # Kolom * getal
        elif isinstance(other, (int, float)):
            nieuwe_data = [x * other for x in self.data]
            nieuwe_naam = f"{self.naam}*{other}"
            return Kolom(nieuwe_naam, nieuwe_data)

        return NotImplemented

    # getal * Kolom
    def __rmul__(self, other):
        return self * other

class Werkblad:
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.data = []  # lijst van lijsten
        self.kolomnamen = []

        with open(bestandsnaam, "r") as f:
            regels = f.readlines()

        # eerste rij = kolomnamen
        self.kolomnamen = regels[0].strip().split(";")
        if self.kolomnamen[-1] == "":
            self.kolomnamen.pop()

        # volgende rijen = floats (komma → punt)
        for regel in regels[1:]:
            waardes = regel.strip().split(";")
            if waardes[-1] == "":
                waardes.pop()
            rij = [float(x.replace(",", ".")) for x in waardes]
            self.data.append(rij)

    def __str__(self):
        totaal = [self.kolomnamen] + self.data
        return str(totaal)

    def get_aantal_kolommen(self):
        return len(self.kolomnamen)

    # oproepbaar: a(4) → Kolom 4
    def __call__(self, index):
        naam = self.kolomnamen[index]
        kolomdata = [rij[index] for rij in self.data]
        return Kolom(naam, kolomdata)

    # += operator om kolom toe te voegen
    def __iadd__(self, kolom_obj):
        self.kolomnamen.append(kolom_obj.naam)
        # voeg kolomwaarden toe aan elke rij
        for i in range(len(self.data)):
            self.data[i].append(kolom_obj.data[i])
        return self

    # CSV uitschrijven (punt → komma)
    def schrijf(self, bestandsnaam):
        with open(bestandsnaam, "w") as f:
            # schrijf kop
            f.write(";".join(self.kolomnamen) + "\n")

            # schrijf rijen
            for rij in self.data:
                tekst = ";".join(str(x).replace(".", ",") for x in rij)
                f.write(tekst + "\n")
