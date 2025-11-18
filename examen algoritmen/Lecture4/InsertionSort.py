
# The function for sorting elements in ascending order
def insertionSort(lst):
    for i in range(1, len(lst)):   #i is geen daje wilt invoegen
        # insert lst[i] into a sorted sublist lst[0..i-1] so that
        #   lst[0..i] is sorted.
        currentElement = lst[i]   #het element dat je wilt invoegen
        k = i - 1           #k is laatste element in gesorteerde, v rechts nr links zoeken waar
        while k >= 0 and lst[k] > currentElement:   #element op k groter dan gene daje wilt invoegen
            lst[k + 1] = lst[k]                   #element op k moet 1 plek nr rechts verschuiven
            k -= 1                                  #1 positie nr links gaan en opnieuw checken

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement


def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    insertionSort(list)
    for v in list:
        print(v, end=" ")


main()