
class Node:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def add_task(self, task_name, duration, priority):
        newNode = Node(task_name, duration, priority)

        if self.tail == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1

    def remove_task(self, task_name):

        if self.size == 0:
            return False

        if self.head.task_name == task_name:
            self.head = self.head.next
            self.size -=1

            if self.size ==0:
                self.tail = None

            return True

        previous = self.head
        current = self.head.next

        while current is not None:  #gene die we verwijderen
            if current.task_name == task_name:
                previous.next = current.next  #gene ervoor verwijst nr gene erna
                self.size -=1
                if current == self.tail:
                    self.tail = previous
                return True

            previous = current
            current = current.next  # <-- essentieel!

        return False

    def display_tasks(self):
            result = "["

            current = self.head  # starten bij 1e node
            while current != None:
                result += f"({current.task_name}, {current.duration}min, p={current.priority})"  # gene in node geven
                current = current.next  # nr volgende node gaan
                if current != None:
                    result += ", "  # Separate two elements with a comma

            result += "]"  # Insert the closing ] in the string

            return result

    def find_task(self,task_name):
        current = self.head
        while current != None:
            if current.task_name == task_name:
                return f"Task: {current.task_name}, Duration: {current.duration}, Priority: {current.priority}"
            current = current.next

        return f"Task '{task_name}' not found."

    def calculate_total_duration(self):
        current = self.head
        duration = 0

        while current != None:
            duration += current.duration
            current = current.next

        return duration

    def read_tasks_from_csv(self, file_path):
        file = open(file_path, "r")
        inhoud = file.readlines()
        for taak in inhoud:
            taak = taak.strip("\n")  #Verwijdert de newline \n aan het einde van de regel.
            opdracht = taak.split(",")  #lijst
            self.add_task(opdracht[0], int(opdracht[1]), int(opdracht[2]))

    def reorder_tasks_by_priority(self):
        current = self.head
        inpoet = None  # nieuwe lege gesorteerde lijst: tijdelijke nieuwe linkedlist

        while current is not None:
            inpoet = self.sorted_insert_by_priority(inpoet, current)  # current is huidige node, doe je vr al de nodes
            current = current.next

        gesorteerd = LinkedList()
        while inpoet is not None:
            gesorteerd.add_task(inpoet.task_name, inpoet.duration, inpoet.priority)
            inpoet = inpoet.next
        return gesorteerd

    def sorted_insert_by_priority(self, head, node):  #head is gesorteede lijst die we opbouwen
        newNode = Node(node.task_name, node.duration, node.priority)

        if head is None: #lijst leeg
            head = newNode
            return head

        #nieuwe node vóór de huidige head moet
        if newNode.priority < head.priority:
            newNode.next = head
            head = newNode
            return head


        previous = head
        while previous.next is not None and newNode.priority > previous.next.priority:  #door ketting lopen tot juiste positie
            previous = previous.next

        if previous.next is None:  #achteraan toevoegen
            previous.next = newNode
        else:
            current = previous.next  #ih midden toevoegen
            previous.next = newNode
            newNode.next = current
        return head


    def reorder_tasks_by_priority_duration(self):
        inpoet = None
        current = self.head
        while current is not None:
            inpoet = self.sorted_insert_by_priority_duration(inpoet, current)
            current = current.next
        resultaat = LinkedList()
        while inpoet is not None:
            resultaat.add_task(inpoet.task_name, inpoet.duration, inpoet.priority)
            inpoet = inpoet.next
        return resultaat

    def sorted_insert_by_priority_duration(self, head, node):
        newNode = Node(node.task_name, node.duration, node.priority)

        if head is None:
            head = newNode
            return head
        if newNode.priority < head.priority:
            newNode.next = head
            head = newNode
            return head
        if newNode.priority == head.priority:
            if newNode.duration < head.duration:
                newNode.next = head
                head = newNode
                return head

        previous = head
        while previous.next is not None and newNode.priority > previous.next.priority:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
            return head

        while previous.next is not None and previous.next.priority == newNode.priority and newNode.duration > previous.next.duration:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
        else:
            temp = previous.next
            previous.next = newNode
            newNode.next = temp
        return head















