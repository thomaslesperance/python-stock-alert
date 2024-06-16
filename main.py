"""
Script to check a given stock api for a given stock at a given time interval.
If the stock has increased/decreased by a given percentage limit, an email is sent
using the STL SMTP features for a users gmail.

Author: Thomas L'Esperance
"""

import time_checker
import stock_checker
import email_notification
from sys import argv

interval_arg = argv[1]
percent_arg = argv[2]
stock_symbol_arg = argv[3]
email_server_arg = argv[4]
# ...
# script argument n = argv[n]

def python_stock_alert(interval, percent, stock_symbol, email_server):
  """docstring explaining this function, specifically"""

  print(f'Hello, and thank you for using python-stock-alert!\n\nStarting to check stock ID {stock_symbol} every {interval} minutes for an increase/decrease greater than {percent}%.\nUsing {email_server} SMTP server to notify you.\n\nPress "Ctrl + c" to stop.')
  
  timer = time_checker.Timer()
  stock = stock_checker.Stock(stock_symbol)

  # Check stock once and email starting value(s)
  print('\n\ndoing an initial check on your stock...')

  stock.update_stock_data()

  print(f'Stock symbol {stock_symbol} starting out with the following data:\n\n{stock.get_stock_data()}')
  
  # Pressing Ctrl-C sends the built-in KeyboardInterrupt exception and allows user to stop script from command line.
  try:
    while True:

      if timer.check_current_minutes(interval):
        print('\n\nchecking stock again...')
        timer.set_current_minutes()

        if stock.get_stock_percent_change() >= abs(float(percent)):
          print(f'Here is the updated data:\n\n{stock.get_stock_data()}')
          # But send this to email instead

  except KeyboardInterrupt:
    # Cleanup operations, such as cancelling any connections to SMTP if applicable...
    print('\n\ndoing cleanup up stuff...')

  finally:
    print(f'\n\nExited python-stock-alert\n\n') 
    
if __name__ == '__main__':
  python_stock_alert(interval_arg, percent_arg, stock_symbol_arg, email_server_arg)
