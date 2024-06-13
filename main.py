'''
docstring explaining this module(script)...
'''

import check_time
import check_stock
import email_notification
from sys import argv

# script argument 1 = argv[1]
# script argument 2 = argv[2]
# ...
# script argument n = argv[n]

def python_stock_alert(params are script arguments):
  # print(f'Hello, and thank you for using python-stock-alert!\n\nStarting to watch stock {script argument x} for an increase/decrease greater than {script argument y}.\nUsing {script argument z}   email server to notify you.\n\nPress "Ctrl + c" to stop.')
  
  check_time = check_time.CheckTime()
  check_stock = check_stock.CheckStock()

  # Check stock once and email starting value(s)
  
  # Pressing Ctrl-C sends the built-in KeyboardInterrupt exception and allows user to stop script from command line.
  try:
    while True:
      # Do some stuff with initialized objects
  except KeyboardInterrupt:
    # Cleanup operations, such as cancelling any connections to SMTP if applicable...
  finally:
    print(f'Exited python-stock-alert\n\n') 
    

# python_stock_alert(script arguments)
