class JournalLine:
    def __init__(self, account, debit=0.0, credit=0.0, description=""):
        self.account = account
        self.description = description

        # bedragen worden afgerond op 2 decimalen
        self.debit = round(float(debit), 2)
        self.credit = round(float(credit), 2)

        # Exact één zijde moet gevuld zijn
        if (self.debit > 0 and self.credit > 0) or (self.debit == 0 and self.credit == 0):
            raise ValueError("A JournalLine must be either debit OR credit, not both or none.")

    def is_debit(self):
        return self.debit > 0

    def is_credit(self):
        return self.credit > 0


class JournalEntry:
    def __init__(self, date, reference, description=""):
        self.date = date
        self.reference = reference
        self.description = description
        self.journal_lines = []

    def add_JournalLine(self, line):
        if not isinstance(line, JournalLine):
            raise TypeError("Must add a JournalLine object.")
        self.journal_lines.append(line)

    def total_Debit(self):
        return round(sum(line.debit for line in self.journal_lines), 2)

    def total_Credit(self):
        return round(sum(line.credit for line in self.journal_lines), 2)

    def in_balance(self):
        return self.total_Debit() == self.total_Credit()

    def validate(self):
        if len(self.journal_lines) < 2:
            raise ValueError("A JournalEntry must contain at least 2 journal lines.")
        if all(not line.is_debit() for line in self.journal_lines):
            raise ValueError("No debit line found.")
        if all(not line.is_credit() for line in self.journal_lines):
            raise ValueError("No credit line found.")
        if not self.in_balance():
            raise ValueError("Journal entry is not balanced.")

    def __str__(self):
        header = (
            f"Date: {self.date}   Ref: {self.reference}\n"
            f"Description: {self.description}\n"
            "------------------------------------------------------------\n"
            "Account                Type       Amount  Description\n"
            "------------------------------------------------------------"
        )

        lines_str = ""
        for line in self.journal_lines:
            type_str = "DEBIT" if line.is_debit() else "CREDIT"
            amount = line.debit if line.is_debit() else line.credit
            lines_str += f"\n{line.account:<22} {type_str:<10} {amount:8.2f}  {line.description}"

        footer = (
            "\n------------------------------------------------------------\n"
            f"Total debit :    {self.total_Debit():.2f}\n"
            f"Total credit:    {self.total_Credit():.2f}\n"
            f"Balanced    : {'YES' if self.in_balance() else 'NO'}"
        )

        return header + lines_str + footer


# Test: verkoopfactuur boeken
entry = JournalEntry("2025-09-02", "INV-1001", "Credit sale incl. VAT 21%")

entry.add_JournalLine(JournalLine("7000", credit=1000.00, description="Sales revenue"))
entry.add_JournalLine(JournalLine("VAT payable", credit=210.00, description="VAT 21%"))
entry.add_JournalLine(JournalLine("Accounts Receivable", debit=1210.00))

entry.validate()

print(entry)
