"""
TERMINAL_PACKAGE VERSION 2.0
ERIC LI 2021

Helps facilitate basic terminal actions
Includes: color_print, colored, marker, ask, delay, nest
"""

from os import system
from time import sleep

def marker(color:str='white'):
  """
  colored(text, color)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Returns the escape sequence for a given color.
  """
  # available colors
  colors = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}
  # if the requested color exists
  if colors.get(color):
    # just return the tag
    return f"\033[1;{colors[color]};40m"
  else:
    # color not found
    raise ValueError("Invalid color: " + color)

def colored(text:str, color:str):
  """
  colored(text, color)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Returns the text parameter as a given color.
  """
  # put tags around it
  return f"{marker(color)}{text}{marker()}"

def color_print(text:str, color:str, is_input=False, insert_end='\n'):
  """
  color_print(text, color, is_input, insert_end)
  allowed colors include:
  BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE

  Prints the text parameter as a given color.
  insert_end is used for the 'end' parameter in print statements; is_input will allow an input to be created instead."""
  # if using input
  if is_input:
    input(colored(text, color))
  else:
    # else just print, but also add the insert_end
    print(colored(text, color), end=insert_end)

def nest(
  text:str,
  top_icon:str="=",
  side_icon:str="",
  corner_icon:str="",
  left_right_padding:int=0,
  up_down_padding:int=0
):
  """
  text, top_icon, side_icon, corner_icon, left_right_padding, up_down_padding
  DEFAULTS TO: None, '=', '', '', 0, 0
  Nests 'text' in a box with 'top_icon' on the top and bottom, 'side_icon' on the left and right, and 'corner_icon' on the corners; can also add interior padding via left_right_padding and up_down_padding
  Returns a string.
  Try nesting nests in nests!
  """
  # ensuring that padding is not affected if corner is empty, or if side is empty, etc.
  if side_icon != "" and corner_icon == "":
    corner_icon = " "
  elif corner_icon != "" and side_icon == "":
    side_icon = " "
  if corner_icon != "" and top_icon == "":
    top_icon = " "

  # split text into an array of lines to figure out the longest line
  line_by_line_text = text.split("\n")
  longest_line_length = 0
  for line in line_by_line_text:
    if len(line) > longest_line_length:
      longest_line_length = len(line)
  
  # insert more lines based on up-down padding
  for new_line in range(up_down_padding):
    line_by_line_text.insert(0, "")
    line_by_line_text.append("")

  # make all lines equal length by appending spaces to the ends
  # then, surround them with left-right padding and side-icons
  for i, line in enumerate(line_by_line_text):
    line_by_line_text[i] = (
      side_icon + (
        " " * left_right_padding + (
          line + (
            " " * (
              longest_line_length - len(line)
            )
          )
        ) + " " * left_right_padding
      ) + side_icon
    )
  
  # if theres a top row
  if top_icon != "" or corner_icon != "":
    # create a row of top=icons until it equals the length of all the other lines in line_by_line_text, then add corner icons to either side
    icon_row = (
      corner_icon + (
        top_icon * (
          left_right_padding + (
            longest_line_length
          ) + left_right_padding
        )
      ) + corner_icon
    )
    # append this to the top and bottom of line_by_line_text
    line_by_line_text.insert(0, icon_row)
    line_by_line_text.append(icon_row)

  # join line_by_line text together using line breaks and return
  return (
    "\n".join(line_by_line_text)
  )

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