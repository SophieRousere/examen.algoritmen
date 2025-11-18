def bubbleSort(lst):
    needNextPass = True  #standaard als true
    
    k = 1
    while k < len(lst) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(lst) - k):    #tot lengte - k, want die op het einde staan al goed
            if lst[i] > lst[i + 1]:
                # swap lst[i] with lst[i + 1]
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
          
                needNextPass = True # Next pass still needed, je hebt geswapt dus moet je opnieuw lijst afgaan
        k +=1
def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")

main()
