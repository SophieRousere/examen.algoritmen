class LinkedList:  #linkedlist is een class

    #creeert lege linked list
    def __init__(self):  #vertrekken met head en tail
        self.__head = None   #lege lijst
        self.__tail = None
        self.__size = 0   #gwn om bij hte houden hoeveel elementen in lijst zitten

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:  #controle niet nul is
            return None
        else:
            return self.__head.element  #return head en daarvan element: verwijst nr 1e node
        #return het element dat in head staat
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head: nieuwe node verwijst nr de oorspr head
        #nieuwe next gaat pointer krijgen nr huidige head
        self.__head = newNode # head points to the new node
        #bestaande head moet verwijzen nr newnode
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head #enigste: dan tail wel aanpassen want dan verwees die nog nr none

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None: #nieuw element toevoegen als er nog geen in lijst zat
            self.__head = self.__tail = newNode # The only node in list
        else:
            #zoals dia 12
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
             #nieuwe tail wordt tailnext
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)


#met index: complexer
    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle !!! dia 17
            #zoeken welke plaats je het zal toevoegen: current die door lijst loopt
            current = self.__head   #current is verwijzing nr node, we starten met 1e: head
            for i in range(1, index): #telkensn v 1 tem plek index tot index-1
                # nr volgende node gaan tot current eindigt bij node op plek voor we willen invoegen
                current = current.next  #soort v pointer die je toevoegt die nr node gaat verwijzen, daar moet hij komen
                #current gaat bepalen: hier moet hij komen
            temp = current.next  #sla op waar current.next naar wijst
           #(= de node die NA de nieuwe node zal komen) #ertussen plaatsen, even opslaan naar waar current verwijst, dus wat de volgende node is
            #temp = erin wordt volgende node opgeslaan
            current.next = Node(e)   #current next aanpassen door nieuwe node: nieuwe node ertussenplaatsen
            (current.next).next = temp  #de next van nieuwe node(current.next) een waarde geven = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None:   #als er gn meer achter eerste staat
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element  #element die in node temp zat
        else:
            current = self.__head  #start bij de eerste

            for i in range(self.__size - 2):
                current = current.next  # voorlaatste node
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next  #= verplaats pointer nr de volgende
                # #previous= zoekt gene voor waar je index wil verwijderen
        
            current = previous.next  #current is node die je wil verwijderen
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):  #lijst v alle elementen
        result = "["

        current = self.__head  #starten bij 1e node
        for i in range(self.__size):
            result += str(current.element)   #gene in node geven
            current = current.next      #nr volgende node gaan
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element o 
    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    # Return the element from this list at the specified index 
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
#blngr van hier
class Node:
    def __init__(self, e): #constructor die werkt met zijn element
        #maak paar aan, 2 elementen waar 1e verwijst nr value en 2e nr none
        self.element = e
        self.next = None  #blngr tot hier

#iterator niet zo belangrijk
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    
        