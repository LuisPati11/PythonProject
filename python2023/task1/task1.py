# Luis Patiño (VU 2023)
#Task1
import csv
from itertools import groupby
from colorama import Fore, Style

# Gloabl variables
i=1

# Read csv file
while True:
    try:
        filename = input("Enter the name of the CSV file: ")
        with open(filename,encoding="utf8",newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            data = [row for row in reader]
            total=len(data)
        break
    except FileNotFoundError:
        print(Fore.RED + "The file has not been found. Please enter a valid file name." + Style.RESET_ALL)
        
# Get the column by which we are going to group
while True: 
    option=input("By which column do you want to group the file? \n a) Job Title \n b) Employer name \n Type 'a' or 'b' and press enter \n")
    if option == 'a':
        A_index = headers.index('job_title')
        break
    elif option == 'b':
        A_index = headers.index('employer_name')
        break
    else:
        print(Fore.RED + "You can only enter a or b" + Style.RESET_ALL)

# Ask the user how many rows they want to display
while True:
    respuesta = input("¿Desea elegir el número de filas a mostrar? (y/n) ")
    if respuesta.lower() == 'y':
        while True:
            try:
                row_count = int(input("How many rows do you want to display? "))
                if row_count > 0:
                    break
                else:
                    print(Fore.RED + "Please enter a positive integer." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter a valid integer." + Style.RESET_ALL)
        break
    elif respuesta.lower() == 'n':
        row_count=-1
        break
    else:
        print(Fore.RED + "Por favor, introduzca 'y' o 'n'." + Style.RESET_ALL)

# Sort data by by the column chosen by the user
sorted_data = sorted(data, key=lambda x: x[A_index])
# Group data by value of column by the column chosen by the user
groups = []
for index, rows in groupby(sorted_data, key=lambda x: x[A_index]):
    groups.append(list(rows))

# Loop through file to get total number of rows by group
    result = []
    for group in groups:
        index = group[0][A_index]
        count = len(group)
       
        result.append((index, count))

    # Sort the result list in descending order by count
    result.sort(key=lambda x: x[1], reverse=True)

while True:
    option=input("What calculation do you want to do: \n 1) Rowcount \n 2) Row count percentage of all rows \n 3) Average value of C \n Type 1, 2 or 3 and press enter \n")
    if option == '1':
        # Print the results in descending order
        for r in result[:row_count]:
            print(f"Group: {r[0]} {Fore.GREEN}({r[1]} rows):{Style.RESET_ALL}")
        break

    elif option == '2':
        # Print the results in descending order
        for r in result[:row_count]:
            print(f"Group: {r[0]} {Fore.GREEN}({round(r[1]/total*100,4)}% of all rows):{Style.RESET_ALL}")
        break
    
    elif option == '3':
        # Calculate averages and add to result list
        C_index = headers.index('annual_base_pay')
        for group in groups:
            index = group[0][A_index]
            values = []
            for row in group[:row_count]:
                if not row[C_index]:  # if empty or None
                    values.append(0)
                else:
                    values.append(float(row[C_index]))
            average = sum(values) / len(values)
            result.append((index, average))
        # Sort the result list in descending order by average value
        result.sort(key=lambda x: x[1], reverse=True)
        # Print the results in descending order
        for r in result:
            print(f"Group: {r[0]} {Fore.GREEN}Average Salary: {r[1]}{Style.RESET_ALL}")
        break