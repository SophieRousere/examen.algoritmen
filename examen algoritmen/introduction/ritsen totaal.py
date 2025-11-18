def samenvoegen(lijst1, lijst2):
    """
    Beurtelings en paarsgewijs samenvoegen van twee reeksen.
    Stoppen bij het einde van de kortste lijst.
    """
    # zip stopt automatisch bij het einde van de kortste lijst
    nieuwelijst = [item for paar in zip(lijst1, lijst2) for item in paar]
    return nieuwelijst


def weven(lijst1, lijst2):
    """
    Beurtelings en paarsgewijs samenvoegen van twee reeksen.
    Stoppen bij het einde van de langste lijst.
    De kortste lijst wordt herhaald via modulo.
    """
    nieuwelijst = []
    lengte1 = len(lijst1)
    lengte2 = len(lijst2)
    max_lengte = max(lengte1, lengte2)

    for i in range(max_lengte):
        # gebruik modulo om in de kortste lijst terug te gaan naar begin
        nieuwelijst.append(lijst1[i % lengte1])         # % geeft rest vd deling
        nieuwelijst.append(lijst2[i % lengte2])
        #i = 1, lengte = 3, i % lengte = 1 % 3 = 0 en rest is 1

    return nieuwelijst


def ritsen(lijst1, lijst2):
    nieuwelijst = []
    min_lengte = min(len(lijst1), len(lijst2))

    # 1. Voeg beurtelings elementen toe tot einde kortste lijst #kan ook via zip()
    for i in range(min_lengte):
        nieuwelijst.append(lijst1[i])
        nieuwelijst.append(lijst2[i])

    # 2. Voeg de resterende elementen van de langste lijst toe
    if len(lijst1) > min_lengte:
        nieuwelijst.extend(lijst1[min_lengte:])
    if len(lijst2) > min_lengte:
        nieuwelijst.extend(lijst2[min_lengte:])

    return nieuwelijst
