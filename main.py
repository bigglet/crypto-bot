from trader import Trader

use_sandbox=False

def run():
    trader = initialise_trader()
    trader.sell_all_currencies()
    current_coin = 'BTC'
    #while(1):
    #    currency_symbols = trader.get_symbol_list()
    #    update_lists()
    #    check_if_enough_data()
    #    make trade()
    #    update_coin()

def initialise_trader():
    return Trader(use_sandbox)

if __name__ == '__main__':

    run()
