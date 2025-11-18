class TaskNode:
    """Node representing a task in the linked list."""  # Beschrijving van de klasse

    def __init__(self, task_name, duration, priority):
        self.task_name = task_name      # Naam van de taak opslaan in de node
        self.duration = duration        # Duur van de taak opslaan
        self.priority = priority        # Prioriteit van de taak opslaan
        self.next = None                # Verwijzing naar de volgende node (standaard None)


class TaskLinkedList:
    """Linked list to manage tasks in the production line."""  # Beschrijving van de lijst

    def __init__(self):
        self.head = None                # Begin van de linked list (nog geen nodes)

    def add_task(self, task_name, duration, priority):
        """Add a new task to the end of the list."""
        new_node = TaskNode(task_name, duration, priority)  # Nieuwe node maken

        if not self.head:              # Als de lijst leeg is
            self.head = new_node       # Nieuwe node wordt de head
        else:
            current = self.head        # Start bij begin van de lijst
            while current.next:        # Zolang er een volgende node is
                current = current.next # Ga verder naar de volgende node
            current.next = new_node    # Voeg nieuwe node op het einde toe

    def remove_task(self, task_name):
        """Remove a task by its name."""
        current = self.head            # Start bij de eerste node
        previous = None                # Houdt bij wat de vorige node is

        while current and current.task_name != task_name:
            previous = current         # Update previous pointer
            current = current.next     # Ga naar de volgende node

        if not current:                # Taak niet gevonden
            print(f"Task '{task_name}' not found.")
            return

        if not previous:               # Als de te verwijderen taak de head is
            self.head = current.next   # Head verschuift naar volgende node
        else:
            previous.next = current.next  # Verbind node ervoor met node erna

    def display_tasks(self):
        """Display all tasks in the linked list."""
        current = self.head            # Start bij de eerste node
        while current:
            print(f"Task: {current.task_name}, Duration: {current.duration}, Priority: {current.priority}")
            current = current.next     # Ga naar de volgende node

    def find_task(self, task_name):
        """Find a task by its name."""
        current = self.head            # Begin bij head
        while current:
            if current.task_name == task_name:   # Vergelijk naam
                return f"Task: {current.task_name}, Duration: {current.duration}, Priority: {current.priority}"
            current = current.next     # Volgende node
        return f"Task '{task_name}' not found."  # Niet gevonden

    def calculate_total_duration(self):
        """Calculate the total duration of all tasks."""
        total_duration = 0             # Start op 0
        current = self.head
        while current:
            total_duration += current.duration   # Duur optellen
            current = current.next     # Naar volgende node
        return total_duration          # Totale duur teruggeven

    def read_tasks_from_csv(self, file_path):
        """Read tasks from a CSV file and add them to the linked list."""
        import csv                     # CSV-module importeren
        with open(file_path, 'r') as file:  # Bestanden openen
            reader = csv.reader(file)       # CSV-reader maken
            next(reader)                    # Header overslaan
            for row in reader:              # Door elke rij gaan
                task_name, duration, priority = row  # Waarden uitlezen
                self.add_task(task_name, int(duration), int(priority))  # Toevoegen aan lijst

    def reorder_tasks_by_priority(self):
        """Reorder tasks based on priority."""
        sorted_head = None             # Nieuwe gesorteerde lijst start leeg
        current = self.head            # Begin bij originele lijst

        while current:
            next_node = current.next   # Bewaar volgende node
            sorted_head = self.sorted_insert_by_priority(sorted_head, current)  # Insert sort
            current = next_node        # Ga verder

        self.head = sorted_head        # Gesorteerde lijst wordt nieuwe head

    def reorder_tasks_by_priority_duration(self):
        """Reorder tasks based on priority and then duration."""
        sorted_head = None             # Start nieuwe lijst
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.sorted_insert_by_priority_duration(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert_by_priority(self, head, node):
        """Helper method to insert node based on priority."""
        if not head or node.priority < head.priority:  # Als nieuwe node eerst moet komen
            node.next = head
            return node

        current = head
        while current.next and current.next.priority <= node.priority:
            current = current.next     # Zoek plaats waar node moet komen

        node.next = current.next       # Plaats node tussen current en volgende
        current.next = node
        return head

    def sorted_insert_by_priority_duration(self, head, node):
        """Helper method to insert node based on priority and duration."""
        if not head or \
           (node.priority < head.priority or
            (node.priority == head.priority and node.duration < head.duration)):
            node.next = head           # Node moet vooraan komen
            return node

        current = head
        while current.next and \
              (current.next.priority < node.priority or
               (current.next.priority == node.priority and current.next.duration <= node.duration)):
            current = current.next     # Zoek correcte plek

        node.next = current.next       # Insert node
        current.next = node
        return head
