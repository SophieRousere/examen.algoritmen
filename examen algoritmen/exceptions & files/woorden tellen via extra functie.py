def woorden_splitsen(tekst):
    file = open(tekst, "r")
    inhoud = file.read()
    inhoudenkelspaties = replacePunctuations(inhoud)
    gesplit = inhoudenkelspaties.split()
    return gesplit


def replacePunctuations(inhoud):
    for ch in inhoud:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':  # is character speciaal teken: maak er spatie van
            inhoud = inhoud.replace(ch, " ")

    return inhoud


def woorden_tellen(tekst):
    words = woorden_splitsen(tekst)

    dictionary = {}

    for word in words:  # woorden een vr een toevoegen
        word = word.lower()
        if word in dictionary:
            dictionary[word] += 1  # als woord al in dictionary zit: value +1
        else:
            dictionary[word] = 1  # zit het er nog niet in: nieuw woord toevoegen en op 1 zetten
    return dictionary