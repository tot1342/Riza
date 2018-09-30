from urllib.parse import urlencode
import hmac, hashlib
import requests, json
from exceptions import ConnectionFailed

class TradeAPI(object):
    def __init__(self, key: str, secret_key: str):
        self.api_url = "https://yobit.net/tapi/"
        # Сreate it in our account
        self.key = key
        self.secret_key = secret_key

    def get_headers(self, data: dict):
        data['nonce'] = 35 # increment this request counter, TODO: secrets.json
        sign = hmac.new(   # make sign hash string
            self.secret_key.encode(),
            urlencode(data).encode(),
            hashlib.sha512).hexdigest()

        return {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Sign': sign,
            'Key': self.key,
        }

    def get_info(self):
        # Return account info, server time etc
        data = {
            "method": "getInfo",
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def WithdrawCoins(self, coinName: str, amount: float, address: str):
        # Transfer money to your wallet [adress]
        data = {
            'method': 'WithdrawCoinsToAddress',
            'coinName': coinName,
            'amount': amount,
            'address': address
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def Trade(self, pair: str, type: str, rate: float, amount: float):
        # pair - валюта, type - тип операции, rate - курс, amount - количество
        data = {
            'method': 'Trade',
            'pair': pair,
            'type': type,
            'rate': rate,
            'amount': amount
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def ActiveOrders(self, pair: str):
        # Return active orders list
        data = {
            'method': 'ActiveOrders',
            'pair': pair
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def OrderInfo(self, order_id: int):
        # Specific order info
        data = {
            'method': 'OrderInfo',
            'order_id': order_id
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def CancelOrder(self, order_id: int):
        data = {
            'method': 'CancelOrder',
            'order_id': order_id
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def TradeHistory(self, pair, fro=0, count=1000, from_id=0, end_id=10000,
                     order='DESC', since=0, end=10000):
        data = {
            'method': 'TradeHistory',
            'pair': pair,
            'fro': fro,         # номер сделки, с которой начинать вывод
            'count': count,     # количество сделок для вывода
            'from_id': from_id, # ID сделки, с которой начинать вывод
            'end_id': end_id,   # ID сделки, на которой заканчивать вывод
            'order': order,     # сортировка при выводе (значения: ASC или DESC
            'since': since,     # с какого времени начинать вывод
            'end':end           # на каком времени заканчивать вывод
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data),data=data)
        json_response = json.loads(response.text)

        return json_response

    def GetDepositAddress(self, coinName, need_new: bool = 0):
        # Return адрес пополнения
        data = {
            'method': 'GetDepositAddress',
            'coinName': coinName,
            'need_new': need_new
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data),data=data)
        json_response = json.loads(response.text)

        return json_response

    def CreateYobicode(self, currency: str, amount: float):
        # Creating Yobicodes (coupons)
        data = {
            'method': 'CreateYobicode',
            'currency': currency,
            'amount': amount
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

    def RedeemYobicode(self,coupon: str):
        # Using Yobicodes (coupons)
        data = {
            'method': 'RedeemYobicode',
            'coupon': coupon,
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response
