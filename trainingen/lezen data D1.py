# Helperfunctie om een lijst te reinigen: spaties verwijderen, lege waarden overslaan, duplicaten verwijderen
def clean_list(lst):
    cleaned = []
    seen = set()
    for item in lst:
        item = item.strip()
        if item and item not in seen:
            cleaned.append(item)
            seen.add(item)
    return cleaned


# Functie om een CSV-kolom in te lezen
def read_csv_single_column(path, column_name):
    values = []
    bestand = open(path,"r")
    lines = bestand.readlines()

    if not lines:
        return []

    # Header verwerken
    header = lines[0].strip().split(",")
    if column_name not in header:
        print(f"Kolom '{column_name}' bestaat niet in het bestand.")
        return []
    col_index = header.index(column_name)

    # Overige regels
    for line in lines[1:]:
        parts = line.strip().split(",")
        if col_index < len(parts):
            values.append(parts[col_index])

    # Lijst reinigen met helperfunctie
    return clean_list(values)


# Helper om te controleren of een lijst niet leeg is
def validate_not_empty(name, lst):
    if not lst:
        print(f"Fout: {name} is leeg!")
        return False
    return True


if __name__ == "__main__":
    # Bestanden en bijbehorende kolomnamen
    files = [
        ("teams.csv", "Team"),
        ("trainers.csv", "Trainer"),
        ("fields.csv", "Field"),
        ("timeslots.csv", "Timeslot")
    ]

    # Lijsten opslaan in een dictionary voor overzicht
    data_lists = {}

    # Inlezen en testen
    for path, col_name in files:
        lst = read_csv_single_column(path, col_name)
        print(f"{col_name}: {lst}")  # inhoud van de lijst printen
        data_lists[col_name] = lst

        # Controleren of de lijst niet leeg is
        if not validate_not_empty(col_name, lst):
            print(f"Foutmelding: {col_name} is leeg! Programma stopt.")
