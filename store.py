week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Store():
    def __init__(self, store_ID):
        self._store_ID = store_ID
        self._setup()

    def _setup(self):
        self._add_employees()
        self._add_store_hours()
        self._add_shift_times()
        self._add_schedule_pattern()

    def _add_employees(self):
        self._employees = []

    def _add_store_hours(self):
        self._store_hours = []

    def _add_shift_times(self):
        self._shift_times = []

    def _add_schedule_pattern(self):
        """
        Get schedule pattern for store.
        Ex: Have scheduling snake across times per day.
            Like, Employee A gets Shift 1 on Monday
             then Employee A gets Shift 2 on Tuesday
             then Employee A gets Shift 3 on Wednesday
             then Employee A gets off day
             then Employee A gets Shift 1 on Friday....
        So, have different mathematical functions determine scheduling
        arrangement. (Sawtooth Wave for above; Sine Wave also works)
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


    def store_ID(self):
        return self._store_ID

    def employees_list(self):
        return self._employees

    def list_employees(self):
        for employee in self._employees:
            print(x)



class Employee():
    def __init__(self, first_name, last_name, employee_id,
                 store=Store(), title='Worker', position='TEMPORARY'):
        self._name = f"{first_name} {last_name}"
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

        if self._position_type is 'FULL-TIME':
            self._hours_per_week = 40
        elif self._position_type is 'PART-TIME':
            self._hours_per_week = 30
        elif self._position_type is 'TEMPORARY':
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
        return self._name
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
