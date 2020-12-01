# Python imports
import random

# PySimpleGUI imports
import PySimpleGUI as sg

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_heading = [''] + weekdays # empty space for axis titles


def setShiftNumber(row):
    """
    Determines number of employees per shift.
    :return:
    """
    # max of 4 employees per shift
    max_shift_employees = {1:3, 2:4, 3:4, 4:3}
    shift_num = random.randint(1, max_shift_employees[row])
    return shift_num

# Sets the employees to a spepcic Shift Block for the day
def setShiftBlock(row):
    shift_num = setShiftNumber(row)
    shift_block =  [[sg.Text(f'Employee {num}',
                             size=(5,1),
                             text_color='black',
                             background_color='white',
                             auto_size_text=True,
                             justification='center')] for num in range(shift_num)]
    new_employee_number = shift_num
    return shift_block


# Sets the employees to a specific Shift for the week
def setShiftRow(row, column):
    # Text for inside table
    if column != 0:
        return setShiftBlock(row)
    # set the Row Heading Text
    else:
        sgText = sg.Text(f'Shift {row}',
                     size=(14, 1),
                     text_color='blue',
                     auto_size_text=True,
                     justification='center')
        return sgText

def setBlockTable():
    """
    Create Table for Schedule
    :return:
    """
    shift_num = 4
    shift_block = [f'Employee {num}' for num in range(shift_num)]

    block = sg.Table(values=shift_block,
                     num_rows=len(shift_block),
                     headings=weekdays_heading
                    )
    return block

def setHeading(text):
    sgText = sg.Text(text,
                     size=(14,1),
                     auto_size_text=True,
                     justification='center')
    return sgText

# Define the window's contents (layout): Header, Schedule Table
def createLayout(headings=weekdays):
#     """
#     Creates header and table for Weekly Schedule GUI.
#     :return:
#     """
    # Header
    header = [[setHeading(h) for h in weekdays_heading]]

    # Schedule Table
    data = [[setBlockTable() for col in range(len(weekdays_heading))] for row in range(1, 5)]
    table = [[sg.Table(values=data,
                       num_rows=len(data),
                       headings=weekdays_heading)]]
    #table = [[setShiftRow(row, col) for col in range(len(weekdays_heading))] for row in range(1, 5)]

    layout = header + table + [[sg.Button('Ok')]]
    return layout

# Create the Window
def createWindow():
    layout = createLayout(weekdays_heading)
    window = sg.Window('Weekly Schedule', layout, font='Courier')
    return window

def show():
    window = createWindow()
    event, values = window.read(close=True)
