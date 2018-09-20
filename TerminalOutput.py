class TerminalOutput(object):
    '''Just some color output values'''

    def __init__(self):
        self.red = "\033[0;31;40m"
        self.pink = "\033[0;35;40m"
        self.green = "\033[0;32;40m"
        self.cyan = "\033[0;36;40m"
        self.normal = "\033[0;31;40m"
        self.red = "\033[0;31;40m"
        self.bold_red = "\033[1;31;40m"
        self.end = "\033[0m"

    def print_get_open_orders(self, asks, bids):
        print('\n')
        print('BUY ORDERS')
        print('Amount: {}{}{}'.format(self.pink, len(asks), self.end))
        for item in asks:
            print(self.cyan, item, self.end)
        print('SELL ORDERS')
        print('Amount: {}{}{}'.format(self.pink, len(bids), self.end))
        for item in bids:
            print(self.cyan, item, self.end)
        print('\n')

    def print_get_closed_orders(self, last_transactions):
        print('\n')
        print(self.green + 'LAST TRANSACTIONS:', self.end)
        for transaction in last_transactions:
            print(transaction)
        print('\n')

    def print_json(self, data, n=0):
        if type(data) == dict:
            for k, v in data.items():
                print(n * '\t', k, ':')
                self.print_json(v, n + 1)
        else:
            print(n * '\t', self.cyan, data, self.end)
