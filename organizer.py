# Scheduler - Organizer

class Organizer():
    """
    Class for Organizing Schedule for Store and its Employees.
    Its takes in the shift times,
    amount of employees and their data (availability, types, and preferences),
    and Store's pattern for scheduling to create a weekly schedule.
    """
    def __init__(self, store):
        # store data
        self.store = store
        self.pattern = store.pattern
        self.week = store.open_days
        self.shifts = store._shift_times

        # employee data
        self.total_employees = store.total_employees
        self.employees = store._employees

        self._create_empty_week()
        self._create_priority_list()

    def _create_empty_week(self):
        """
        Creates Empty Arrary for managing schedules.
        :return: None
        """
        store = self.store
        employees_per_shift = 1

        shift_schedule = [[[None for employees in range(employees_per_shift)]
                            for shift in self.shifts] for day in self.week]

        print_shifts(shift_schedule)


    def schedule(self):
        if 'saw' in self.pattern.lower():
            self._schedule_saw()

        else:
            print("Other patterns not implemented yet.")


    def _schedule_saw(self):
        # use sawtooth pattern for scheduling employees
        pass





def print_shifts(array):
    for num, day in enumerate(array):
        print(f'{week[num]}')
        for pos, shift in enumerate(day):
            print(f'\tShift {pos}: ', end='')
            print_employees(shift)

def print_employees(shift):
    for employee in shift:
        print(f'{employee}')
