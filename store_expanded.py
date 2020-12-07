week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
affirmative = ['yes', 'y', 'ya']

class Store():
    def __init__(self, name, store_ID):
        self._name = name
        self._ID = store_ID
        self.setup()

    def setup(self):
        self._create_datasets()
        #self._add_store_hours()
        self._add_shift_times()
        self._add_employees()
        self._add_schedule_pattern()

    def read_data_simple(self):
        """
        Simple Setup for data entry.
        """
        with open('.\data\Example_data.txt', 'r') as simple:
            data = simple.read()


    def _create_datasets(self):
        """
        Create datasets for store:
            Shift Times Data
            Employee Data
            Organizer Data
        """
        self._create_shift_data()
        self._create_employee_data()
        self._create_organizer_data()

    def _create_shift_data(self):
        """
        General Data Set.
        :return: None
        """
        with open(f'.\data\{self._name}_shifts.txt', 'w+') as general:
            general.write(f'{self._name} {self._ID} SHIFTS\n')
        return None

    def _create_employee_data(self):
        with open(f'.\data\{self._name}_employees.txt', 'w+') as employee:
            employee.write(f'{self._name} {self._ID} EMPLOYEES\n')
            employee.write("EMPLOYEE FORMAT: [id] [fname] [lname] [position_type] [title] [availability] [priority]\n")

    def _create_organizer_data(self):
        with open(f'.\data\{self.name()}_organizer.txt', 'w+') as organizer:
            organizer.write(f'{self._name} {self._ID)} ORGANIZER\n')
            organizer.write('PATTERN:   SINE || SAWTOOTH || STEP-FUNCTION || ALTERNATE')

    def _update_datasets(self):
        """
        Update datasets of Store.
        """
        pass

    def _save_hours(self):
        """
        Saves inputted opening hours into general data file.
        :return: None
        """
        hours = self._store_hours
        topen, close = 0, 1
        with open(f'.\data\{self._name}_data.txt', 'a+') as general:
            general.write('OPENING HOURS:\n')

            for day in week:
                # EX:   Monday: 7AM to 11PM
                general.write(f'{day}: {hours[day][topen]}AM to {hours[day][close]}PM\n')
            general.write('\n')
            general.write(divider())
        return None

    def _save_shifts(self):
        """
        Saves inputted shift times into general data file.
        :return: None
        """
        shifts = self._shift_times
        start, end = 0, 1
        with open(f'.\data\{self._name}_shifts.txt', 'a+') as general:
            general.write('SHIFT TIMES:\n')
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
        with open(f'.\data\{self._name}_data.txt', 'a+') as general:
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

    def _add_store_hours(self):
        self._store_hours = {}
        exception = input("Are there different opening days? ")
        if exception in affirmative:
            # Ask about different groupings of hours
            # Then input days that open the same,
            #   same opening: [day1] thru [day5]
            #   individual:   [day6] & [day7]
            # input same times first, then individual times
            pass

        # All days have the same opening hours
        else:
            print("Monday thru Sunday:")
            open = input("\t open: ")
            close = input("\tclose: ")
            for day in week:
                self._store_hours[day] = [open, close]

        self._save_hours()
        return None

    def _add_shift_times(self):
        self._shift_times = {}
        self._shift_amt = int(input('\nHow many shifts per day? '))

        for shift in range(1, self._shift_amt+1):
            print(f'Shift {shift}:')
            start = input('\tstart time: ')
            end =   input('\t  end time: ')
            self._shift_times[shift] = [start, end]

        self._save_shifts()

    def _add_employees(self):
        self._employees = []
        employee_amt = input('\nHow many employees in department? ')
        employee_amt = int(employee_amt)

        for id in range(employee_amt):
            print(f'Employee ID: {id}')
            name = input('\t Enter first & last name: ')
            first, last = name.split(' ')
            self._employees.insert(id, [first, last])

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

    def _edit_employee(self):
        """
        Allows Store to edit employee's hours or availability.
        :return: None
        """
        pass

    def _edit_store_hours(self):
        pass

    def _edit_shift_times(self):
        pass

    def _edit_schedule_pattern(self):
        pass

    def name(self):
        return self._name

    def ID(self):
        return self._ID

    def employees_list(self):
        return self._employees

    def list_employees(self):
        for employee in self._employees:
            print(x)



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
