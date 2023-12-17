# pip install beautifulsoup4
# pip install requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

'''
[--input--][Button]
|         |[ City ]
|   IMG   |[ TIME ]   
|         |[ TEMP ]
(image_col)(info_col)
'''

def get_weather_data(location):
    url = f"https://www.google.com/search?q=weather+{location.replace(' ','')}"
    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)

    soup    = bs(html.text, 'html.parser')
    name    = soup.find('span', attrs = {'class': 'BBwThe' }).text 
    time    = soup.find('div' , attrs = {'id': 'wob_dts'}).text 
    weather = soup.find('div' , attrs = {'id': 'wob_dcp'}).text 
    temp    = soup.find('span', attrs = {'id': 'wob_ttm'}).text 
    return name, time, weather, temp


sg.theme('DarkGrey')

image_col = sg.Column([[sg.Image(key = '-IMAGE-', background_color='#FFFFFF')]])
info_col  = sg.Column([
    [sg.Text('', key = '-LOCATION-', font = 'Calibri 30', background_color = '#FF0000',                         pad = 0,      visible = False)],
    [sg.Text('', key = '-TIME-',     font = 'Calibri 16', background_color = '#000000', text_color = '#FFFFFF', pad = 0,      visible = False)],
    [sg.Text('', key = '-TEMP-',     font = 'Calibri 16', background_color = '#FFFFFF', text_color = '#000000', pad = (0,10), visible = False, justification = 'center')]
    ])

layout = [
    [sg.Input(expand_x = True, key = '-INPUT-'), sg.Button('Enter', button_color = '#000000', border_width = 0)],
    [image_col,info_col]
]

window = sg.Window('Weather',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break


    if event == 'Enter':
        name, time, weather, temp = get_weather_data(values['-INPUT-'])
        window['-LOCATION-'].update(name, visible = True)
        window['-TIME-'    ].update(time, visible = True)
        window['-TEMP-'    ].update(f'{temp} \u2103  ({weather})', visible = True)

        # sun
        if weather in ('Sun','Sunny','Clear','Clear with periodic clouds', 'Mostly sunny'):
            window['-IMAGE-'].update('symbols/sun.png')

        # part sun
        if weather in ('Partly Sunny','Mostly Sunny','Partly cloudy','Mostly cloudy','Cloudy','Overcast'):
            window['-IMAGE-'].update('symbols/part sun.png')

        # rain
        if weather in ('Rain','Chance of Rain','Light Rain','Showers','Scattered Showers','Rain and Snow','Hail'):
            window['-IMAGE-'].update('symbols/rain.png')

        # thunder
        if weather in ('Scattered Thunderstorms','Chance of Storm','Storm','Thunderstorm','Chance of TStorm'):
            window['-IMAGE-'].update('symbols/thunder.png')

        # foggy
        if weather in ('Mist','Dust','Fog','Smoke','Haze','Flurries'):
            window['-IMAGE-'].update('symbols/fog.png')

        # snow
        if weather in ('Freezing Drizzle','Chance of Snow','Sleet','Snow','Icy','Snow Showers'):
            window['-IMAGE-'].update('symbols/snow.png')


       


window.close()