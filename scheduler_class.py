# Python Imports
from random import randint

class Scheduler():
    def __init__(self):
        self._weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._headings = [''] + self._weekdays # empty space for axis titles
        self._days = 7
        self.total_shifts = 4
        self.max_employees_per_shift = 4
        #self.setSchedule()


    def _setShiftNumbers(self):
        """
        Determines number of employees per shift.
        :return: None
        """
        self._shift_employees = {}
        for x in range(1, self.total_shifts + 1):
            # self._shift_employees[x] = randint(2, self.max_employees_per_shift)
            self._shift_employees[x] = self.max_employees_per_shift
        return None

    # Sets the employees to a spepcic Shift Block for the day
    def _setShiftBlock(self, shift_pos, day):
        """
        List of employees per shift.
        :return:
        """
        total_employees = self._shift_employees[shift_pos]

        # STRANGE THINGS GOING ON HERE
        #shift_block = [f'{self._weekdays[day][:2]}: Employee {id} S{shift_pos}' for id in range(total_employees)]
        shift_block = [f'{self._weekdays[day][:2]} S{shift_pos} Emp. {id}' for id in range(total_employees)]
        #shift_block = [f'Emp. {id}' for id in range(total_employees)]
        # change employee num based on previous' rows max number of employees
        #new_employee_number = shift_num
        return shift_block


    def _createLayout(self):
        """
        Creates header and table for Weekly Schedule.
        :return: None
        """
        # num_shifts  =   number of shifts in a day
        # num_days    =   number of days
        # num_emps    =   number of employees per shift
        # num_shifts x num_days x num_emps matrix
        num_shifts, num_days, num_emps = self.total_shifts, self._days, self.max_employees_per_shift
        self.table = [[self._setShiftBlock(shift_pos+1, day) for day in range(self._days)]
                        for shift_pos in range(self.total_shifts)]
        # reshape format of table
        #   from:   [shift_number][day][employees per day]
        #   to:     [shift_number][employees_id][day]
        self.schedule = [transpose(matrix) for matrix in self.table]

        #self.layout = [self._headings] + [table]
        return None

    def _display(self):
        """
        Print the schedule to the Command Line.
        Later, show the GUI for schedule.
        :return: None
        """
        print_header(self._weekdays)
        print_schedule(self.schedule)
        return None

    def setSchedule(self):
        """
        Layout for Week Schedule.
        :return: None
        """
        self._setShiftNumbers()
        self._createLayout()
        self._display()
        return None

def transpose(matrix):
    """
    Transpose matrix.
    :return: T (2D array)
    """
    zipped = zip(*matrix)
    T = [list(row) for row in zipped]
    return T

def print_schedule(schedule):
    """
    Print schedule.
    :return: None
    """
    for shift in schedule:
        print(f"Shift {schedule.index(shift)+1}:")
        for emp_row in shift:
            print("    ", end='')
            for emp_id in emp_row:
                print(f"{emp_id.center(13)}", end='    ')
            print()
        print()
    return None

def print_header(header):
    """
    Print header: Days of Week
    :return: None
    """
    for x in header:
        print(f"{x.center(18)}", end='')
    print()
    return None
