def mergeSort(list):
    if len(list) > 1:
        #lijst in twee delen en beide delen sorteren
        # Merge sort the first half
        firstHalf = list[ : len(list) // 2]  #firsthalf = nieuwe lijst aangemaakt
        mergeSort(firstHalf)

        # Merge sort the second half
        secondHalf = list[len(list) // 2 : ]
        mergeSort(secondHalf)

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, list)  #!belangrijk dat je ze in juiste volgorde mergt

# Merge two sorted lists */
def merge(list1, list2, temp): #zoals oefn ritsen: 2 lijsten gesorteerd bijeenvoegen
    #opslaan in temp, temp = het resultaat
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2):  #even lange lijsten
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]  #element uit lijst 1 toevoegen aan nieuwe lijst
            current1 += 1
            current3 += 1  #resultatenlijst + 1
            #deze currents zijn indexen, dus deze verschuiven
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]  ##deze op einde nog erachter plaatsen
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2] #op einde nog een vr een eraan toevoegen
        current2 += 1
        current3 += 1

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(list)
    for v in list:
        print(v, end = " ")

main()
 
