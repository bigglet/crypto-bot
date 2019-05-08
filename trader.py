from kucoin.client import Client
from kucoin.exceptions import KucoinAPIException
from decouple import config

class Trader:
    def __init__(self, use_sandbox):
        if(use_sandbox is True):
            self.client = Client( config('SAND_PUBLIC'), config('SAND_SECRET'), config('PASS_PHRASE'), sandbox=True )
        else:
            self.client = Client( config('PUBLIC_KEY'), config('SECRET_KEY'), config('PASS_PHRASE') )

    def sell_all_currencies(self):
        for coins_in_wallet in self.client.get_accounts():
            if(coins_in_wallet["currency"] != "BTC"):
                print( coins_in_wallet["currency"] + ":\t" + coins_in_wallet["balance"] + "\t/\t" + coins_in_wallet["available"] )
                sell_pair = coins_in_wallet["currency"] + "-BTC"
                print( "Create Sell order for: " + sell_pair )
                try:
                    self.client.create_market_order(sell_pair, 'sell', size=coins_in_wallet["available"])
                except KucoinAPIException as error:
                    print("DID NOT SELL")
                    print( error )

    def get_symbol_list(self, quote_currency=None):
        currency_symbol_list = []
        if(quote_currency is None):
            for currency_stats in self.client.get_symbols():
                currency_symbol_list.append( currency_stats["symbol"] )
        else:
            for currency_stats in self.client.get_symbols():
                if( currency_stats["symbol"].endswith(quote_currency) ):
                    currency_symbol_list.append( currency_stats["symbol"] )

        return currency_symbol_list
