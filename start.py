# В данном файле список команд для мониторинга запросов к боту и от бота.
# Команды использовать ТОЛЬКО в встройном интерпритаторе <<Python IDLE>>.
# Команды записывать СТРОГО по этой последовательности. 

token = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE' #Записали токен Бота

import requests #Импортировали библиотеку для работы с запросами

BASE_URL = 'https://api.telegram.org/bot727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE/' #Основная ссылка(с токеном)

r = requests.get(f'{BASE_URL}getMe') #Запрос на информацию про бота

r = requests.get(f'{BASE_URL}getUpdates') #Запрос на получение писем к боту

payload = {} #Создание словаря ответа к юзеру

payload['chat_id'] = 461367829 #ID чата

payload['text'] = 'Habib won' #Текст сообщения

r = requests.post(f'{BASE_URL}sendMessage', data = payload) #Запрос на ответ от бота

r.json() #Команда для просмотра данных ЗАПРОСА(читать коментарии)