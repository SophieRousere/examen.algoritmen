def dubbel(lijst):
    # Tel hoe vaak elk getal voorkomt
    telling = {}
    for getal in lijst:
        if getal in telling:
            telling[getal] += 1
        else:
            telling[getal] = 1

    # Zoek het getal dat precies twee keer voorkomt
    for getal in telling:  # getal is de key
        if telling[getal] == 2:
            return getal

    # andere methode: for getal, count in telling.items():
    # if count == 2:
    # return getal

    return None


def dubbels(lijst):
    telling = {}  # (getal, aantal keer dat getal voorkomt)
    for getal in lijst:
        if getal in telling:
            telling[getal] += 1
        else:
            telling[getal] = 1

    uniek = set()  # 2 sets aanmaken
    dubbel = set()

    for getal in telling:
        if telling[getal] == 1:  # count == 1
            uniek.add(getal)
        else:
            dubbel.add(getal)

    return uniek, dubbel
