class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def addFirst(self, e):
        newNode = Node(e)
        newNode.next = self.__head

        if self.__head is not None:
            self.__head.prev = newNode
        else:
            self.__tail = newNode  # lijst was leeg

        self.__head = newNode
        self.__size += 1

    def addLast(self, e):
        newNode = Node(e)
        newNode.prev = self.__tail

        if self.__tail is not None:
            self.__tail.next = newNode
        else:
            self.__head = newNode

        self.__tail = newNode
        self.__size += 1

    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.addFirst(e)
            return
        if index == self.__size:
            self.addLast(e)
            return

        newNode = Node(e)

        current = self.__head
        for _ in range(index):
            current = current.next

        previous = current.prev

        newNode.next = current
        newNode.prev = previous
        previous.next = newNode
        current.prev = newNode

        self.__size += 1

    def removeFirst(self):
        if self.__size == 0:
            return None

        temp = self.__head.element
        self.__head = self.__head.next

        if self.__head is not None:
            self.__head.prev = None
        else:
            self.__tail = None

        self.__size -= 1
        return temp

    def removeLast(self):
        if self.__size == 0:
            return None

        temp = self.__tail.element
        self.__tail = self.__tail.prev

        if self.__tail is not None:
            self.__tail.next = None
        else:
            self.__head = None

        self.__size -= 1
        return temp

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

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")

        current = self.__head
        for _ in range(index):
            current = current.next
        return current.element
    
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of bounds")

        current = self.__head
        for _ in range(index):
            current = current.next

        old = current.element
        current.element = e
        return old

