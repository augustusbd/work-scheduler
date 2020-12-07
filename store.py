week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
affirmative = ['yes', 'y', 'ya']

class Store():
    def __init__(self, name, store_ID):
        self._name = name
        self._ID = store_ID

    def setup_simple(self):
        """
        Simple Setup for data entry.
        """
        self._create_datasets()
        self._add_shift_times_simple()
        self._add_employees_simple()
        self._add_schedule_pattern()

    def _create_datasets(self):
        """
        Create datasets for store:
            Shift Times Data
            Employee Data
            Organizer Data
        """
        with open(f'.\data\{self._name}_shifts.txt', 'w+') as general:
            general.write(f'{self._name} {self._ID} SHIFTS\n')

        with open(f'.\data\{self._name}_employees.txt', 'w+') as employee:
            employee.write(f'{self._name} {self._ID} EMPLOYEES\n')
            employee.write("EMPLOYEE FORMAT: [id] [fname] [lname]")

        with open(f'.\data\{self._name}_organizer.txt', 'w+') as organizer:
            organizer.write(f'{self._name} {self._ID} ORGANIZER\n')
            organizer.write('PATTERN:   SINE || SAWTOOTH || STEP-FUNCTION || ALTERNATE')

    def _add_shift_times_simple(self):
        self._shift_times = {}
        shift_amt = 3
        # Shifts: 5AM to 2PM; 9AM to 6PM; 11AM to 8PM
        shifts = [[5, 2], [9, 6], [11, 8]]

        for shift in range(1, shift_amt+1):
            start, end = shifts[shift-1]
            self._shift_times[shift] = [start, end]
            print(f'Shift {shift}: {start}AM to {end}PM')

        self._save_shifts()

    def _add_employees_simple(self):
        self._employees = {}
        employee_amt = 3    # amount of employees
        names = ['Morty Smith', 'Summer Smith', 'Rick Sanchez']

        for id in range(employee_amt):
            print(f'Employee ID: {id} {names[id]}')
            first, last = names[id].split(' ')
            self._employees[id] = [first, last]

        self._save_employees()

    def _add_schedule_pattern(self):
        """
        Get schedule pattern for store.
        Ex: Have scheduling snake across times per day.
            Like, Employee A gets Shift 1 on Monday
             then Employee A gets Shift 2 on Tuesday
             then Employee A gets Shift 3 on Wednesday
             then Employee A gets off day
             then Employee A gets Shift 1 on Friday....
        So, have different mathematical functions guide scheduling
        arrangement.
        (Sawtooth Wave for above; Sine Waves & Step Functions also work)
        :return:
        """
        pass

    def _save_shifts(self):
        """
        Saves inputted shift times into general data file.
        :return: None
        """
        shifts = self._shift_times
        start, end = 0, 1
        with open(f'.\data\{self._name}_shifts.txt', 'a+') as general:
            for shift in shifts:
                # EX:   Shift 1: 5AM to 2PM
                general.write(f'Shift {shift}: {shifts[shift][start]}AM to {shifts[shift][end]}PM\n')
        return None

    def _save_employees(self):
        """
        Saves inputted employee information into general data file.
        :return: None
        """
        employees = self._employees
        first, last = 0, 1
        with open(f'.\data\{self._name}_employees.txt', 'a+') as general:
            general.write('EMPLOYEES: [id]  [first name]  [last name]\n')
            for id in range(len(employees)):
                # EX: 0 Morty Smith
                general.write(f'{id} {employees[id][first]} {employees[id][last]}\n')
        return None

    def _save_schedule(self):
        """
        Saves schedule created by Organizer.
        :return: None
        """
        pass



class Employee():
    def __init__(self, first_name, last_name, employee_id,
                 store, title='Worker', position='TEMPORARY'):
        self._name = [first_name, last_name]
        self._ID = employee_id

        self._store = store
        self._title = title
        self._position_type = position
        self._setup_employee()

    def _setup_employee(self):
        """
        Setup Employee Preferences
        :return: None
        """
        self._edit_position()
        self._edit_availability()
        self._edit_priority()

    def _edit_position(self):
        """
        Automatically temporary until changed (TBD).
        Choose part-time, full-time, temporary, or contract.
        :return: None
        """
        self._position_type = input("Part-time, Full-Time, Temporary, or Contract: ")

        if self._position_type in 'FULL-TIME':
            self._hours_per_week = 40
        elif self._position_type in 'PART-TIME':
            self._hours_per_week = 30
        elif self._position_type in 'TEMPORARY':
            self._hours_per_week = 35
        else: # Contract position
            self._hours_per_week = 40

    def _edit_availability(self):
        """
        Set availability for employee.
        A dictionary containing each day as key and times as value.

        Later, this can be inputted through a table.
        :return: None
        """
        self._availability = {}
        for day in week:
            self._availability[day] = input(f"Enter availability for {day}'s': ")
        self.list_availability()

    def _edit_priority(self):
        """
        Set the employee's priority in scheduling.
        Ranking:
            High
            Med
            Low - default
        """
        self._priority = 'Low'


    def _request_off(self):
        pass

    def list_availability(self):
        for day in self._availability:
            print(f"{day}: {self._availability[day]}")

    def priority(self):
        return self._priority
    def availability(self):
        return self._availability
    def name(self):
        return f"{self._name[0]} {self._name[1]}"
    def first(self):
        return self._name[0]
    def last(self):
        return self._name[1]
    def id(self):
        return self._ID
    def position(self):
        """
        **Find a way to put Title, Position Type, and Hours together**
        :return:
        """
        return f"{self._position_type} with {self._hours_per_week} hours per week"
    def title(self):
        return self._title



def divider():
    return "==================================\n"
