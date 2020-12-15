# Scheduler - Organizer 

class Organizer():
    """
    Class for Organizing Schedule for Store and its Employees.
    Its takes in the shift times,
    amount of employees and their data (availability, types, and preferences),
    and Store's pattern for scheduling to create a weekly schedule.
    """
    def __init__(self, store):
        self.store = store
        self.pattern = self.store.pattern
        self.week = self.store.week_days

        self._create_shifts()

    def _create_shifts(self):
        """
        Creates Empty Arrary for managing schedules.
        :return: None
        """
        store = self.store
        self.shifts = store._shift_times
        self.employees = store._employees
        employees_per_shift = 1

        shift_schedule = [[[None for employees in range(employees_per_shift)]
                            for shift in self.shifts] for day in self.week]

        print_shifts(shift_schedule)




def print_shifts(array):
    for num, day in enumerate(array):
        print(f'{week[num]}')
        for pos, shift in enumerate(day):
            print(f'\tShift {pos}: ', end='')
            print_employees(shift)

def print_employees(shift):
    for employee in shift:
        print(f'{employee}')
