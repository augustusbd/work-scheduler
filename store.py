# Scheduler - Store & Employee

class Store():
    open_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    affirmative = ['yes', 'y', 'ya']

    def __init__(self, name, store_ID):
        self._name = name
        self._ID = store_ID


    def setup_simple(self):
        """
        Simple Setup for data entry.
        """
        self.total_employees = 5

        self._create_datasets()
        self._add_shift_times_simple()
        self._add_employees_simple()
        self._add_organizer()

    def _create_datasets(self):
        """
        Create datasets for store:
            Shift Times Data
            Employee Data
            Organizer Data
        """
        # Store's Shift Times
        with open(f'.\data\{self._name}_shifts.txt', 'w+') as shift_times:
            shift_times.write(f'{self._name} {self._ID} SHIFTS\n')

        # Store's Employees Data
        with open(f'.\data\{self._name}_employees.txt', 'w+') as employees_data:
            employees_data.write(f'{self._name} {self._ID} EMPLOYEES\n')
            employees_data.write('EMPLOYEE FORMAT: [id] [fname] [lname]')

        # Store's Organizer Data
        with open(f'.\data\{self._name}_organizer.txt', 'w+') as organizer:
            organizer.write(f'{self._name} {self._ID} ORGANIZER\n')
            organizer.write('PATTERN:   SINE || SAWTOOTH || STEP-FUNCTION || ALTERNATE')

    def _add_shift_times_simple(self):
        self._shift_times = {}
        shift_amt = 3
        # Shifts: 5AM to 2PM; 9AM to 6PM; 11AM to 8PM
        shifts = [[5, 2], [9, 6], [11, 8]]

        for shift in range(len(shifts)):
            self._shift_times[shift+1] = shifts[shift]
            print(f'Shift {shift}: {start}AM to {end}PM')

        self._save_shifts()

    def _add_employees_simple(self):
        self._employees = [f'Employee 00{x+1}' for x in range(self.total_employees)]
        self._save_employees()

    def _add_organizer(self):
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
        print('Choose pattern: SINE or SAWTOOTH or STEP-FUNCTION or ALTERNATE')
        self.pattern = 'sawtooth'
        # choice = input('Choose pattern: SINE or SAWTOOTH or STEP-FUNCTION or ALTERNATE: ')
        # self.pattern = choice

        import organizer as ORG
        self.organizer = ORG.Organizer(self)

    def _save_shifts(self):
        """
        Saves inputted shift times into general data file.
        :return: None
        """
        shifts = self._shift_times
        start, end = 0, 1
        with open(f'.\data\{self._name}_shifts.txt', 'a+') as shift_times:
            for shift in shifts:
                # EX:   Shift 1: 5AM to 2PM
                shift_times.write(f'Shift {shift}: {shifts[shift][start]}AM to {shifts[shift][end]}PM\n')
        return None

    def _save_employees(self):
        """
        Saves inputted employee information into general data file.
        :return: None
        """
        employees = self._employees
        first, last = 0, 1
        with open(f'.\data\{self._name}_employees.txt', 'a+') as employees_data:
            employees_data.write('EMPLOYEES: [id]  [first name]  [last name]\n')
            for id in range(len(employees)):
                # EX: 0 Morty Smith
                employees_data.write(f'{id} {employees[id][first]} {employees[id][last]}\n')
        return None

    def _save_schedule(self):
        """
        Saves schedule created by Organizer.
        :return: None
        """
        pass



class Employee():
    def __init__(self, employee_id, full_name):
        self.ID = employee_id
        self.name = full_name
        self.hours_per_week = 40
        #first_name, last_name = full_name[0], full_name[-1]

        #self._store = store
        #self._title = 'Worker'
        #self._position_type = 'Temporary'

        self.setup_employee()

    def setup_employee(self):
        """
        Setup Employee Preferences
        :return: None
        """
        self.edit_total_hours()
        self.edit_availability()
        #self.edit_priority()
        # priority will be based on employee id
        # lowest ID number is #1 priority

    def edit_total_hours(self):
        """
        Automatically temporary until changed (TBD).
        Choose part-time, full-time, temporary, or contract.
        :return: None
        """
        self.hours_per_week = input(f"Enter total hours per week for {self.name}: ")


    def edit_availability(self):
        """
        Set availability for employee.
        A dictionary containing each day as key and times as value.

        Later, this can be inputted through a table.
        :return: None
        """
        blurb = """
                Enter available times during open days. Enter in 12 hour format.
                Earliest time then latest time.
                If you are unavailable on a specific day, put 'NA'.
                """
        print(blurb)

        self.availability = {}
        for day in self.open_days:
            earliest = input(f"Enter earliest availability for {day}: ")
            latest = input(f"Enter latest availability for {day}: ")
            self.availability[day] = (earliest, latest)

        self.list_availability()



    def request_off(self):
        pass

    def list_availability(self):
        for day in self._availability:
            print(f"{day}: {self._availability[day][0]}AM to {self._availability[day][1]}PM")

    # RETURN VALUES FOR EMPLOYEE
