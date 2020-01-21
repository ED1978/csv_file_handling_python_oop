import csv
from employee import Employee

with open("employees.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    all_employees = []

    for row in reader:
        row = [column.strip().replace('"', "") for column in row]
        current_employee = Employee(*row)
        all_employees.append(current_employee)

with open("employees.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    new_employee = ("Jenny", "Jones", 12.50, 40, 0)

    writer.writerow(new_employee)
