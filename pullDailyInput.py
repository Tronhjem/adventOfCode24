import requests
from os import path

dataFileName = f'inputDay'
cookieFileNane = f'cookie'
dataFolder = f'inputData/'
extension = f'.txt'


def GetDailyData(day):
    if (path.exists(f'{dataFolder}{dataFileName}{day}{extension}')):
        print('File exists already')
        return

    if not path.exists(f'{cookieFileNane}{extension}'):
        print('No session cookie found for advent of code website')
        return

    with open(f'{cookieFileNane}{extension}', 'r') as file:
        sessionCookie = file.read()

    sessionCookie = sessionCookie.replace('\n', '')

    cookies = {
        'session': sessionCookie
    }

    url = f'https://adventofcode.com/2024/day/{str(day)}/input'
    response = requests.get(url, cookies=cookies)

    print(response)
    if response.status_code == 200:
        with open(f'{dataFolder}{dataFileName}{day}{extension}', 'w') as file:
            file.write(response.text)
        print(f'Data saved as {dataFileName}{day}{extension}')
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
