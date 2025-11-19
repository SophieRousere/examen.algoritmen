def is_valid_session(new_session, schedule):
    """
    Controleert of new_session geen conflict veroorzaakt met bestaande planning.
    """
    for session in schedule:
        if new_session.conflicts_with(session):
            return False
    return True


def plan_trainings(teams, i, schedule, trainers, fields, timeslots):
    """
    Probeert alle teams in te plannen via backtracking.

    teams: lijst van teams
    i: huidige positie in teams
    schedule: lijst van Session objecten (huidige planning)
    trainers, fields, timeslots: beschikbare resources
    """
    if i == len(teams):
        # Stopconditie: alle teams zijn ingepland
        return True

    team = teams[i]

    # Probeer alle mogelijke combinaties
    for timeslot in timeslots:
        for trainer in trainers:
            for field in fields:
                new_session = Session(team, trainer, field, timeslot)
                if is_valid_session(new_session, schedule):
                    # Session toevoegen
                    schedule.append(new_session)
                    # Recursief verder met volgend team
                    if plan_trainings(teams, i + 1, schedule, trainers, fields, timeslots):
                        return True
                    # Backtrack: verwijder de session
                    schedule.pop()
    # Geen enkele combinatie werkt voor dit team
    return False

def create_schedule(teams, trainers, fields, timeslots):
    """
    Creëert een planning en print resultaat.
    """
    schedule = []

    if plan_trainings(teams, 0, schedule, trainers, fields, timeslots):
        print("Geldige planning gevonden:")
        for session in schedule:
            print(session)
    else:
        print("Geen geldige planning mogelijk.")

def main():
    # CSV-bestanden inlezen
    teams = read_csv_single_column("teams.csv", "Team")
    trainers = read_csv_single_column("trainers.csv", "Trainer")
    fields = read_csv_single_column("fields.csv", "Field")
    timeslots = read_csv_single_column("timeslots.csv", "Timeslot")

    # Lijsten printen en valideren
    print(f"Teams: {teams}")
    print(f"Trainers: {trainers}")
    print(f"Fields: {fields}")
    print(f"Timeslots: {timeslots}\n")

    if not validate_not_empty("Teams", teams) or \
       not validate_not_empty("Trainers", trainers) or \
       not validate_not_empty("Fields", fields) or \
       not validate_not_empty("Timeslots", timeslots):
        print("Programma stopt vanwege lege inputlijsten.")
        return

    # Planning maken
    create_schedule(teams, trainers, fields, timeslots)


# Main aanroepen
if __name__ == "__main__":
    main()
