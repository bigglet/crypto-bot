from trader import Trader


use_sandbox=True

def run():
    trader = initialise_trader()
    print(trader.get_market_list())

def initialise_trader():
    return Trader(use_sandbox)

if __name__ == '__main__':

    run()
