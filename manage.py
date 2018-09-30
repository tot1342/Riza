

# TODO:
# Вообще этот файл нужен будет для управления из командной строки ботом
# по аналогии с тем, как это делается в Django:
# python3 manage.py importStats -f 11.12.2018.cvs -t myServer@ssh...
# Веб приложения не будет иметь доступа непосредственно к боту (для секьюрити),
# будет иметь доступ только к БД и к этому manage.py

# Пока это аналог main.py и запускаем отсюда код.




from tradeAPI import TradeAPI
from publicAPI import PublicAPI

# Example of the some methods from public and private API parts

# Connecting parts of Riza
api = PublicAPI()
trade_api = TradeAPI(key='224D93ACB44484DEE7840306D0301201', secret_key='b084908abad152cf287a5ac199a11192')
to = TerminalOutput()

# Demonstration of methods
asks, bids = api.get_open_orders('ETC', 'USD', 2)
last_transactions = api.get_closed_orders(limit=2)
account_info = trade_api.get_info()

print(account_info)
