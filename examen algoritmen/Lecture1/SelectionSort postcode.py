def selectionSortStudents(students):
    for i in range(len(students) - 1):
        # zoek de index van het kleinste postcode vanaf i
        min_index = i

        for j in range(i + 1, len(students)):
            if students[j]["postcode"] < students[min_index]["postcode"]:
                min_index = j  #j verandert telkens, min index blijft index v kleinste element

        # wissel studenten als een kleinere postcode is gevonden
        if min_index != i:
            students[i], students[min_index] = students[min_index], students[i]
            #kleinste wisselen met gene op eerste plek i

    return students


# voorbeeld
students = [
    {"naam": "Anna", "postcode": 3012},
    {"naam": "Bram", "postcode": 2021},
    {"naam": "Sofie", "postcode": 5043},
    {"naam": "Timo", "postcode": 1015}
]

sorted_students = selectionSortStudents(students)
print(sorted_students)
