class Employee:
    def __init__(self, first_name, last_name, hourly_rate, hours_worked, amount_due):
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.amount_due = amount_due

    def values(self):
        return [self.first_name, self.last_name, self.hourly_rate, self.hours_worked, self.amount_due]
