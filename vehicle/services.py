import requests
from rest_framework import status

from config import settings


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        f'{settings.CUR_API_URL}/v3/latest?apikey={settings.CUR_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
        #print(response.json())
        # >>> {'meta': {'last_updated_at': '2024-08-11T23:59:59Z'}, 'data': {'RUB': {'code': 'RUB', 'value': 88.7374299952}}}

    return usd_price