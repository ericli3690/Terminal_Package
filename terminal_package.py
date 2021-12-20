"""
TERMINAL_PACKAGE VERSION 1.0
ERIC LI 2021

Helps facilitate basic terminal actions
Includes: color_print, colored, marker, ask, delay
"""

from os import system
from time import sleep

# available colors
colors = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}

def color_print(text:str, color:str, is_input=False, insert_end='\n'):
  """
  color_print(text, color, is_input, insert_end)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Prints the text parameter as a given color.
  insert_end is used for the 'end' parameter in print statements; is_input will allow an input to be created instead."""
  
  # colors.get checks if the color provided in the parameters matches any key in the dictionary
  if colors.get(color):
    # print <start color><text><end color>, end="<end>"
    if is_input:
      input(f"\033[1;{colors[color]};40m{text}\033[1;37;40m")
    else:
      print(f"\033[1;{colors[color]};40m{text}\033[1;37;40m", end=insert_end)
  else:
    # throw error, color not found
    raise ValueError("Invalid color: " + color)

def colored(text:str, color:str):
  """
  colored(text, color)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Returns the text parameter as a given color.
  """
  # color located in colors dictionary
  if colors.get(color):
    # return the text with the surrounding color markers
    return f"\033[1;{colors[color]};40m{text}\033[1;37;40m"
  else:
    # else raise an error, color not found
    raise ValueError("Invalid color: " + color)

def marker(color:str='white'):
  """
  colored(text, color)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Returns the escape sequence for a given color.
  """
  if colors.get(color):
    # just return the tag
    return f"\033[1;{colors[color]};40m"
  else:
    # color not found
    raise ValueError("Invalid color: " + color)

def ask(
  prompt:str,
  reply_filter,

  disallow_null:bool=True,
  clear_console:dict={"on_true": False, "on_false": False},
  colors:dict={"success": "green", "failure": "red"}
):
  """
  ask(prompt, filter, disallow_null, clear_console, colors)
  define a filter, then call ask:
    def myFilter(reply):
      if (reply == "0"):
        return False, 'This value is not allowed.'
      else:
        return True, 'Value accepted.'
    ask("Enter a non-zero character.", myFilter)
  disallow_null is true by default; clear_console on user success and failure are both false by default; success color and failure color are green and red respectively by default
  """
  # until the user enters a permissible answer
  while True:
    # prompt the user
    reply = input(prompt)

    # null catch
    if disallow_null and reply == "":
      if clear_console["on_false"]:
        system("clear")
      color_print("Please enter a value.", colors["failure"])
      continue # go back to the top of the loop
    
    # use the dev-provided filter
    reply_allowed = reply_filter(reply)

    # the dev-provided filter should return a tuple, if not, then log an error
    if type(reply_allowed) != tuple:
      raise ValueError(
        f"""
      
        {marker("yellow")}Developer: When using ask(), please return a two-element tuple of a boolean (for whether the user answer was valid) followed by an error or success message. For example:
        
        if (reply == "0"):
          return False, 'This value is not allowed'{marker()}
          
        User: Please contact this program's developer.""")

    # if the dev's filter returns true for the user's input, then print the dev's provided success statement and return the reply
    if reply_allowed[0]:
      if clear_console["on_true"]:
        system("clear")
      color_print(reply_allowed[1], colors["success"])
      return reply
    else:
      # else try again, return to the top of the loop
      if clear_console["on_false"]:
        system("clear")
      color_print(reply_allowed[1], colors["failure"])
      continue

def delay(interval):
  """delay(interval):
  Repeatedly refreshes the line, inputting a new dot every second until the amount of dots equals parameter INTERVAL (in seconds)"""
  dots_to_print = ' '
  for dot in range(interval):
    dots_to_print += '.'
    print(dots_to_print, end='\r')
    # \r clears the line
    sleep(1)
  print()