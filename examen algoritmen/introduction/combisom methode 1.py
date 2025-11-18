def combisom (lijst,som):
    lengte = len(lijst)
    for i in range (lengte):
        for j in range(i+1, lengte):
            if lijst[i] + lijst[j] == som:
                return True
    return False

"i loopt over alle indices van de lijst. j begint een plek na i (i+1), en loopt tot het einde. "
"i = 0 → lijst[i] = 1"

"j = 1 → lijst[j] = 2 → 1+2=3 ≠ 5"

"j = 2 → lijst[j] = 3 → 1+3=4 ≠ 5"

"j = 3 → lijst[j] = 4"