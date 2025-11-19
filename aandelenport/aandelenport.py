class AandelenPortefeuille:
    # Vraag 2: constructor zonder parameters
    def __init__(self):
        self.reader = FileReader()  # FileReader object
        self.portefeuille_map = {}   # dictionary met key -> AandeelData

        # Vul portefeuille_map met alle aandelen uit de reader
        while self.reader.has_next():
            aandeel = self.reader.next()
            key = AandeelData.create_key(aandeel.get_markt(), aandeel.get_ticker())
            self.portefeuille_map[key] = aandeel

    # Vraag 3: controleren of aandeel aanwezig is
    def aandeel_aanwezig(self, markt, ticker):
        key = AandeelData.create_key(markt, ticker)
        return key in self.portefeuille_map

    # Vraag 4: aandeel toevoegen
    def toevoegen_aandeel(self, aandeel):
        key = AandeelData.create_key(aandeel.get_markt(), aandeel.get_ticker())
        if key not in self.portefeuille_map:
            self.portefeuille_map[key] = aandeel
            return True
        return False

    # Vraag 5: aandeel aanpassen
    def aanpassen_aandeel(self, markt, ticker, prijs, aantal):
        key = AandeelData.create_key(markt, ticker)
        if key in self.portefeuille_map:
            aandeel = self.portefeuille_map[key]
            aandeel.prijs = prijs       # update prijs
            aandeel.aantal = aantal     # update hoeveelheid

    # Vraag 6: waarde van aandeel
    def waarde_aandeel(self, markt, ticker):
        key = AandeelData.create_key(markt, ticker)
        if key in self.portefeuille_map:
            aandeel = self.portefeuille_map[key]
            return aandeel.get_prijs() * aandeel.get_aantal()
        return 0.0

    # Vraag 7: totale waarde van portefeuille
    def totale_waarde(self):
        totaal = 0.0
        for aandeel in self.portefeuille_map.values():
            totaal += aandeel.get_prijs() * aandeel.get_aantal()
        return totaal

    # Vraag 8: aandelen van een specifieke markt
    def get_aandelen_markt(self, marktcode):
        return [aandeel for aandeel in self.portefeuille_map.values() if aandeel.get_markt() == marktcode]

    # Vraag 9: aandeel met laagste waarde
    def get_kleinste_aandeel(self):
        if not self.portefeuille_map:
            return None
        # bereken waarde (prijs * aantal) voor elk aandeel
        kleinste = min(self.portefeuille_map.items(), key=lambda kv: kv[1].get_prijs() * kv[1].get_aantal())
        return kleinste[0]  # retourneer de key

    # Vraag 10: rapport printen
    def rapport(self):
        print("Portefeuille")
        print("----------------")
        for aandeel in self.portefeuille_map.values():
            print(f"{aandeel.get_markt()} {aandeel.get_ticker()}  {aandeel.get_prijs()} {aandeel.get_aantal()}")
        print(f"TOTALE WAARDE: {self.totale_waarde():.2f}")
