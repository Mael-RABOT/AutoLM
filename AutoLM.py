from datetime import datetime
date = datetime.today().strftime('%d/%m/%Y')
jobTitle = input("What is the job title: ")
entrepriseName = input("What is the entreprise name: ")
adress = input("What is the adress: ")
city = input("What is the city and the postal code: ")
file_name = "LM_" + entrepriseName + ".txt"
with open('LM.txt', 'r') as f_in, open(file_name, 'w') as f_out:
    for line in f_in:
        line = line.replace('[ENTREPRISE]', entrepriseName)
        line = line.replace('[DATE]', date)
        line = line.replace('[TITLE]', jobTitle)
        line = line.replace('[ADRESS]', adress + "\n" + city)
        f_out.write(line)