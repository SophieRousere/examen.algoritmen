# The function for sorting elements in ascending order (Simplified Version)
def selectionSort(lst):
    for i in range(len(lst) - 1):  #lijst start bij i = 0
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i : ]) #lijst begint bij i en gaat tot einde
        currentMinIndex = i + lst[i: ].index(currentMin) #+i want index in volledige lijst
        #index(currentMin) zoekt de positie van de minimumwaarde binnen die sublijst
        
        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
            # lijstposities = waarden
            
def main():
    lst = [-2, 4.5, 5, 1, 2, -3.3]
    selectionSort(lst)
    print(lst)

main()