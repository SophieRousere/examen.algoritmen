def woorden_splitsen(txt):
    file = open(txt, "r")  # "r" argument leest het nog niet, da's gwn om te zorgen da je het kan lezen
    inhoud = file.read()
    woorden = inhoud.split()  # splitst string op witruimtes : spaties, tabs (\t), nieuwe regels (\n)

    gestript = []

    for woord in woorden:  # overloopt elk elment in de lijst woorden (zoals for line in inputfile)
        woordzondertekens = woord.strip('?.!,:;()')
        gestript.append(woordzondertekens)
    return gestript