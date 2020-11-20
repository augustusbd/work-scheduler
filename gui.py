import PySimpleGUI as sg

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
headings = [''] + weekdays # empty space for axis titles


def setRowText(row, column):
    # Text for inside table
    if column != 0:
        sgText = sg.Text(f'Employee{row}',
                          size=(14, 1),
                          text_color='black',
                          background_color='white',
                          auto_size_text=True,
                          justification='center')
    # set the Row Heading Text
    else:
        sgText = sg.Text(f'Shift{row}',
                     size=(14, 1),
                     text_color='blue',
                     auto_size_text=True,
                     justification='center')
    return sgText

def setHeading(text):
    sgText = sg.Text(text,
                     size=(14,1),
                     auto_size_text=True,
                     justification='center')
    return sgText

# Define the window's contents (layout): Header, Schedule Table
def createLayout(headings=weekdays):
    # Header
    header = [[setHeading(h) for h in headings]]

    # Schedule Table
    table = [[setRowText(row, col) for col in range(len(headings))] for row in range(5)]

    layout = header + table + [[sg.Button('Ok')]]
    return layout

# Create the Window
def createWindow():
    layout = createLayout(headings)
    window = sg.Window('Weekly Schedule', layout, font='Courier')
    return window

def show():
    window = createWindow()
    event, values = window.read(close=True)
