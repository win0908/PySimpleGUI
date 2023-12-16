import PySimpleGUI as sg

'''
---OUTPUT---
[ AC ][ EN ]
[7][8][9][/]
[4][5][6][*]
[1][2][3][-]
[ 0  ][.][+]
'''

def create_window(theme):

    sg.theme(theme) 
    sg.set_options(font = 'Frankli 15', button_element_size = (6,3)) # font = font fontsize
    button_size = (6,3)
    layout = [
        [sg.Text(
            '', 
            font = 'Frankli 30', 
            justification = 'right', 
            expand_x = True, 
            pad = (10,20),
            right_click_menu = theme_menu,
            key = '-TEXT-')
        ],
        [sg.Button('AC', expand_x = True)  , sg.Button('EN', expand_x = True)],
        [sg.Button('7', size = button_size), sg.Button('8', size = button_size), sg.Button('9', size = button_size), sg.Button('/', size = button_size)],
        [sg.Button('4', size = button_size), sg.Button('5', size = button_size), sg.Button('6', size = button_size), sg.Button('*', size = button_size)],
        [sg.Button('1', size = button_size), sg.Button('2', size = button_size), sg.Button('3', size = button_size), sg.Button('-', size = button_size)],
        [sg.Button('0', expand_x = True)   , sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
        ]
    
    return sg.Window('Calculator',layout)


theme_menu = ['menu', ['DarkGrey5','DarkGrey8','DarkGrey11','Random']]
window = create_window('DarkGrey5')

current_num = []
full_operation = []

while True: 
    event, values = window.read()

    if event == sg.WIN_CLOSED: 
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)


    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)
         
    if event in ['+','-','*','/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')

    if event == 'EN':
        full_operation.append(''.join(current_num))
        result = eval(''.join(full_operation))
        current_num[0] = str(result)
        window['-TEXT-'].update(result)
        full_operation = []

    if event == 'AC':
        full_operation = []
        current_num = []
        window['-TEXT-'].update('')
    


window.close()
