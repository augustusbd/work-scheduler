# Python Imports
from random import randint

class Scheduler():
    def __init__(self):
        self._weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._headings = [''] + self._weekdays # empty space for axis titles
        self._days = 7
        self._total_shifts = 4
        self._max_employees = 4
        #self.setSchedule()


    def _setShiftNumbers(self):
        """
        Determines number of employees per shift.
        :return: None
        """
        self._max_shift_employees = {}
        for x in range(1, self._total_shifts + 1):
            # self._max_shift_employees[x] = randint(2, self._max_employees)
            self._max_shift_employees[x] = self._max_employees
        return None

    # Sets the employees to a spepcic Shift Block for the day
    def _setShiftBlock(self, shift_pos, day):
        """
        List of employees per shift.
        :return:
        """
        total_employees = self._max_shift_employees[shift_pos]

        # STRANGE THINGS GOING ON HERE
        #shift_block = [f'{self._weekdays[day][:2]}: Employee {id} S{shift_pos}' for id in range(total_employees)]
        shift_block = [f'S{shift_pos} Emp. {id}' for id in range(total_employees)]
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
        num_shifts, num_days, num_emps = self._total_shifts, self._days, self._max_employees
        self.table = [[self._setShiftBlock(shift_pos+1, day) for day in range(self._days)]
                        for shift_pos in range(self._total_shifts)]
        # reshape format of table
        #   from:   [shift_number][day][employees per day]
        #   to:     [shift_number][employees_id][day]
        self.schedule = [transpose(matrix) for matrix in self.table]

        #self.layout = [self._headings] + [table]

    def setSchedule(self):
        """
        Layout for Week Schedule.
        :return: None
        """
        self._setShiftNumbers()
        self._createLayout()

        print_header(self._weekdays)
        print_schedule(self.schedule[:])



def transpose(matrix):
    """
    Transpose matrix.
    :return:
    """
    zipped = zip(*matrix)
    T = [list(row) for row in zipped]
    return T


def print_schedule(schedule):
    for shift in schedule:
        print(f"Shift {schedule.index(shift)+1}:")
        for emp_row in shift:
            print("    ", end='')
            for emp_id in emp_row:
                print(f"{emp_id.center(13)}", end='    ')
            print()
        print()

def print_header(header):
    for x in header:
        print(f"{x.center(18)}", end='')
    print()
