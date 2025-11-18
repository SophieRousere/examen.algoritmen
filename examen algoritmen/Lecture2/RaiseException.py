def getArea(radius):  #functie die opp v cirkel berekent
    if radius < 0:
        raise RuntimeError("Negative radius")  #zelf in code error gooien
    
    return radius * radius * 3.1415

try:
    print(getArea(5)) #gwn passeren, w juist uitgevoerd
    print(getArea(-5))
except RuntimeError:  #catch toegevoegd v runtime error
    print("Invalid radius")
