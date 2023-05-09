import csv

from readCSV import csv_read

from paquete.employer import Employer
from paquete.employee import Employee
from paquete.job import Job

data=csv_read()
employers=data[0]
jobs=data[1]

CSV_FILE_NAME = 'salaries_clean.csv'
id = 1654
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
                Employer.show_employers(employers)

            elif option == "2":
                data=Job.show_all_jobs(jobs)
                for datos in data:
                    print(datos)

            elif option == "3":
                employer_name = input("Please enter the name of an employer: ")
                Job.show_jobs_for_employeer(employer_name,jobs)
                

            elif option == "4":
                set_jobs=set(jobs)
                for job in set_jobs:
                    print(job.title, job.calculate_average_salary(jobs))

            elif option == "5":
                
                id_job_to_delete = int(input("Please enter the job id of the job you want to delete: "))
                Job.delete_job(id_job_to_delete,jobs)

            elif option == "6":
                name = input("Please enter the name of the new employer: ")
                location = input("Please enter the new employer's location: ")
                new_employer = Employer(name, location)

                title = input("Please enter the job title: ")
                category = input("Please enter the job category: ")
                rank = input("Please enter the job rank: ")
                salary = input("Please enter the job salary: ")
                new_job = Job(id, title, category, rank, salary, new_employer)
                new_job.add_job(new_job.id, new_job.title, new_job.category, new_job.rank, new_job.salary, new_job.employer,jobs)

                
                print(f"\nTe employeer '{name}' has been successfully added.")

            elif option == "7":
                Employee.add_employees(jobs)
                data=Employee.show_employees()
                for datos in data:
                    print(datos)

            elif option == "8":
                print("\nSee you!")
                break
            else:
                print("\nPlease select a valid option (1-5).")

if __name__ == '__main__':
    main(id)