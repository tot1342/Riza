# AUTHOR: github.com/me0em
# TODO: Написать APIException

import requests
import json


class PublicAPI(object):
    class APIException(Exception):

        pass  # TODO: сделать заглушку, чтобы на одном зафакапленном реквесте
    # не летел все трейдинги и рассчёты

    def __init__(self):
        self.base_url = 'https://yobit.net/api/3/'

    def get_open_orders(self, currency='BTC', equivalent='USD', limit=10):
        if limit < 1 or limit > 2000:
            print('The limit is invalid')
            limit = 150
        try:
            response = requests.get('{}depth/{}_{}?limit={}'.format(
                self.base_url, currency.lower(), equivalent.lower(), limit))
        except:
            raise APIException('Error: Check API request url or Internet connection')
        if response.status_code != 200:
            raise APIException('Looks like API was changed or server is down')

        else:
            json_response = json.loads(response.text)
            asks = json_response['{}_{}'.format(currency.lower(), equivalent.lower())]['asks']
            bids = json_response['{}_{}'.format(currency.lower(), equivalent.lower())]['bids']

            return (asks, bids)

    def get_closed_orders(self, currency='BTC', equivalent='USD', limit=10):
        if limit < 1 or limit > 2000:
            print('The limit is invalid')
            limit = 150
        try:
            response = requests.get('{}trades/{}_{}?limit={}'.format(
                self.base_url, currency.lower(), equivalent.lower(), limit))
        except:
            raise APIException('Error: Check API request url or Internet connection')

        if response.status_code != 200:
            raise APIException('Looks like API was changed or server is down')

        else:
            json_response = json.loads(response.text)
            last_transactions = json_response[
                '{}_{}'.format(currency.lower(), equivalent.lower())]

            return last_transactions

    def get_market_info(self, currency='BTC', equivalent='USD'):
        try:
            response = requests.get('{}info'.format(self.base_url))
        except:
            raise APIException('Error: Check API request url or Internet connaction')
        if response.code != 200:
            raise APIException('Looks like API was changed or server is down')

        else:
            json_response = json.loads(response.text)
            key_pair = '{}_{}'.format(
                currency.lower(),
                equivalent.lower())
            val_pair = json_response['pairs']

            return {
                'server_time': json_response['server_time'],
                'pairs': {key_pair: val_pair['pairs']},
            }

    def get_market_statistics(self, currency='BTC', equivalent='USD'):
        try:
            response = requests.get('{}ticker/{}_{}'.format(self.base_url, currency.lower(), equivalent.lower()))
        except:
            raise APIException('Error: Check API request url or Internet connaction')
        if response.status_code != 200:
            raise APIException('Looks like API was changed or server is down')
        else:
            json_response = json.loads(response.text)

            return json_response
