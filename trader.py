from kucoin.client import Client
from decouple import config

class Trader:
    def __init__(self, use_sandbox):
        if(use_sandbox is True):
            self.client = Client( config('SAND_PUBLIC'), config('SAND_SECRET'), config('PASS_PHRASE'), sandbox=True )
        else:
            self.client = Client( config('PUBLIC_KEY'), config('SECRET_KEY'), config('PASS_PHRASE') )

    def sell_all_currencies(self):
        print( self.client.get_accounts() )

    def get_symbol_list(self, sell_currency=None):
        currency_symbol_list = []
        if(sell_currency is None):
            for currency_stats in self.client.get_symbols():
                currency_symbol_list.append( currency_stats["symbol"] )
        else:
            for currency_stats in self.client.get_symbols():
                if( currency_stats["symbol"].endswith('BTC') ):
                    currency_symbol_list.append( currency_stats["symbol"] )

        return currency_symbol_list
