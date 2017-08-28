'''Fetches the stock exchange closing values from tdcfinancial on a given day,
sorted alphabetically by company name.
'''

__last_change__ = '2017.08.25.'

import os
import logging
import stock_exchange_data
import sys

def main():

    logging.basicConfig(level=logging.INFO)
    
    past_market_data = stock_exchange_data.MarketData()
    past_market_data.load_from_file()
    
    past_market_data.clean()

    actual_market_data = stock_exchange_data.MarketData()
    actual_market_data.load_from_html(True)
    
    past_market_data.append(actual_market_data.marketdata)
    past_market_data.clean()
    
    past_market_data.save_to_file()

    # wait for key stroke
    os.system('pause')

if __name__ == '__main__':
    sys.exit(main())
