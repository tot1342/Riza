from TradeAPI import TradeAPI
from PublicAPI import PublicAPI
from TerminalOutput import TerminalOutput

if __name__ == '__main__':
    # Example of the some methods from public and private API parts

    # Connecting parts of Riza
    api = PublicAPI()
    trade_api = TradeAPI(key='224D93ACB44484DEE7840306D0301201', secret_key='b084908abad152cf287a5ac199a11192')
    to = TerminalOutput()

    # Demonstration of methods
    asks, bids = api.get_open_orders('ETC', 'USD', 2)
    last_transactions = api.get_closed_orders(limit=2)
    account_info = trade_api.get_info()

    # Nice output
    to.print_get_open_orders(asks, bids)
    to.print_get_closed_orders(last_transactions)
    to.print_json(account_info)
