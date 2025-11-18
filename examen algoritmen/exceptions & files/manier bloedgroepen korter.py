def bloedgroep_kind(vader, moeder):
    # mogelijke allelen
    ABO = {'A':['A','O'], 'B':['B','O'], 'AB':['A','B'], 'O':['O','O']}
    Rh = {'+':['+','-'], '-':['-','-']}

    def abo_fenotype(a1, a2):
        if 'A' in [a1, a2] and 'B' in [a1, a2]: return 'AB'
        if 'A' in [a1, a2]: return 'A'
        if 'B' in [a1, a2]: return 'B'
        return 'O'

    mogelijk = set()
    for a1 in ABO[vader[:-1]]:
        for a2 in ABO[moeder[:-1]]:
            for r1 in Rh[vader[-1]]:
                for r2 in Rh[moeder[-1]]:
                    rh = '+' if '+' in [r1,r2] else '-'
                    mogelijk.add(abo_fenotype(a1,a2) + rh)
    return mogelijk
