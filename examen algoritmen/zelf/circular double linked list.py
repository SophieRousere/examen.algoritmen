class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    # Add element at the beginning
    def addFirst(self, e):
        newNode = Node(e)
        if self.__head is None:  # empty list
            newNode.next = newNode
            newNode.prev = newNode
            self.__head = newNode
        else:
            tail = self.__head.prev
            newNode.next = self.__head
            newNode.prev = tail
            tail.next = newNode
            self.__head.prev = newNode
            self.__head = newNode
        self.__size += 1

    # Add element at the end
    def addLast(self, e):
        if self.__head is None:
            self.addFirst(e)
            return
        newNode = Node(e)
        tail = self.__head.prev
        newNode.next = self.__head
        newNode.prev = tail
        tail.next = newNode
        self.__head.prev = newNode
        self.__size += 1

    # Add element at a specific index
    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.addFirst(e)
            return
        if index == self.__size:
            self.addLast(e)
            return
        current = self.__head
        for _ in range(index):
            current = current.next
        previous = current.prev
        newNode = Node(e)
        newNode.next = current
        newNode.prev = previous
        previous.next = newNode
        current.prev = newNode
        self.__size += 1

    # Remove first element
    def removeFirst(self):
        if self.__size == 0:
            return None
        removed = self.__head.element
        if self.__size == 1:
            self.__head = None
        else:
            tail = self.__head.prev
            self.__head = self.__head.next
            self.__head.prev = tail
            tail.next = self.__head
        self.__size -= 1
        return removed

    # Remove last element
    def removeLast(self):
        if self.__size == 0:
            return None
        tail = self.__head.prev
        removed = tail.element
        if self.__size == 1:
            self.__head = None
        else:
            prevNode = tail.prev
            prevNode.next = self.__head
            self.__head.prev = prevNode
        self.__size -= 1
        return removed

    # Remove element at specific index
    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.removeFirst()
        if index == self.__size - 1:
            return self.removeLast()
        current = self.__head
        for _ in range(index):
            current = current.next
        previous = current.prev
        nxt = current.next
        previous.next = nxt
        nxt.prev = previous
        self.__size -= 1
        return current.element

    # Get element at specific index
    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")
        current = self.__head
        for _ in range(index):
            current = current.next
        return current.element

    # Set element at specific index and return old value
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")
        current = self.__head
        for _ in range(index):
            current = current.next
        old = current.element
        current.element = e
        return old

    # Check if element ex
