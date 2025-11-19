import random

class DobbelWorp:
    def __init__(self, aantal):
        self.aantal = aantal
        self.waarden = [0] * aantal              # actuele waarden
        self.constant_mask = [False] * aantal    # True = niet meer gooien

    def __str__(self):
        lijst = []
        for i in range(self.aantal):
            if self.constant_mask[i]:
                lijst.append(-self.waarden[i])    # negatieve weergave
            else:
                lijst.append(self.waarden[i])
        return str(lijst)

    def nieuwe_worp(self):
        for i in range(self.aantal):
            if not self.constant_mask[i]:
                self.waarden[i] = random.randint(1, 6)

    def __isub__(self, waarde):
        """
        Zoek de *eerste* dobbelsteen (laagste index) die:
        - nog niet constant is
        - de waarde 'waarde' toont
        Markeer deze steen als constant.
        """
        for i in range(self.aantal):
            if not self.constant_mask[i] and self.waarden[i] == waarde:
                self.constant_mask[i] = True
                break
        return self

    def aantal_beurten(self, k, m):
        """
        Gooi totdat er minstens k dobbelstenen waarde m tonen.
        Deze dobbelstenen worden telkens constant gezet.
        Return: aantal beurten die nodig waren.
        """
        beurt = 0

        while True:
            beurt += 1
            self.nieuwe_worp()

            # markeer alle stenen met waarde m als constant
            for i in range(self.aantal):
                if self.waarden[i] == m:
                    self.constant_mask[i] = True

            # tel hoeveel stenen waarde m hebben
            aantal_m = sum(
                1 for i in range(self.aantal) if self.waarden[i] == m
            )

            if aantal_m >= k:
                return beurt
