def samenvoegen(lijst1, lijst2):
    # Bepaal de lengte van de kortste lijst
    min_lengte = min(len(lijst1), len(lijst2))

    # Maak een lege lijst om de resultaten in te bewaren
    nieuwelijst = []

    # Voeg de elementen paarsgewijs toe
    for i in range(min_lengte):
        nieuwelijst.append(lijst1[i])
        nieuwelijst.append(lijst2[i])

    return nieuwelijst