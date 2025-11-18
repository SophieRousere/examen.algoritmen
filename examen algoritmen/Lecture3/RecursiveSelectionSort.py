def sort(lst):
    sortHelper(lst, 0, len(lst) - 1) # Sort the entire lst

def sortHelper(lst, low, high):
    if low < high:
        # Find the smallest number and its index in lst[low .. high]
        indexOfMin = low;
        min = lst[low];  #eerst gwn et laagste, eerste als min doen
        for i in range(low + 1, high + 1): #echte minimum zoeken
            if lst[i] < min:  #als je i vindt dat waarde < 1e getal
                min = lst[i] #1e getal wordt minimum
                indexOfMin = i

        # Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low]  #gene op plek v minimum vervangen door eerste
        lst[low] = min #gene op 1e plek vervangen door minimum

        # Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high)   #recursieve oproep!!! low +1 en dan zelfde doen

def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)

main()
