def combisom(lijst, doelsom):
    # lijst sorteren
    gesorteerde_lijst = sorted(lijst)

    # mogeijke termen van som bepalen
    i = 0
    j = len(lijst) - 1
    while i != j:
        som = gesorteerde_lijst[i] + gesorteerde_lijst[j]
        if som == doelsom:
            return True
        elif som < doelsom:
            i += 1
        else:
            j -= 1 #som is te groot, gesorteerde lijst dus 1tje kleiner
    # geen termen die som opleveren
    return False