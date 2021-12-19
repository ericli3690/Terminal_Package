"""
DELAY.PY VERSION 1.0
Temporarily stalls the terminal
"""

import time

def delay(interval):
  """delay(interval):
  Repeatedly refreshes the line, inputting a new dot every second until the amount of dots equals parameter INTERVAL (in seconds)"""
  dots_to_print = ' '
  for dot in range(interval):
    dots_to_print += '.'
    print(dots_to_print, end='\r')
    # \r clears the line
    time.sleep(1)
  print()