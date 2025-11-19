class Session:
    def __init__(self, team, trainer, field, timeslot):

        self.team = team
        self.trainer = trainer
        self.field = field
        self.timeslot = timeslot

    def __str__(self):

        return f"{self.team} → {self.timeslot} with {self.trainer} on {self.field}"

    def conflicts_with(self, other_session):

        if self.timeslot != other_session.timeslot:
            return False  # verschillend tijdstip, geen conflict

        # conflict bij dezelfde trainer of hetzelfde field
        if self.trainer == other_session.trainer or self.field == other_session.field:
            return True

        return False

# Deel 2 – testen van de klasse
def main():
    # Voorbeeldsessions
    s1 = Session("U10", "Sara", "Field 1", "Mon 18-19")
    s2 = Session("U12", "Tom", "Field 2", "Wed 19-20")
    s3 = Session("U14", "Sara", "Field 1", "Mon 18-19")  # voor conflict test

    # Sla de sessies op in een lijst
    schedule = [s1, s2, s3]

    # Print alle sessies
    print("Planning van sessies:")
    for session in schedule:
        print(session)

    # Test conflicts_with
    print("\nConflict tests:")
    print(f"{s1} conflicts with {s2}? {s1.conflicts_with(s2)}")  # False
    print(f"{s1} conflicts with {s3}? {s1.conflicts_with(s3)}")  # True

# Main aanroepen
if __name__ == "__main__":
    main()
