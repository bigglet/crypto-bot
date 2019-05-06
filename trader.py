from kucoin.client import Client
from decouple import config

class Trader:
    def __init__(self, use_sandbox):
        if(use_sandbox is True):
            self.client = Client( config('SAND_PUBLIC'), config('SAND_SECRET'), config('PASS_CODE'), sandbox=True )
        else:
            self.client = Client( config('PUBLIC_KEY'), config('SECRET_KEY'), config('PASS_CODE') )

    def get_market_list(self):
        return self.client.get_market_list()
