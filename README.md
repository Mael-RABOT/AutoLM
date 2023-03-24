# AutoLM
Automaticaly create your cover letter

---

# How to use
Add to the repository a file called 'LM.txt'

To launch the program, just use
> python3 AutoLM.py

Then, the program will ask you question about the entreprise, currently they are:

- Job title
- Entreprise name
- Entreprise adress
- Entreprise city and postal code

> Be carefull to not put the postal code inside the adress

---

# File format

To file a field with an information, you have to write one of the operator below directly in the 'LM.txt' file

- [ENTREPRISE]
- [DATE]
- [ADDRESS]
- [TITLE]

---

# Advanced usage

If you want to make a lot of cover letter, you can pass an excel file in argument

> python3 AutoLM.py job_info.xlsx

The xlsx file need to have the following field

| jobTitle  | entrepriseName | address | city |
|-----------|----------------|---------|------|
