import csv
CSV_FILE_NAME = 'salaries_clean.csv'
class Job:
    def __init__(self, id, title, category, rank, salary, employer):
        self.id = id
        self.title = title
        self.category = category
        self.rank = rank
        self.salary = salary
        self.employer = employer

    @staticmethod
    def show_all_jobs(jobs):
        data=[]
        for job in jobs:
            data.append(f"{job.title} ({job.employer.name}): {job.salary}")
        return data

    def calculate_average_salary(self,jobs):
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

    def add_job(self,id,title,category,rank,salary,employer,jobs):
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

    def delete_job(id_job_to_delete,jobs):
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

    def show_jobs_for_employeer(employer_name,jobs):
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