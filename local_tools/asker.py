"""
ASKER.PY VERSION 1.0

Helps handle user input.
Please place this script within a package named "local_tools", together with the printer.py file.
Uses the function ask(prompt, filter), where prompt is the question posed to the user and filter is the evaluations of their reply in order to ask again after a false input.
To use, define a function with argument "reply" that checks "reply" against conditionals, and returns a tuple of either True followed by a success statement, or False followed by a failure statement. The function may not return None or any other data type. Then, use ask("str", func). If the user's input does not match your filter, ask() will automatically pose the question again to the user. If it does pass, ask() will return their answer. ask() will automatically call out null replies, but this can be disabled via disallow_null. ask()'s error/success colours and whether or not it clears the console may also be customized.

For example:
###
def myFilter(reply)
  if (reply == "0"):
    return False, 'This value is not allowed.'
  else:
    return True, 'Value accepted.'
ask("Enter a non-zero character.", myFilter)
###
"""

from local_tools.printer import color_print, marker
from os import system

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
  while True:
    reply = input(prompt)

    if disallow_null and reply == "":
      if clear_console["on_false"]:
        system("clear")
      color_print("Please enter a value.", colors["failure"])
      continue
    
    reply_allowed = reply_filter(reply)

    if type(reply_allowed) != tuple:
      raise ValueError(
        f"""
      
        {marker("yellow")}Developer: When using ask(), please return a two-element tuple of a boolean (for whether the user answer was valid) followed by an error or success message. For example:
        
        if (reply == "0"):
          return False, 'This value is not allowed'{marker()}
          
        User: Please contact this program's developer.""")

    if reply_allowed[0]:
      if clear_console["on_true"]:
        system("clear")
      color_print(reply_allowed[1], colors["success"])
      return reply
    else:
      if clear_console["on_false"]:
        system("clear")
      color_print(reply_allowed[1], colors["failure"])
      continue