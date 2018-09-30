import requests, json
import traceback
from exceptions import ConnectionFailed

class PublicAPI(object):
    def __init__(self):
        self.base_url = 'https://yobit.net/api/3/'

    def get_open_orders(self, currency='BTC', equivalent='USD', limit=10, err_time=1):
        if limit < 1 or limit > 2000:
            print('The limit is invalid')
            limit = 150
        try:
            response = requests.get('{}depth/{}_{}?limit={}'.format(
                self.base_url, currency.lower(), equivalent.lower(), limit))
        except:
            error = ConnectionFailed(self.get_open_orders, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()

        if response.status_code != 200:
            error = ConnectionFailed(self.get_open_orders, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()
        else:
            json_response = json.loads(response.text)
            asks = json_response['{}_{}'.format(currency.lower(), equivalent.lower())]['asks']
            bids = json_response['{}_{}'.format(currency.lower(), equivalent.lower())]['bids']

            return (asks, bids)

    def get_closed_orders(self, currency='BTC', equivalent='USD', limit=10, err_time=1):
        if limit < 1 or limit > 2000:
            print('The limit is invalid')
            limit = 150
        try:
            response = requests.get('{}trades/{}_{}?limit={}'.format(
                self.base_url, currency.lower(), equivalent.lower(), limit))
        except:
            error = ConnectionFailed(self.get_closed_orders, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()

        if response.status_code != 200:
            error = ConnectionFailed(self.get_closed_orders, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()
        else:
            json_response = json.loads(response.text)
            last_transactions = json_response[
                '{}_{}'.format(currency.lower(), equivalent.lower())]

            return last_transactions

    def get_market_info(self, currency='BTC', equivalent='USD', err_time=1):
        try:
            response = requests.get('{}info'.format(self.base_url))
        except:
            error = ConnectionFailed(self.get_market_info, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()

        if response.code != 200:
            error = ConnectionFailed(self.get_market_info, message=traceback.format_exc(),
                                   locals(), err_time+=1)
            error.log(); error.repeat()
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

    def get_market_stats(self, currency='BTC', equivalent='USD', err_time=1):
        try:
            response = requests.get('{}ticker/{}_{}'.format(self.base_url, currency.lower(), equivalent.lower()))
        except:
            error = ConnectionFailed(self.get_market_stats, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()

        if response.status_code != 200:
            error = ConnectionFailed(self.get_market_stats, message=traceback.format_exc(),
                                   locals(), err_time+=1); error.log(); error.repeat()
        else:
            json_response = json.loads(response.text)

            return json_response
