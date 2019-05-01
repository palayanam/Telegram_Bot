token = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE'

import requests

BASE_URL = 'https://api.telegram.org/bot727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE/'
r_getMe = requests.get(f'{BASE_URL}getMe')

r_getUpdates = requests.get(f'{BASE_URL}getUpdates')