# The function for finding a key in the list 
def linearSearch(lst, key):
    for i in range(len(lst)): 
        if key == lst[i]:  #element op positie i vd lijst
            return i
    return -1 #dit pas hier zetten en niet met else onder de if, je moet eerst volledige lijst afgaan

def main():
    lst = [4, 5, 1, 2, 9, -3]
    print(linearSearch(lst, 2))
    
main()  #Roept de main-functie aan zodat het programma start