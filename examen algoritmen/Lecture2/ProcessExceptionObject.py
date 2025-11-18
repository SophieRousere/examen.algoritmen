try:
    number = float(input("Enter a number: "))  #fout bij omzetten v float
    print("The number entered is", number)  #hier nt geraakt
except ValueError as ex:  #value error: weten: als je iets wil inlezen en omzetten nr float en hij kan het niet
    print("Exception:", ex)


