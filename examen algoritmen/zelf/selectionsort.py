def SelectionSort(lijst):
    for i in range(len(lijst)-1):
        minimum = min(lijst[i:])  #!
        indexminimum = i + lijst[i:].index(minimum) #!!

        if indexminimum != i:
            lijst[indexminimum], lijst[i] = lijst[i], minimum