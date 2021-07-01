def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
        Modular function imported into app.py

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    csvpath = Path("qualifying_loans.csv")
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in qualifying_loans:
            csvwriter.writerow(row.values())