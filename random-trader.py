from kucoin.client import Client
import numpy as np
import kucoin.exceptions
import time
from decouple import config

def startup():
	client = Client(config('SECRET_KEY'), config('PUBLIC_KEY'))

	return client

def get_next_coin():
	#search coin market cap and find the next coin to buy
	while True:
		try:	
			coinz_list = client.get_coin_list()
			coin = coinz_list[np.random.randint(len(coinz_list))]['coin']
			pair = coin+'-BTC'
			price = client.get_tick(pair)['buy']
			if(price == None):
				print pair+' has no price'
				continue 

		except kucoin.exceptions.KucoinAPIException:
			print pair+' is not a coin'
			continue
		break	
	print pair+': '+str(price)

	return coin, pair, price

def buy_coin(pair, price, current_coin):
	order = None
	mma = None
	while(mma == None):
		print 'Get coin balance'
		mma = client.get_coin_balance(current_coin)
	max_amount = float(mma['balance']/(price))
	balance = np.round(max_amount,3)*0.98
	while(order == None):
		try:
			order = client.create_buy_order(pair, price*1.02, balance)
		except:
			print 'Retry'
			continue
	print order
	orderID = order['orderOid']
	return orderID

def get_bitcoin(current_coin):
	#get trade position
	balance = np.round(client.get_coin_balance(current_coin)['balance'],3)
	price  = client.get_tick(current_coin+'-BTC')['sell']

	print 'Balance of '+current_coin+':  ' + str(balance)
	print 'Buy price of BTC:  ' + str(price)
	order = None
	while(order==None):
		order = client.create_sell_order(current_coin+'-BTC',price*0.98,balance)
	orderID = order['orderOid']
	print 'Order number: '+orderID

	#Add something to check if order has been done, if not cancel the order, and change the price

	return orderID

if __name__ == '__main__':
	client = startup()
	print("Connected to coin marketcap and kucoin ....")

	current_coin = 'BTC'
	while True:
		print 'Main loop: '+current_coin
		if(current_coin == 'BTC'):
			orderID = None
			while orderID == None:	
				price = None
				while(price == None):
					next_coin, pair, price = get_next_coin()
				orderID = buy_coin(pair,price,current_coin)
				print orderID

			current_coin = next_coin

		else:
			get_bitcoin(current_coin)
			current_coin = 'BTC'
		time.sleep(60*5)
