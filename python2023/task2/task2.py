import csv
import unittest
CSV_FILE_NAME = 'salaries_clean.csv'
id = 1654
class Employee:
    def __init__(self, name, surname, age, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job

    @staticmethod
    def show_employees():
        data=[]
        for employee in employees:
            data.append(f"{employee.name} {employee.surname}: {employee.age} -> {employee.job.title}")
        return data

class Employer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @staticmethod
    def show_employers():
        for employer in employers:
            print(f"Name: {employer.name} - Location: {employer.location}")

class Job:
    def __init__(self, id, title, category, rank, salary, employer):
        self.id = id
        self.title = title
        self.category = category
        self.rank = rank
        self.salary = salary
        self.employer = employer

    @staticmethod
    def show_all_jobs():
        data=[]
        for job in jobs:
            data.append(f"{job.title} ({job.employer.name}): {job.salary}")
        return data

    def calculate_average_salary(self):
        total_salary = 0.0
        count = 0

        for job in jobs:
            if job.title == self.title:
                if job.salary!='':
                    total_salary += float(job.salary)
                else:
                    total_salary=0

                count += 1

        if count > 0:
            if total_salary!=0:
                average_salary = round(total_salary / count,2)
            else:
                average_salary='Missing data'
            return average_salary
        else:
            return 0

    def add_job(self,id,title,category,rank,salary,employer):
        #Create new object job
        new_job = Job(id,title,category,rank,salary,employer)
        
        jobs.append(new_job)

        with open(CSV_FILE_NAME,'a',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                new_job.id,
                ',',
                new_job.employer.name,
                new_job.employer.location,
                ',',',',',',',',
                new_job.title,
                new_job.category,
                new_job.rank,
                ',',',',
                new_job.salary,
                ',',',',',',',',','                
            ])

            print("New job added to CSV file")

    def delete_job(id_job_to_delete):
        for job in jobs:
            if job.id == id_job_to_delete:
                jobs.remove(job)

        with open(CSV_FILE_NAME, 'r',encoding="utf8") as file:
            reader = csv.reader(file)
            id_job_to_delete=id_job_to_delete + 1
            rows = list(reader)
        print ("The job has been successfully removed.")

        # Eliminar la fila deseada de la lista de listas
        row_to_delete = id_job_to_delete # índice de la fila que desea eliminar
        del rows[row_to_delete]

        # Sobrescribir el archivo CSV con la nueva lista de listas
        with open(CSV_FILE_NAME, 'w',encoding="utf8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def sow_jobs_for_employeer(employer_name):
            employer_jobs = set()
            for job in jobs:
                if job.employer.name == employer_name:
                    employer_jobs.add(job.title)
            employer_jobs=sorted(employer_jobs)
            if len(employer_jobs)>0:
                for title in employer_jobs:
                    print(title)
            else:
                print("There are no jobs for this employer")

employers=[]
jobs=[]
employees=[]


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

def add_employees():
    employee1=Employee("Luis","Patiño",23,jobs[25])
    employees.append(employee1)
    employee2=Employee("Ibai","Llanos",29,jobs[1512])
    employees.append(employee2)
    employee3=Employee("Beatriz","García",21,jobs[11])
    employees.append(employee3)
    employee4=Employee("Perxita","Perxas",32,jobs[777])
    employees.append(employee4)
    employee5=Employee("Ten","Gris",26,jobs[666])
    employees.append(employee5)

def main(id):
        data = csv_read()
        id=id+1
        
        while True:
            print("\nChoose an option:")
            print("1. Show list of employers.")
            print("2. Show list of jobs.")
            print("3. Show list of jobs foer each employer.")
            print("4. Show average salary for job.")
            print("5. Delete a job.")
            print("6. Add new job.")
            print("7. Show list of employees.")
            print("8. Exit.")
            
            option = input("\nPlease select an option (1-8): ")
            
            if option == "1":
                Employer.show_employers()

            elif option == "2":
                data=Job.show_all_jobs()
                for datos in data:
                    print(datos)

            elif option == "3":
                employer_name = input("Please enter the name of an employer: ")
                Job.sow_jobs_for_employeer(employer_name)
                

            elif option == "4":
                set_jobs=set(jobs)
                for job in set_jobs:
                    print(job.title, job.calculate_average_salary())

            elif option == "5":
                
                id_job_to_delete = int(input("Please enter the job id of the job you want to delete: "))
                Job.delete_job(id_job_to_delete)

            elif option == "6":
                name = input("Please enter the name of the new employer: ")
                location = input("Please enter the new employer's location: ")
                new_employer = Employer(name, location)

                title = input("Please enter the job title: ")
                category = input("Please enter the job category: ")
                rank = input("Please enter the job rank: ")
                salary = input("Please enter the job salary: ")
                new_job = Job(id, title, category, rank, salary, new_employer)
                new_job.add_job(new_job.id, new_job.title, new_job.category, new_job.rank, new_job.salary, new_job.employer)

                
                print(f"\nTe employeer '{name}' has been successfully added.")

            elif option == "7":
                add_employees()
                data=Employee.show_employees()
                for datos in data:
                    print(datos)

            elif option == "8":
                print("\nSee you!")
                break
            else:
                print("\nPlease select a valid option (1-5).")


class TestSalary(unittest.TestCase):
    def test_calculate_average_salary(self):
        jobs.clear()
        employers.clear()
        prueba=Employer('Luis','Vilna')
        employers.append(prueba)

        job1= Job(1,'Developer','Dev','Senior',500,employers[0])
        job2= Job(2,'Developer','Dev','Junior',150,employers[0])
        job3= Job(3,'Developer','Dev','Student',250,employers[0])

        jobs.append(job1)
        jobs.append(job2)
        jobs.append(job3)

        for job in jobs:
                    avg_salary=(job.calculate_average_salary())

        self.assertEqual(avg_salary, 300.0)
    
    def test_add_job(self):
        jobs.clear()
        employers.clear()
        prueba=Employer('Luis','Vilna')
        employers.append(prueba)
        new_job = Job(1,'Developer','Dev','Senior',500,employers[0])
        new_job.add_job(new_job.id, new_job.title, new_job.category, new_job.rank, new_job.salary, new_job.employer)
        assert len(jobs) == 1

    def test_delete_job(self):
        jobs1=[]
        employers1=[]
        jobs1.clear()
        employers1.clear()
        prueba1=Employer('Luis','Vilna')
        employers1.append(prueba1)
        new_job1 = Job(1,'Developer','Dev','Senior',500,employers[0])
        new_job1.add_job(new_job1.id, new_job1.title, new_job1.category, new_job1.rank, new_job1.salary, new_job1.employer)
        Job.delete_job(1)
        assert len(jobs1) == 0

    def test_show_jobs(self):
        job1= Job(1,'Developer','Dev','Senior',250,employers[0])
        employee1=Employee("Luis","Patiño",23,jobs[1])
        employees.append(employee1)
        data=Job.show_all_jobs()
        self.assertEqual(data[0], 'Developer (Luis): 150')
        
    def test_show_employees(self):
        employees.clear()
        job1= Job(1,'Developer','Dev','Senior',500,employers[0])
        employee1=Employee("Luis","Patiño",23,jobs[1])
        employees.append(employee1)
        self.assertEqual(Employee.show_employees(),['Luis Patiño: 23 -> Developer'])          

if __name__ == '__main__':
    main(id)
    #unittest.main()


