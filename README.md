# PySimpleGUI
 --> Create simple Apps using the PySimpleGUI library.
 
Install PySimpleGUI: pip install PySimpleGUI


Skeleton of a gui app:

    import PySimpleGUI as sg
    
    layout = [
        []
    ]
    
    window = sg.Window('',layout)
    
    while True:
        event, values = window.read()
    
        if event == sg.WIN_CLOSED:
            break
            
    window.close()

