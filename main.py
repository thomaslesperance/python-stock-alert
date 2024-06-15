"""
Script to check a given stock api for a given stock at a given time interval.
If the stock has increased/decreased by a given percentage limit, an email is sent
using the STL SMTP features for a users gmail.

Author: Thomas L'Esperance
"""

import check_time
import check_stock
import email_notification
from sys import argv

interval_arg = argv[1]
percent_arg = argv[2]
stock_id_arg = argv[3]
email_server_arg = argv[4]
# ...
# script argument n = argv[n]

def python_stock_alert(interval, percent, stock_id, email_server):
  """docstring explaining this function, specifically"""

  print(f'Hello, and thank you for using python-stock-alert!\n\nStarting to check stock ID {stock_id} every {interval} minutes for an increase/decrease greater than {percent}%.\nUsing {email_server} SMTP server to notify you.\n\nPress "Ctrl + c" to stop.')
  
  timer = check_time.CheckTime()
  # stock = check_stock.CheckStock()

  # Check stock once and email starting value(s)
  print('\n\ndoing an initial check on your stock...')
  
  # Pressing Ctrl-C sends the built-in KeyboardInterrupt exception and allows user to stop script from command line.
  try:
    while True:

      print('while loop iteration')
      print(timer.get_time())
      print(timer.check_time(interval))

      if timer.check_time(interval):
        print('\n\nchecking stock...')
        # if stock.check_stock(percent):
        #   # do some email stuff
        #   print('doing email stuff')

  except KeyboardInterrupt:
    # Cleanup operations, such as cancelling any connections to SMTP if applicable...
    print('\n\ndoing cleanup up stuff...')
    
  finally:
    print(f'\n\nExited python-stock-alert\n\n') 
    
if __name__ == '__main__':
  python_stock_alert(interval_arg, percent_arg, stock_id_arg, email_server_arg)
