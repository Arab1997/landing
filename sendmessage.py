import requests

token = '7404402504:AAErM7qP0OUsMDU3rvT5pV1fBG5HKO3PD3Y'
chat_id = '-4212283936'
text = 'Test_2'


def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })


sendTelegram()
