from kucoin.client import Client

class Trader:
    def __init__(self, api_key, api_secret, api_passphrase):
        self.client = Client(api_key, api_secret, api_passphrase)
