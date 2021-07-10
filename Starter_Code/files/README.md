# Loan Qualifier for Consumers

This app allows the creation of a list of bank loans for which a consumer qualifies based on the consumer's information, e.g. such as credit score, monthly income or debt.  

---

## Technologies

The app was written in python using VScode as editor. A number of libraries were imported into the app incl. sys, fire, questionary, Path, csv. 

---

## Usage and Examples

The app is run from app.py and starts by a terminal prompt for the file path from where the bank rates are read from (../data/daily_rate_sheet.csv)
![Screenshot (8)](https://user-images.githubusercontent.com/85372363/125171791-e930bb00-e16a-11eb-9b35-a2bb0fbb9cb9.png)

After the consumer's information (credit score, monthly debt, monthly income, requested loan value, home value) are entered into terminal prompts, 
the qualifying loans are written into a 'qualifying_loans' csv file (../data/qualifying_loans.csv)
![Screenshot (9)](https://user-images.githubusercontent.com/85372363/125171952-d1a60200-e16b-11eb-9f69-9fa57f26fe82.png)


---

## Contributors

This was project coded by George Kraft into a code framework provided by a FinTech bootcamp.

---

## License

This project is public on github under georgekraft/module_2_challenge
