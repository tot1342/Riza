from urllib.parse import urlencode
import hmac
import hashlib
import requests
import json

class TradeAPI(object):
    def __init__(self, key: str, secret_key: str):
        self.api_url = "https://yobit.net/tapi/"
        # Сreate them in an account
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

    def get_info(self):#Метод возвращает информацию о балансах пользователя и привилегиях API-ключа, время сервера.
        data = {
            "method": "getInfo",
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data), data=data)
        json_response = json.loads(response.text)

        return json_response

#дополнил/ниже всё не правильно(возможно):)
    def WithdrawCoins(self, coinName:str, amount:float, address:str):#метод вывода денег, подаётся валюта, сумма, адрес
        data = {
            'method': 'WithdrawCoinsToAddress',
            'coinName': coinName,
            'amount': amount,
            'address': address
        }

        response = requests.post(url = self.api_url, headers = self.get_headers(data['method']),
                                 data = data['coinName','amount','address'] )
        json_response = json.loads(response.text)

        return json_response

    def Trade(self, pair:str, type:str, rate:float,amount:float):#валюта, тип операции, курс,количество
        data = {
            'method': 'Trade',
            'pair': pair,
            'type': type,
            'rate': rate,
            'amount': amount
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['pair','type','rate','amount'])
        json_response = json.loads(response.text)

        return json_response

    def ActiveOrders(self, pair:str):#возвращает список активных ордеров
        data = {
            'method': 'ActiveOrders',
            'pair': pair
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['pair'])
        json_response = json.loads(response.text)

        return json_response

    def OrderInfo(self, order_id:int):#подробная информация об ордере
        data = {
            'method': 'OrderInfo',
            'order_id': order_id
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['order_id'])
        json_response = json.loads(response.text)

        return json_response

    def CancelOrder(self, order_id:int):#отменяет ордер
        data = {
            'method': 'CancelOrder',
            'order_id': order_id
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['order_id'])
        json_response = json.loads(response.text)

        return json_response

    def TradeHistory(self, pair,  fro:int = 0, count:int = 1000, from_id:int = 0, end_id:int = 10000, order:str = 'DESC',
                     since:int = 0, end:float = 10000):
        #Возвращает историю сделок. Переменные, разные параметры вывода, значения по умолчанию(с сайта)
        data = {
            'method': 'TradeHistory',
            'pair': pair,
            'fro': fro, #номер сделки, с которой начинать вывод
            'count': count,#количество сделок для вывода
            'from_id': from_id,#ID сделки, с которой начинать вывод
            'end_id': end_id,# ID сделки, на которой заканчивать вывод
            'order': order,#сортировка при выводе (значения: ASC или DESC
            'since': since,#с какого времени начинать вывод
            'end':end#на каком времени заканчивать вывод
        }


        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['pair', 'fro', 'count', 'from_id', 'end_id', 'order', 'since', 'end'])
        json_response = json.loads(response.text)

        return json_response

    def GetDepositAddress(self, coinName:str, need_new:bool = 0): #Метод возвращает адрес пополнения.
        data = {
            'method': 'GetDepositAddress',
            'coinName': coinName,
            'need_new': need_new
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['coinName','need_new'])
        json_response = json.loads(response.text)

        return json_response

    def CreateYobicode(self,currency:str,amount:float):#Метод предназначен для создания  Yobicodes (купонов).
        data = {
            'method': 'CreateYobicode',
            'currency': currency,
            'amount': amount
        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['currency', 'amount'])
        json_response = json.loads(response.text)

        return json_response

    def RedeemYobicode(self,coupon:str):#Метод предназначен для погашения Yobicodes (купонов).
        data = {
            'method': 'RedeemYobicode',
            'coupon': coupon,

        }

        response = requests.post(url=self.api_url, headers=self.get_headers(data['method']),
                                 data=data['coupon'])
        json_response = json.loads(response.text)

        return json_response