def isISBN13(code):
    if not (
            isinstance(code, str) and  # code moet als string zijn, controleert of het v type string is
            len(code) == 13 and
            code.isdigit()  # eerste negen karakters in de code moeten cijfers zijn
    ):
        return False

    if code[:3] not in {'978', '979'}:  # kijken nr eerste 3 cijfers
        return False

    # controlecijfer berekenen
    controle = 0
    for i in range(12):
        if i % 2 == 1:  # even positie * 3
            controle += 3 * int(code[i])
        else:
            controle += int(code[i])
    controlecijf = controle % 10
    controlecijf = (10 - controlecijf) % 10
    return controlecijf == int(code[-1])


# vanaf hier functie overzicht
# dictionary landcode= key en aantal voorkomens = value

def overzicht(codes):
    # stap 1: lege dictionary
    groepen = {}
    for i in range(11):
        groepen[i] = 0

    # stap 2: tellen
    for code in codes:
        if not isISBN13(code):
            groepen[10] += 1  # fout
        else:
            groepen[int(code[3])] += 1   #pakt het 4e karakter!! , int om het nr getal om te zetten

    # stap 3: printen in jouw stijl
    print('Engelstalige landen: {}'.format(groepen[0] + groepen[1]))  #format zorgt daje {} invult
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    # overige = 6, 8, 9
    print('Overige landen: {}'.format(groepen[6] + groepen[8] + groepen[9]))
    print('Fouten: {}'.format(groepen[10]))
