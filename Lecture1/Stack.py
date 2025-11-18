class Stack:
    def __init__(self):
        self.__elements = []
#meerdere operaties die bij stack horen
    # Return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0   #stack is leeg als lijst leeg is, lengte lijst = 0 ==> true retourneren
    
    # Returns the element at the top of the stack 
    # without removing it from the stack. #kijken wat bovenaanstaat zonder eraf te halen
    def peek(self):
        if self.isEmpty():
            return None  #lege lijst, none retourneren
        else:
            return self.__elements[len(self.__elements) - 1] #retourneren wat op einde v lijnst staat

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value) #append v element id lijst

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop() #pop functie in lijst
    
    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)