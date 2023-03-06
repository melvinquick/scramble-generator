# --- Libraries --- #

import PySimpleGUI as sg
import functions

# --- Window Settings --- #

# Set theme
sg.theme('DarkPurple')

# Create layout for the window
layout = [[sg.Text('Enter number of desired moves, select your puzzle from the dropdown (leave blank for defaults), then hit generate!', pad=6)],
          [sg.InputText(default_text='', size=(10, 1), pad=6, justification='center'), sg.Combo(values=['2x2', '3x3'], default_value='3x3', pad=6), sg.Button(
              'Generate Scramble!', pad=6), sg.Button('Exit', pad=6)],
          [sg.Text(key='-SCRAMBLE-', pad=6)]]

# Create the window
window = sg.Window('Scramble Generator', layout, icon='G:/My Drive/Workspaces/GitHub/scramble-generator/images/logo-512x512.ico',
                   element_justification='center')

# Event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Generate Scramble!' and values[0] != '':
        if values[1] == '2x2':
            window['-SCRAMBLE-'].update(functions.two_by_two(int(values[0])))
        if values[1] == '3x3':
            window['-SCRAMBLE-'].update(functions.three_by_three(int(values[0])))
    if event == 'Generate Scramble!' and values[0] == '':
        if values[1] == '2x2':
            window['-SCRAMBLE-'].update(functions.two_by_two())
        if values[1] == '3x3':
            window['-SCRAMBLE-'].update(functions.three_by_three())
        # window['-SCRAMBLE-'].update('The number of moves cannot be empty!')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
