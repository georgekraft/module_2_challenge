import sys
import fire
import questionary
from pathlib import Path
import csv

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
        Modular function imported into app.py

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    
    answer = questionary.text("Would you like to save your qualifying loans?").ask()

    if answer == 'Yes' or 'yes' or 'YES' or 'Y' or 'y':
        file_path = questionary.text("Enter a file path to save_qualifying_loans():").ask()
        csvpath = Path(file_path)
        with open(csvpath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for row in qualifying_loans:
                csvwriter.writerow(row)
    else:
        print("Since you didn't answer Yes to saving your qualifying loans, they have not been saved.")