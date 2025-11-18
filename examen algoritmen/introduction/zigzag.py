def iszigzag(lijst):
    for i in range(len(lijst) - 1):
        if i % 2 == 0:  # even index
            if lijst[i] < lijst[i + 1]:  # moet >= zijn
                return False   #hier false, want eerst alles controleren tegen da je true mag geven
        else:  # oneven index
            if lijst[i] > lijst[i + 1]:  # moet <= zijn
                return False
    return True


def zigzag_traag(lijst):
    # 1. sorteer in place #(mag ook met gesorteerdelijst = sorted(lijst), maar dan ook nog dit lijst[:] = gesorteerdelijst)
    lijst.sort()

    # 2. wissel paren
    for i in range(0, len(lijst) - 1, 2):  # range(start, stop, step)
        lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]


def zigzag_snel(lijst):
    for i in range(0, len(lijst), 2):  # alle even indices

        # check voorgaande element (i-1)
        if i > 0 and lijst[i] < lijst[i - 1]:
            lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]

        # check volgende element (i+1)
        if i + 1 < len(lijst) and lijst[i] < lijst[i + 1]:
            lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]
