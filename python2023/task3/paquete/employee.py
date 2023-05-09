employees=[]
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
    
    def add_employees(jobs):
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
