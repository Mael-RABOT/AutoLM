from datetime import datetime
import os
import pandas as pd
import sys


def create_path(path) -> None:
    os.mkdir(path)


def check_dir() -> None:
    path = "Results"
    if not os.path.exists(path):
        create_path(path)


def create_lm(job_title="", entreprise_name="", address="", city=""):
    date = datetime.today().strftime('%d/%m/%Y')
    if job_title == "":
        job_title = input("What is the job title: ")
    if entreprise_name == "":
        entreprise_name = input("What is the entreprise name: ")
    if address == "":
        address = input("What is the address: ")
    if city == "":
        city = input("What is the city and the postal code: ")

    file_name = "Results/LM_" + entreprise_name + ".txt"
    pdf_name = "Results/LM_" + entreprise_name + ".pdf"
    with open('LM.txt', 'r') as f_in, open(file_name, 'w') as f_out:
        for line in f_in:
            line = line.replace('[ENTREPRISE]', entreprise_name)
            line = line.replace('[DATE]', date)
            line = line.replace('[TITLE]', job_title)
            line = line.replace('[ADDRESS]', address + "\n" + city)
            f_out.write(line)


def excel(path):
    try:
        df = pd.read_excel(path)
        for index, row in df.iterrows():
            create_lm(row['jobTitle'], row['entrepriseName'], row['address'], row['city'])
    except FileNotFoundError:
        print(f"File {path} do not exist")


def main():
    check_dir()
    if len(sys.argv) == 2:
        excel(sys.argv[1])
    else:
        create_lm()


main()
