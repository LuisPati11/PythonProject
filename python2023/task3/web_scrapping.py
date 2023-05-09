from bs4 import BeautifulSoup
import requests
import csv
import concurrent.futures

from paquete.job import Job
from paquete.employer import Employer
from readCSV import csv_read

iterator=1656

def process_job(trabajo, salario, jobs_ws):
    name = "e-voluzion"
    location = "CR"
    new_employer = Employer(name, location)

    title = trabajo
    category = "boss"
    rank = "god"
    salary_job = salario
    new_job = Job(iterator, title, category, rank, salary_job, new_employer)
    new_job.add_job(new_job.id, new_job.title, new_job.category, new_job.rank, new_job.salary, new_job.employer, jobs_ws)

URL = 'https://www.careerprofiles.info/top-100-careers.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)

soup=BeautifulSoup(page.text,'html.parser')

jobs = []
for i in range (0,100):
    job = soup.find_all('td', attrs = {'style': 'text-align: left; padding-left: 2%;'})[i].text
    job = job.replace('\n','')
    job = job.strip()
    jobs.append(job)

salaries = []
for i in range (0,100):
    salary = soup.find_all('td', attrs = {'style': 'vertical-align:middle; text-align: left; padding-left: 2%;'})[i].text
    salary = salary.replace('\n','')
    salary = salary.strip()
    salaries.append(salary)

data = dict(zip(jobs, salaries))

web_CSV = "jobs_web_scrapping.csv"

with open(web_CSV, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Name", "Salary"])
    for jobs, salaries in data.items():
        csv_writer.writerow([jobs, salaries])

jobs_ws = csv_read()[1]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for trabajo, salario in data.items():
        if len(futures) < 25:
            futures.append(executor.submit(process_job, trabajo, salario, jobs_ws))
        else:
            concurrent.futures.wait(futures)
            futures = [executor.submit(process_job, trabajo, salario, jobs_ws)]
        iterator=iterator+1
    concurrent.futures.wait(futures)

