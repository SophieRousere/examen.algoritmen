def combisom(lijst, som):
    # lijst omzetten naar een verzameling
    verzameling = set()  # begint met lege set

    # voor elk getal uit de lijst naagaan of zijn partnerterm in de verzameling voorkomt
    for x in lijst:
        if som - x in verzameling:
            return True
        else:
            verzameling.add(x)
    return False