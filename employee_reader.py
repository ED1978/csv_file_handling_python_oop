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

# with open("employees.csv", "a") as csvfile:
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#
#     new_employee = ("Jenny", "Jones", 12.50, 40, 0)
#
#     writer.writerow(new_employee)

with open("employees.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["first_name", "last_name", "hourly_rate", "hours_worked", "amount_due"])

    for employee in all_employees:
        employee.amount_due = float(employee.hours_worked) * float(employee.hourly_rate)
        writer.writerow(employee.values())
