def samenvoegen(lijst1, lijst2):
    nieuwelijst = [item for paar in zip(lijst1, lijst2) for item in paar]
    return nieuwelijst

# zip() combineert twee of meer lijsten element voor element tot paren (tuples).
#Beurtelings en paarsgewijs samenvoegen van twee reeksen.

# Het stopt automatisch bij het einde van de kortste lijst.

"#for paar in zip(...) → loop over elk paar."
"for item in paar → haal elk item uit dat paar."