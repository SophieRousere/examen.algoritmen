# Clear the list
def clear(self):
    self.__head = None
    self.__tail = None
    self.__size = 0


# Return true if this list contains the element e
def contains(self, e):
    current = self.__head
    while current is not None:
        if current.element == e:
            return True
        current = current.next
    return False


# Remove the element e (first occurrence) and return true if found
def remove(self, e):
    if self.__size == 0:
        return False

    # Speciaal geval: element zit in de head
    if self.__head.element == e:
        self.__head = self.__head.next
        self.__size -= 1

        # Als er maar 1 element was, tail moet ook aangepast worden
        if self.__size == 0:
            self.__tail = None
        return True

    # Ander geval: element zit verder in de lijst
    previous = self.__head
    current = self.__head.next

    while current is not None:
        if current.element == e:
            previous.next = current.next
            self.__size -= 1
            if current == self.__tail:      # als we de laatste verwijderen
                self.__tail = previous
            return True

        previous = current
        current = current.next

    return False  # niet gevonden


# Return the element at the specified index
def get(self, index):
    if index < 0 or index >= self.__size:
        raise IndexError("Index out of bounds")

    current = self.__head
    for i in range(index):
        current = current.next #eentje opschuiven, tot gene index

    return current.element


# Return the index of the first matching element, or -1 if no match
def indexOf(self, e):
    current = self.__head
    index = 0
    while current is not None:
        if current.element == e:
            return index
        current = current.next
        index += 1
    return -1


# Return the index of the last matching element, or -1 if no match
def lastIndexOf(self, e):
    current = self.__head
    index = 0
    lastIndex = -1

    while current is not None:
        if current.element == e:
            lastIndex = index  #huidige index invullen op laatste positie, telkens overschrijven als je volgende vindt
        current = current.next
        index += 1

    return lastIndex


# Replace the element at the specified index with e
def set(self, index, e):
    if index < 0 or index >= self.__size:
        raise IndexError("Index out of bounds")

    current = self.__head
    for i in range(index):
        current = current.next  #doorgaan tot node vd index

    old = current.element
    current.element = e
    return old
