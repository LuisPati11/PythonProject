import csv
CSV_FILE_NAME = 'salaries_clean.csv'

from paquete.employer import Employer
from paquete.job import Job

employers=[]
jobs=[]

def csv_read():
    with open(CSV_FILE_NAME, encoding="utf8", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:

            # Creamos un objeto Empresa y lo agregamos al diccionario de empresas
            employer = Employer(row['employer_name'],row['location_name'])
            employers.append(employer)

            # Creamos un objeto Trabajo y lo agregamos a la lista de trabajos
            job = Job(row['index'], row['job_title'], row['job_title_category'], row['job_title_rank'], row['annual_base_pay'], employer)
            jobs.append(job)

    return employers,jobs